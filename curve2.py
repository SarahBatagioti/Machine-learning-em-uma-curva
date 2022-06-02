import numpy as np
import tensorflow as tf

listex = np.linspace(-40,40,20)
listey = np.array([0.3*i + np.random.normal(0, 1, 1) for i in listex])

model = tf.keras.Sequential([tf.keras.layers.Dense(1)])
model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))
model.fit(listex,listey, epochs=100, verbose=False)

print(model)