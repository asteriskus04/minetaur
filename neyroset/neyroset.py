import numpy as np
from tensorflow import keras
from tensorflow.keras.layers import Dense, Flatten, Dropout, Conv2D, MaxPooling2D


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return list(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


x_train = []
nameNumber = 0
f = open('test.txt', 'r')
while True:
    hex_split = f.readline()
    if not hex_split:
        break
    print(hex_split)
    res = np.zeros((30, 30, 3)).astype(int)
    s = 0
    k = 0
    for i in range(0, len(hex_split) - 6, 6):
        a = hex_split[i:i + 6]
        RGB = hex_to_rgb(a)
        r = RGB[0]
        g = RGB[1]
        b = RGB[2]
        res[k, s] = [r, g, b]
        s += 1
        if s == 30:
            k += 1
            s = 0
    x_train.append(res)
    x = np.expand_dims(res, axis=0)
f = open('test1.txt', 'r')
while True:
    hex_split = f.readline()
    if not hex_split:
        break
    print(hex_split)
    res = np.zeros((30, 30, 3)).astype(int)
    s = 0
    k = 0
    for i in range(0, len(hex_split) - 6, 6):
        a = hex_split[i:i + 6]
        RGB = hex_to_rgb(a)
        r = RGB[0]
        g = RGB[1]
        b = RGB[2]
        res[k, s] = [r, g, b]
        s += 1
        if s == 30:
            k += 1
            s = 0
    x_train.append(res)
    x = np.expand_dims(res, axis=0)
f = open('test2.txt', 'r')
while True:
    hex_split = f.readline()
    if not hex_split:
        break
    print(hex_split)
    res = np.zeros((30, 30, 3)).astype(int)
    s = 0
    k = 0
    for i in range(0, len(hex_split) - 6, 6):
        a = hex_split[i:i + 6]
        RGB = hex_to_rgb(a)
        r = RGB[0]
        g = RGB[1]
        b = RGB[2]
        res[k, s] = [r, g, b]
        s += 1
        if s == 30:
            k += 1
            s = 0
    x_train.append(res)
    x = np.expand_dims(res, axis=0)
x_train = np.array(x_train)
y_train = []

for i in range(0, 59):
    y_train.append(0)
for i in range(59, 115):
    y_train.append(1)
for i in range(115, x_train.shape[0]):
    y_train.append(0)
y_train = np.array(y_train)
print(x_train.shape)
print(y_train)

x_train = x_train / 255
y_train_cat = keras.utils.to_categorical(y_train, 2)
print(x_train.shape)
model = keras.Sequential([
    Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=(30, 30, 3)),
    MaxPooling2D((2, 2), strides=2),
    Conv2D(64, (3, 3), padding='same', activation='relu'),
    MaxPooling2D((2, 2), strides=2),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(2, activation='softmax')
])

# print(model.summary())      # вывод структуры НС в консоль

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

his = model.fit(x_train, y_train_cat, batch_size=32, epochs=5, validation_split=0.2)

x = x_train[80]
x = np.expand_dims(x, axis=0)

res = model.predict(x)
print(np.argmax(res))
