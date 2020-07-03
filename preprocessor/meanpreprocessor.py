import numpy as np
import cv2

class MeanPreprocessor:
  def __init__(self, rMean, gMean, bMean):
    self.rMean = rMean
    self.gMean = gMean
    self.bMean = bMean

  def preprocess(self, image):
    (b, g ,r) = cv2.split(image.astype('float32'))
    b -= bMean
    g -= gMean
    r -= rMean
    image = cv2.merge([b,g,r])
    return image
