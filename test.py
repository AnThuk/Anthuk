import keras

model = keras.models.load_model('wholemodel')

model.summary()
model.evaluate()