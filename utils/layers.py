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
