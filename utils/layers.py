import tensorflow as tf


def linear(input_,
           output_size,
           scope="SimpleLinear"):
    """
    Linear map: output[k] = sum_i(Matrix[k, i] * args[i] ) + Bias[k]
    Args:
        input_: a tensor or a list of 2D, batch x n, Tensors.
        output_size: int, second dimension of W[i].
        scope: VariableScope for the created subgraph; defaults to
        "SimpleLinear".
    Returns:
        A 2D Tensor with shape [batch x output_size] equal to
        sum_i(args[i] * W[i]), where W[i]s are newly created matrices.
    Raises:
        ValueError: if some of the arguments has unspecified or wrong
        shape.
    """
    
    shape = input_.get_shape().as_list()
    if len(shape) != 2:
        raise ValueError("Linear is expecting 2D arguments: {0}".
                         format(str(shape)))
    if not shape[1]:
        raise ValueError("Linear expects shape[1] of arguments: {0}".
                         format(str(shape)))
    input_size = shape[1]
    
    # Now the computation.
    with tf.variable_scope(scope):
        W = tf.get_variable("W",
                            [input_size, output_size],
                            dtype=input_.dtype)
        b = tf.get_variable("b",
                            [output_size],
                            dtype=input_.dtype)
    
    return tf.nn.xw_plus_b(input_,
                           W,
                           b)


def highway_layer(input_,
                  size,
                  num_layers=1,
                  bias=-2.0,
                  f=tf.nn.relu):
    """
    Highway Network (cf. http://arxiv.org/abs/1505.00387).
    t = sigmoid(Wy + b)
    z = t * g(Wy + b) + (1 - t) * y
    where g is nonlinearity, t is transform gate, and (1 - t) is
    carry gate.
    """
    
    for idx in range(num_layers):
        g = f(linear(input_,
                     size,
                     scope=("highway_lin_{0}".
                            format(idx))))
        t = tf.sigmoid(linear(input_,
                              size,
                              scope=("highway_gate_{0}".
                                     format(idx))) + bias)
        output = t * g + (1. - t) * input_
        input_ = output
    
    return output


def do_cnn(gov_or_art,
           filter_sizes,
           embedding_size,
           num_filters,
           embedded_sentence_expanded,
           is_training,
           sequence_length,
           fc_hidden_size,
           dropout_keep_prob):
    # Create a convolution + maxpool layer for each filter size
    pooled_outputs = []
    
    for filter_size in filter_sizes:
        with tf.name_scope("conv-filter{}_{}".format(filter_size,
                                                     gov_or_art)):
            # Convolution Layer
            filter_shape = [filter_size,
                            embedding_size,
                            1,
                            num_filters]
            W = tf.Variable(tf.truncated_normal(shape=filter_shape,
                                                stddev=0.1,
                                                dtype=tf.float32),
                            name="W")
            b = tf.Variable(tf.constant(value=0.1,
                                        shape=[num_filters],
                                        dtype=tf.float32),
                            name="b")
            conv = tf.nn.conv2d(
                embedded_sentence_expanded,
                W,
                strides=[1, 1, 1, 1],
                padding="VALID",
                name="conv")
            
            conv = tf.nn.bias_add(conv, b)
            
            # Batch Normalization Layer
            conv_bn = tf.layers.batch_normalization(conv,
                                                    training=is_training)
            
            # Apply nonlinearity
            conv_out = tf.nn.relu(conv_bn,
                                  name="relu")
        
        with tf.name_scope("pool-filter{}_{}".format(filter_size,
                                                     gov_or_art)):
            # Maxpooling over the outputs
            pooled = tf.nn.max_pool(
                conv_out,
                ksize=[1, sequence_length - filter_size + 1, 1, 1],
                strides=[1, 1, 1, 1],
                padding="VALID",
                name="pool")
        
        pooled_outputs.append(pooled)
    
    # Combine all the pooled features
    num_filters_total = num_filters * len(filter_sizes)
    pool = tf.concat(pooled_outputs,
                     axis=3)
    pool_flat = tf.reshape(pool,
                           shape=[-1, num_filters_total])
    
    # Fully Connected Layer
    with tf.name_scope("fc_{}".format(gov_or_art)):
        W = tf.Variable(tf.truncated_normal(shape=[num_filters_total,
                                                   fc_hidden_size],
                                            stddev=0.1,
                                            dtype=tf.float32),
                        name="W")
        b = tf.Variable(tf.constant(value=0.1,
                                    shape=[fc_hidden_size],
                                    dtype=tf.float32),
                        name="b")
        fc = tf.nn.xw_plus_b(pool_flat, W, b)
        
        # Batch Normalization Layer
        fc_bn = tf.layers.batch_normalization(fc,
                                              training=is_training)
        
        # Apply nonlinearity
        fc_out = tf.nn.relu(fc_bn,
                            name="relu")
    
    # Highway Layer
    with tf.name_scope("highway".format(gov_or_art)):
        highway = highway_layer(fc_out,
                                fc_out.get_shape()[1],
                                num_layers=1,
                                bias=0)
    
    # Add dropout
    with tf.name_scope("dropout"):
        h_drop = tf.nn.dropout(highway,
                               dropout_keep_prob)
    return h_drop
