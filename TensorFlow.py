import tensorflow as tf

import numpy as np



# Distance (in 100 km units) -> Fuel used (liters)

X = np.array([1, 2, 3, 4, 5], dtype=float)

Y = np.array([8, 15, 24, 31, 40], dtype=float)



# Simple linear model

model = tf.keras.Sequential([tf.keras.layers.Dense(1, input_shape=[1])])

model.compile(optimizer='sgd', loss='mean_squared_error')



# Train the mode
l
model.fit(X, Y, epochs=300, verbose=0)



# Predict fuel for 6×100 km

distance = 6
fuel_pred = model.predict([distance])[0][0]

print(f"Predicted fuel for {distance*100} km: {fuel_pred:.2f} liters")