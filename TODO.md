# TODO — Sphinx Review Findings

## Critical

### Deprecated Keras import paths
Multiple deep learning files use `from keras.layers import ...` (standalone Keras, no longer maintained).
Should use `from tensorflow.keras.layers import ...`.
- `deep_learning/recurrent_neural_networks/multi.py` lines 4–8
- `deep_learning/recurrent_neural_networks/rnn.py` lines 4–8
- `deep_learning/gan/gan.py` line 7 (`from keras.layers.advanced_activations import LeakyReLU` → `from tensorflow.keras.layers import LeakyReLU`)
