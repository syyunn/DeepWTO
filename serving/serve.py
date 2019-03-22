import os
import sys
import json

import tensorflow as tf

from utils.misc.dict import Dotdict

sys.path.append('../')


tf.app.flags.DEFINE_integer('model_version',
                            1,
                            'Models version number.')
tf.app.flags.DEFINE_string('work_dir',
                           './runs',
                           'Working directory.')
tf.app.flags.DEFINE_integer('model_id',
                            1552899680,
                            'Model id name to be loaded.')
tf.app.flags.DEFINE_string('export_model_dir',
                           "./versions",
                           'Directory where the model exported files '
                           'should be placed.')
tf.flags.DEFINE_integer("num_classes",
                        80,
                        "Number of labels (depends on the task)")
tf.flags.DEFINE_integer("embedding_dim",
                        300,
                        "Dimensionality of character embedding "
                        "(default: 128)")
tf.flags.DEFINE_integer("pad_seq_len",
                        35842,
                        "Recommended padding Sequence length of data "
                        "(depends on the data)")
# GPU HANDLE
tf.flags.DEFINE_boolean("allow_soft_placement",
                        True,
                        "Allow device soft device placement")
tf.flags.DEFINE_boolean("log_device_placement",
                        False,
                        "Log placement of ops on devices")
tf.flags.DEFINE_boolean("gpu_options_allow_growth",
                        True,
                        "Allow gpu options growth")
# Test Parameters
tf.flags.DEFINE_integer("batch_size",
                        1,
                        "Batch Size (default: 1)")
tf.flags.DEFINE_float("threshold",
                      0.5,
                      "Threshold for prediction classes (default: 0.5)")


########################################################
# Might Be Required

TEST_DIR = 'HandWritten.json'
tf.flags.DEFINE_string("test_data_file",
                       TEST_DIR,
                       "Data source for the test data")
#######################################################

FLAGS = tf.app.flags.FLAGS

model_name = str(FLAGS.model_id)
log_folder = FLAGS.work_dir
pre_trained_model_dir = os.path.join(log_folder, model_name, "checkpoints")
checkpoint_file = tf.train.latest_checkpoint(pre_trained_model_dir)

if not os.path.exists(os.path.join(log_folder, model_name, "test")):
    os.makedirs(os.path.join(log_folder, model_name, "test"))

with open(
        log_folder + '/' + model_name + '/checkpoints/data.json', 'r') as fp:
    args = json.load(fp)

args = Dotdict(args)


def main(_):
    graph = tf.Graph()
    with tf.Session(graph=graph) as sess:
        # Load the saved meta graph and restore variables
        saver = tf.train.import_meta_graph("{0}.meta".format(
            checkpoint_file))
        saver.restore(sess, checkpoint_file)

        # Get the placeholders from the graph by name
        input_x = graph.get_operation_by_name("input_x").outputs[0]
        input_y = graph.get_operation_by_name("input_y").outputs[0]
        dropout_keep_prob = graph.get_operation_by_name(
            "dropout_keep_prob").outputs[0]
        is_training = graph.get_operation_by_name("is_training").outputs[0]

        # Tensors we want to evaluate
        scores = graph.get_operation_by_name("output/scores").outputs[0]
        gstep = graph.get_operation_by_name("Global_Step").outputs[0]
        graph.del
        print("gstep", gstep)
        # Create SavedModelBuilder class
        # defines where the model will be exported
        export_path_base = FLAGS.export_model_dir
        export_path = os.path.join(
            tf.compat.as_bytes(export_path_base),
            tf.compat.as_bytes(str(FLAGS.model_version)))
        builder = tf.saved_model.builder.SavedModelBuilder(export_path)

        # Creates the TensorInfo protobuff objects that encapsulates the
        # input/output tensors
        tensor_info_input_x = tf.saved_model.utils.build_tensor_info(
            input_x)
        tensor_info_input_y = tf.saved_model.utils.build_tensor_info(
            input_y)
        tensor_info_dropout_keep_prob = \
            tf.saved_model.utils.build_tensor_info(
            dropout_keep_prob)
        tensor_info_is_training = tf.saved_model.utils.build_tensor_info(
            is_training
        )

        # output tensor info
        tensor_info_output = tf.saved_model.utils.build_tensor_info(scores)

        # Defines the DeepLab signatures, uses the TF Predict API
        prediction_signature = (
            tf.saved_model.signature_def_utils.build_signature_def(
                inputs={'input_x': tensor_info_input_x,
                        'input_y': tensor_info_input_y,
                        'dropout_keep_prob': tensor_info_dropout_keep_prob,
                        'is_training': tensor_info_is_training},
                outputs={'prediction_result': tensor_info_output},
                method_name=
                tf.saved_model.signature_constants.PREDICT_METHOD_NAME))
        
        print(tf.saved_model.tag_constants)
        builder.add_meta_graph_and_variables(
            sess, [tf.saved_model.tag_constants.SERVING],
            signature_def_map={
                'predict':
                    prediction_signature
            })

        # export the model
        builder.save(as_text=True)
        print('Done exporting!')


if __name__ == '__main__':
    tf.app.run()
