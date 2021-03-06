import tensorflow as tf
import datetime


mnist = tf.keras.datasets.fashion_mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0


model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
  ])


model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['sparse_categorical_accuracy'])


model.fit(x=x_train, 
          y=y_train, 
          epochs=5)

# Evaluate model 
test_loss, test_accuracy = model.evaluate(x_test, y_test ) #, steps = 10000)
print("Test accuracy: {}".format(test_accuracy))