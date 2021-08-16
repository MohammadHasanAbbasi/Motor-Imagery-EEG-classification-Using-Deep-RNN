import tensorflow as tf
from tensorflow import keras
from keras.layers import Bidirectional
def get_model(shape):
    model = keras.models.Sequential([
    keras.layers.LSTM(14, return_sequences=True,input_shape = shape),
    keras.layers.BatchNormalization(),
    keras.layers.LeakyReLU(alpha=0.05),
#     keras.layers.Dropout(0.2),
    Bidirectional(keras.layers.LSTM(7 , activation = 'sigmoid', return_sequences=True)),
    keras.layers.BatchNormalization(),
    keras.layers.LeakyReLU(alpha=0.05),
    keras.layers.Dropout(0.1),
    keras.layers.LSTM(7),
    keras.layers.Dense(4,activation='softmax')
    ])
    model.summary()
    model.compile(loss='categorical_crossentropy',metrics=['accuracy'])
    
    return model