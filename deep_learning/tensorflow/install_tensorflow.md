
Installing TensorFlow

During the next two course days, we will train neural network models with TensorFlow. The installation can be a bit tedious. In particular you need to take care to use Python 3.10-3.12. A setup that worked well for me is using the package manager `uv`. Try:

- create a project folder
- open a terminal in the project folder
- pip install uv
- uv init --python 3.12
- uv add tensorflow
- uv add pandas
- uv add seaborn
- uv add jupyter

To then start a notebook, tell VSCode to use the uv-managed environment from the project folder or start Jupyter with:

- uv run jupyter notebook


If you have a GPU, you may want to install a TensorFlow version with GPU support. We don't need it but it speeds up things a lot.

If the above approach does not work for you, please see the installation instructions on https://www.tensorflow.org/ .