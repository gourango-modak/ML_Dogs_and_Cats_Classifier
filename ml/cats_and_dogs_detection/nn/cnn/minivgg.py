from keras.layers import Dense, Conv2D, MaxPool2D, BatchNormalization, Dropout, Flatten
from keras.models import Sequential

class MiniVGG:
  @staticmethod
  def build(width, height, depth, clasess):
    model = Sequential()
    inputShape = (width, height, depth)
    model.add(Conv2D(32,(3,3), activation='relu', padding="Same", input_shape=inputShape))
    model.add(BatchNormalization())
    model.add(Conv2D(32, (3,3), activation='relu', padding='same'))
    model.add(BatchNormalization())
    model.add(MaxPool2D((2,2)))

    model.add(Dropout(0.25))

    model.add(Conv2D(64,(3,3), activation='relu', padding="Same"))
    model.add(BatchNormalization())
    model.add(Conv2D(64,(3,3), activation='relu', padding="Same"))
    model.add(BatchNormalization())
    model.add(MaxPool2D((2,2)))

    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(BatchNormalization())

    model.add(Dropout(0.5))

    model.add(Dense(clasess, activation='softmax'))

    return model