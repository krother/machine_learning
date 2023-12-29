from tensorflow.contrib.slim.nets import inception
import tensorflow.contrib.slim as slim
    
X = tf.placeholder(tf.float32, shape=[None, 299, 299, 3])
with slim.arg_scope(inception.inception_v3_arg_scope()):
    logits, end_points = inception.inception_v3(
            X, num_classes=1001, is_training=False)

predictions = end_points["Predictions"]
saver = tf.train.Saver()
