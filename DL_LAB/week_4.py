from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

dataset = loadtxt("diabetes.csv")
X = dataset[:, :8]
y = dataset[:, 8]

model = Sequential(
    Dense(12, input_shape = (8,), activation='relu')
    Dense(8, activation='relu')
    Dense(1, activation ='sigmoid')
)

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X, y, epochs=150, batch_size=10)
# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))
