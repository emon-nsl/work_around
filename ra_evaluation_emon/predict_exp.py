import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.optimizers import SGD, Adam
# from tensorflow.keras.optimizers import Adam

#convert input
def cvrt2embd(no):
    l = np.zeros(11)
    l[no] = 1
    return np.array(l)


x_train = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_train = np.array([5*i**2 + 7*i + 9 for i in x_train])
input_emb = np.array([cvrt2embd(i) for i in x_train])

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(40, input_shape=(None,11), activation='relu'),
    tf.keras.layers.Dense(20, activation='relu'),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(1)
])

model.compile(loss='mean_squared_error', optimizer = Adam())
model.summary()

model.fit(input_emb, y_train, epochs=1000, batch_size=11)

for i in x_train:
    out = round(model.predict(np.array([cvrt2embd(i)]))[0][0])
    print('If we input to our model {} it outputs {}'.format(i, out))