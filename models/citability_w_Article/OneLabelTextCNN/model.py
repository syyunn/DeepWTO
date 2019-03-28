# -*- coding:utf-8 -*-
__author__ = 'Randolph'
__modify__ = 'Zachary'

import tensorflow as tf
from utils.layers import do_cnn, fc_w_nl_bn


class OneLabelTextCNN(object):
    """A CNN for generation of text-seq encoding."""

    def __init__(self,
                 sequence_length_gov,
                 sequence_length_art,
                 vocab_size,
                 fc_hidden_size,
                 embedding_size,
                 embedding_type,
                 filter_sizes,
                 num_filters,
                 l2_reg_lambda=0.0,
                 pretrained_embedding=None):

        # Placeholders for input, output, dropout_prob and training_tag
        self.input_x_gov = tf.placeholder(tf.int32,
                                          [None, sequence_length_gov],
                                           name="input_x_gov")

        self.input_x_art = tf.placeholder(tf.int32,
                                          [None, sequence_length_art],
                                           name="input_x_art")
        
        self.input_y = tf.placeholder(tf.float32,
                                      [None, 1],
                                      name="input_y")

        self.dropout_keep_prob = tf.placeholder(tf.float32,
                                                name="dropout_keep_prob")

        self.is_training = tf.placeholder(tf.bool,
                                          name="is_training")

        self.global_step = tf.Variable(0,
                                       trainable=False,
                                       name="Global_Step")

        # Embedding Layer
        with tf.device("/cpu:0"), tf.name_scope("embedding"):
            # Use random generated the word vector by default
            # Can also be obtained through our own word vectors trained
            # by our corpus
            if pretrained_embedding is None:
                self.embedding = tf.Variable(tf.random_uniform(
                    [vocab_size,
                     embedding_size],
                    minval=-1.0,
                    maxval=1.0,
                    dtype=tf.float32),
                    trainable=True,
                    name="embedding")
            else:
                if embedding_type == 0:
                    self.embedding = tf.constant(pretrained_embedding,
                                                 dtype=tf.float32,
                                                 name="embedding")
                if embedding_type == 1:
                    self.embedding = tf.Variable(pretrained_embedding,
                                                 trainable=True,
                                                 dtype=tf.float32,
                                                 name="embedding")
            self.embedded_sentence_gov = tf.nn.embedding_lookup(
                self.embedding,
                self.input_x_gov)

            self.embedded_sentence_art = tf.nn.embedding_lookup(
                self.embedding,
                self.input_x_art)
             
            self.embedded_sentence_expanded_gov = tf.expand_dims(
                self.embedded_sentence_gov, axis=-1)
            
            self.embedded_sentence_expanded_art = tf.expand_dims(
                self.embedded_sentence_art, axis=-1)
        
        h_drop_gov_args = filter_sizes, embedding_size, num_filters
        
        h_drop_gov = do_cnn(gov_or_art="gov",
                            filter_sizes=filter_sizes,
                            embedding_size=embedding_size,
                            num_filters=num_filters,
                            embedded_sentence_expanded=
                            self.embedded_sentence_expanded_gov,
                            is_training=self.is_training,
                            sequence_length=sequence_length_gov,
                            fc_hidden_size=fc_hidden_size,
                            dropout_keep_prob=self.dropout_keep_prob)

        h_drop_art_args = filter_sizes, embedding_size, num_filters
        print("Args Bool: ", h_drop_gov_args == h_drop_art_args)
        
        h_drop_art = do_cnn(gov_or_art="art",
                            filter_sizes=filter_sizes,
                            embedding_size=embedding_size,
                            num_filters=num_filters,
                            embedded_sentence_expanded=
                            self.embedded_sentence_expanded_art,
                            is_training=self.is_training,
                            sequence_length=sequence_length_art,
                            fc_hidden_size=fc_hidden_size,
                            dropout_keep_prob=self.dropout_keep_prob)
        
        print(tf.shape(h_drop_art))
        print(tf.shape(h_drop_gov))
        
        self.h_drop = tf.concat(values=[h_drop_gov,
                                        h_drop_art],
                                axis=1)
        
        # self.h_drop = tf.Print(self.h_drop,
        #                        [tf.shape(self.h_drop),
        #                         tf.shape(h_drop_art),
        #                         tf.shape(h_drop_gov)],
        #                         message="The shapes are:")

        self.legal = fc_w_nl_bn("legal",
                                fc_hidden_size=2*fc_hidden_size,
                                input_tensor=self.h_drop,
                                output_size=fc_hidden_size,
                                is_training=self.is_training)
        
        # Final scores
        with tf.name_scope("output"):
            W = tf.Variable(tf.truncated_normal(shape=[fc_hidden_size,
                                                       1],
                                                stddev=0.1,
                                                dtype=tf.float32),
                            name="W")
            b = tf.Variable(tf.constant(value=0.1,
                                        shape=[1],
                                        dtype=tf.float32),
                            name="b")
            self.logits = tf.nn.xw_plus_b(self.legal,
                                          W,
                                          b,
                                          name="logits")
            self.scores = tf.sigmoid(self.logits,
                                     name="scores")

        # Calculate mean cross-entropy loss, L2 loss
        with tf.name_scope("loss"):
            losses = tf.nn.sigmoid_cross_entropy_with_logits(
                labels=self.input_y,
                logits=self.logits)
            losses = tf.reduce_mean(tf.reduce_sum(losses, axis=1),
                                    name="sigmoid_losses")
            l2_losses = tf.add_n([tf.nn.l2_loss(tf.cast(v, tf.float32))
                                  for v in tf.trainable_variables()],
                                 name="l2_losses") * l2_reg_lambda
            self.loss = tf.add(losses, l2_losses, name="loss")
