
from matplotlib.pyplot import imread
from keras.applications.resnet50 import ResNet50
from keras.applications.resnet50 import decode_predictions

m = ResNet50()
m.compile(optimizer='rmsprop', loss='categorical_crossentropy',
              metrics=['accuracy'])

a = imread('myimage.png')
p = m.predict(a)

print(decode_predictions(p))
