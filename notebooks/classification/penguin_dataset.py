
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


def preprocess_penguins():
    # get the data
    df = pd.read_csv('../data/penguins_simple.csv', sep=';')

    # train-validation-test split
    train_val, test = train_test_split(df, test_size=0.2, random_state=42)    # <-- now reproducibility pays off
    train, val = train_test_split(train_val, test_size=0.2, random_state=43)

    # define X and y
    COLUMNS = ['Culmen Length (mm)', 'Culmen Depth (mm)',
            'Flipper Length (mm)', 'Body Mass (g)', 'Sex']

    Xtrain = train[COLUMNS]
    Xval = val[COLUMNS]
    Xtest = test[COLUMNS]

    ytrain = train['Species']
    yval = val['Species']
    ytest = test['Species']

    # feature engineering
    ohc = ColumnTransformer([
        ('one-hot', OneHotEncoder(drop='first', handle_unknown='error', sparse=False), ['Sex']),
        ('do nothing', 'passthrough', COLUMNS[:-1])
    ])
    ohc.fit(Xtrain)

    Xtrain_trans = ohc.transform(Xtrain)
    Xval_trans = ohc.transform(Xval)
    Xtest_trans = ohc.transform(Xtest)

    assert Xtrain_trans.shape[0] == ytrain.shape[0]
    assert Xval_trans.shape[0] == yval.shape[0]
    assert Xtest_trans.shape[0] == ytest.shape[0]
    assert Xtrain_trans.shape[1] == Xval_trans.shape[1] == Xtest_trans.shape[1]

    return Xtrain_trans, ytrain, Xval_trans, yval, Xtest_trans, ytest