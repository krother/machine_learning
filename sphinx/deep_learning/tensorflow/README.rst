
.. _keras:

TensorFlow
==========

**TensorFlow is a Python library that makes building neural networks easy.**

Tensorflow is maintained by Google.
Next to PyTorch (Facebook) it is one of the two big Deep Learning libraries.

One key advantage of TensorFlow is that it works on many platforms, including GPUs, computing clusters, embedded devices, web browsers and phones. 


.. container:: banner warmup

   Download MNIST Data

.. highlights::

   The MNIST dataset contains images of 60,000 handwritten digits.
   It is a great example to experiment with TensorFlow:

   .. code:: python3

      from tensorflow.keras.datasets import mnist

      (Xtrain, ytrain), (Xtest, ytest) = mnist.load_data()

   To plot some of the digits use:

   .. code:: python3

      from matplotlib import pyplot as plt

      for i in range(25):
          plt.subplot(5, 5, i+1)
          plt.imshow(Xtrain[i], cmap=plt.cm.Greys)
          plt.axis('off')


   You may want to one-hot encode the target column:

   .. code:: python3

      import tensorflow as tf

      ytrain = tf.keras.utils.to_categorical(ytrain, num_classes=None, dtype='float32')
      ytest = tf.keras.utils.to_categorical(ytest, num_classes=None, dtype='float32')

   To train a Fully Connected ANN, you need to reshape X:

   .. code:: python3
    
      Xtrain = Xtrain.reshape(60000, 784)
      Xtest = Xtest.reshape(10000, 784)


.. seealso::

   Original source: `MNIST training and test data <http://yann.lecun.com/exdb/mnist/>`__



Training a Neural Network
-------------------------

.. code:: python3

   from tensorflow.keras.models import Sequential
   from tensorflow.keras.layers import Dense, Activation
   from tensorflow.keras import backend as K
   from sklearn.datasets import make_moons
   from matplotlib import pyplot as plt
   import numpy as np


   K.clear_session()

   m = Sequential([
      Dense(10, activation='relu', input_shape=(784,)),
      Dense(10, activation='relu')
      Dense(1, activation='sigmoid')
   ])

   # builds a computation graph internally
   m.compile(optimizer='adam',
            loss='binary_crossentropy',
            metrics=['accuracy'])

   # inspect all layers
   print(m.summary())

   # train the model
   h  = m.fit(X, y, epochs=100, batch_size=50, validation_split=0.2)
   print(h.history['loss'].shape)
   print(h.history['val_loss'].shape)

   # plot the learning curve
   plt.plot(h.history['loss'])

   score = m.evaluate(X, y, batch_size=50)
   print(score)

   # prediction on new data points
   print(m.predict(X[:10]))


Input shape
-----------

The `input_shape` parameter is the one causing beginners the most headaches.

-  it **must** be specified in the first layer
-  it **must not** be specified in any other layer
-  it contains the shape of the input, but without the first dimension
-  the first dimension of your input data **must** be the data points
-  if your data has only two dimensions, `input_shape` still must be written as a tuple, e.g. ``(2, )``
-  if your data has only one dimension, you may have to reshape your data to ``(n, 1)`` with NumPy.


Output shape
------------

The shape of the `predicted` output is determined by the number of neurons/units
and the activation function in the last layer of the network. The specific
configuration depends on the shape of the `true` (possibly one-hot-encoded) output:

- For `binary classification` there is `1` unit with a ``sigmoid`` activation.
- For `single output regression` there is `1` unit with a ``linear`` activation.
- For `multiclass classification` with `K` classes there are `K` units with a ``softmax`` activation.
- For `multilabel classification` with `K` classes there are `K` units with a ``sigmoid`` activation.

For multiclass/ multilabel classification the `true` output
must be one-hot encoded before fitting. The function ``tensorflow.keras.utils.to_categorical``
does that for you.



Mini-Batches and Epochs
-----------------------

An efficient way to train a neural network is to feed small subsets of the training data.
It is a variant of *stochastic gradient descent*. These subsets are called *mini-batches*.

Mini-batches are used, because using one data point at a time would take too long,
but the gradients for all data points might consume too much memory.
So choosing the batch size is a sort of balancing act.

When the backpropagation algorithm has processed every data point once, one a
training **epoch** is finished. Training a neural nework usually requires multiple epochs.

Mini-batch size and number of epochs are two important hyperparameters in Keras.

.. hint::

   You would usually want to set the number of epochs *as low as possible*, but the mini-batch-size *as high as possible*.



Reset the model
---------------

When you build several models in the same session,
it is worth clearing the session in between:

.. code-block:: python3

   from tensorflow.keras import backend as K

   K.clear_session()


Inspect the model architecture
------------------------------

To view all layers and the number of parameters, write:

.. code-block:: python

   model.summary()

It results in a table like:

============================ ============== =====================
Layer (type)                 Output Shape              Param #
============================ ============== =====================
dense_1 (Dense)              (None, 100)               78500
batch_normalization_1 (Batch (None, 100)               400
activation_1 (Activation)    (None, 100)               0
============================ ============== =====================

.. warning::

   If you see that your model has millions of parameters, training will take very long.
   To see your model take off, start with a smaller size.

Fit multiple times
------------------

When you call `.fit()` a second time, the training **will not start from scratch**. 
TensorFlow resumes the training from the point where it last left off.

This has the advantage that you can approach the training in small portions, depending on how it goes.
If this is not what you want, reset the model in between runs.


Check the history
-----------------

The ``fit()`` function returns a **History object**. 
You can access the loss and accuracy (most of the time for plotting).

.. code:: python3

   h = fit(...)
   acc = h.history['acc']  # or loss, val_loss, val_acc

   plt.plot(range(acc.shape[0]), acc)



Writing a trained model
-----------------------

First install the H5PY libtrary to save models in the ``h5`` format:

.. code-block:: bash

   pip install h5py

Save the model's architecture, weights and training configuration in a single
file such that training or prediction can be resumed at a later time:

.. code-block:: python

   # serialize model
   network.save("model.h5")
   print("Saved model to disk")

To use the trained model somewhere else in a project it can be loaded from file:

.. code-block:: python

   from tensorflow.keras.models import load_model

   # load, create and compile model

   network = load_model("model.h5")
   network.summary()



.. container:: banner debug

   Debugging Checklist

.. highlights::

   -  inspect the shapes of your X/y data
   -  one-hot-encode y (in multiclass classification)
   -  print the model summary
   -  add accuracy to the metrics
   -  set a validation dataset
   -  draw learning curve
   -  vary the number of layers/neurons
   -  try a few learning strategies
   -  save checkpoints during training
   -  plot a histogram of model weights before/after training


.. container:: banner reading

   Further Reading

.. highlights::

   - `TensorFlow Homepage <https://www.tensorflow.org>`__
   - `Checklist for debugging neural networks <https://towardsdatascience.com/checklist-for-debugging-neural-networks-d8b2a9434f21>`__
   - `Deep Learning Resources by Sebastian Raschka <https://sebastianraschka.com/deep-learning-resources.html>`__
