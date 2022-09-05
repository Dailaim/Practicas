from pickletools import optimize
from tabnanny import verbose
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([3, 14, 32, 46, 59, 72, 100], dtype=float)


capa = tf.keras.layers.Dense(units=1, input_shape=[1])
modelo = tf.keras.Sequential([capa])


modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

print("Estado: Entrendado.....")
historial = modelo.fit(celsius, fahrenheit, epochs=1000, verbose=False)

print("Estado: Modelo entrenado")

plt.xlabel("# Epoca"),
plt.ylabel("Magnitud de pérdida"),
plt.plot(historial.history["loss"])

print("Hagamos una predicción!")
resultado = modelo.predict([100.0])
print("El resultado es " + str(resultado) + " fahrenheit!")

print("Variables internas del modelo")
print(capa.get_weights())
