# -*- coding: utf-8 -*-
"""Class-8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iqT0tiEKU_9zRo8CVQ_X-IEpkKBCzJ_y
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;
from sklearn.model_selection import train_test_split;
from sklearn.linear_model import LinearRegression;
# Encontrar el error de prediccion
from sklearn.metrics import mean_squared_error;
# %matplotlib inline

df = pd.read_csv("/content/FIFA_data.csv", index_col=0);
df.head(1)

df.shape

# ISNULL() MUESTRA SI HAY DATOS NULOS
print(df['Age'].isnull().any(), df['Potential'].isnull().any());

# SCATTER nos muestra una grafica
plt.scatter(df['Age'], df['Potential']);

#
plt.scatter(data=df, x='Age', y='Potential');
plt.xlabel('Age');
plt.ylabel('Potential');

plt.hist2d(data=df, x='Age', y='Potential');

plt.hist2d(data = df, x='Age', y='Potential');
plt.xlabel('Age');
plt.ylabel('Potential');
plt.colorbar();

x_train, x_test, y_train, y_test = train_test_split(df['Age'], df['Potential'], test_size=0.2);
x_train.shape, x_test.shape, y_train.shape, y_test.shape ;

x_train = np.array(x_train).reshape(-1, 1);
x_test = np.array(x_test).reshape(-1, 1);

y_train = np.array(y_train).reshape(-1, 1);
y_test = np.array(y_test).reshape(-1, 1);

regression = LinearRegression();

# entrenamiento
regression.fit(x_train, y_train);

# prediccion
y_predict = regression.predict(x_test);

# Encontrar el margen de error
mean_squared_error(y_predict, y_test);

from sklearn.ensemble import RandomForestRegressor;

regression = RandomForestRegressor();
regression.fit(x_train, y_train);
y_predict = regression.predict(x_test);
mean_squared_error(y_predict, y_test);

from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Selecciona características
features = ['Age', 'Overall', 'Special', 'International Reputation', 'Weak Foot', 'Skill Moves', 'Jersey Number',
            'Penalties', 'Composure', 'Marking', 'StandingTackle', 'SlidingTackle', 'GKDiving', 'GKHandling',
            'GKKicking', 'GKPositioning', 'GKReflexes']

# Divide los datos en características (X) y variable objetivo (y)
X = df[features]
y = df['Potential']

# Divide los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Convert to ndarray
x_train = np.array(X_train)
y_train = np.array(y_train)
x_test = np.array(X_test)
# Reshape
x_train = x_train.reshape(-1, 1)
y_train = y_train.reshape(-1, 1)
x_test = x_test.reshape(-1, 1)
print(x_train.shape)

# Imputa los valores faltantes con la media de cada columna
imputer = SimpleImputer(strategy='mean')
X_train_imputed = imputer.fit_transform(X_train)
X_test_imputed = imputer.transform(X_test)

# Entrena el modelo RandomForestRegressor con los datos imputados
rf_regressor = RandomForestRegressor()
rf_regressor.fit(X_train_imputed, y_train)

# Predicción
y_predict_rf_imputed = rf_regressor.predict(X_test_imputed)

# Evaluación del modelo
mse_rf_imputed = mean_squared_error(y_test, y_predict_rf_imputed)
r2_rf_imputed = rf_regressor.score(X_test_imputed, y_test)
print("Random Forest Mean Squared Error (with imputation):", mse_rf_imputed)
print("Random Forest R^2 Score (with imputation):", r2_rf_imputed)