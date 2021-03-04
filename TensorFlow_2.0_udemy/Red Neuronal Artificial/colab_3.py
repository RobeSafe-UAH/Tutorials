import numpy as np
import datetime
import tensorflow as tf
from tensorflow.keras.datasets import fashion_mnist

#Cargar el dataset Fashion Mnist 
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

X_train = X_train / 255.0
X_train.shape
X_test =  X_test / 255.0

#Como cada imagen tiene 28x28 píxeles, 
# usamos la función reshape en todo el dataset de entrenamiento para convertirlo 
# en vectores de tamaño [-1 (todos los elementos), anchura * altura]
X_train = X_train.reshape(-1, 28*28)
X_test = X_test.reshape(-1, 28*28)

#Redimensionamos el conjunto de testing del mismo modo
X_test = X_test.reshape(-1, 28*28)
X_test.shape

dropout = 0.25
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(units=512, activation='relu', input_shape=(784, )))
model.add(tf.keras.layers.Dropout(dropout))
model.add(tf.keras.layers.Dense(units=512, activation='relu'))
model.add(tf.keras.layers.Dropout(dropout))
model.add(tf.keras.layers.Dense(units=128, activation='relu'))
model.add(tf.keras.layers.Dropout(dropout))
model.add(tf.keras.layers.Dense(units=128, activation='relu'))
model.add(tf.keras.layers.Dropout(dropout))


model.add(tf.keras.layers.Dense(units=10, activation='softmax'))

                   

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', 
                metrics=['sparse_categorical_accuracy'])
model.summary()


# Train model
model.fit(X_train, y_train, epochs = 100, batch_size=256)


# Evaluate model 
test_loss, test_accuracy = model.evaluate(X_test, y_test ) #, steps = 10000)
print("Test accuracy: {}".format(test_accuracy))

# Save model
model_json = model.to_json()
with open("fashion_model.json", "w") as json_file:
    json_file.write(model_json)

model.save_weights("fashion_model.h5")