# -*- coding: utf-8 -*-
"""Red Neuronal con TensorFlow.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yrwuqav-F0vZ4Vtsu0gs8SxW-WalQNgp
"""

# Red Neuronal con TensorFlow
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Definición del modelo
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train_imputed.shape[1],)),
    Dense(32, activation='relu'),
    Dense(1)
])

# Compilación del modelo
model.compile(optimizer='adam', loss='mean_squared_error')

# Entrenamiento del modelo
model.fit(X_train_imputed, y_train, epochs=50, batch_size=32, verbose=0)

# Evaluación del modelo
mse_nn_imputed = model.evaluate(X_test_imputed, y_test, verbose=0)
print("Neural Network Mean Squared Error (with imputation):", mse_nn_imputed)