import imutils
import cv2

class AspectAwarePreprocessor_WithPadding:
  def __init__(self, width, height, inter=cv2.INTER_AREA):
    self.width = width
    self.height = height
    self.inter = inter

  def preprocess(self, image):
    (h, w) = image.shape[:2]
    if w > h:
      image = imutils.resize(image, width=self.width, inter=self.inter)
    else:
      image = imutils.resize(image, height=self.height, inter=self.inter)
    padW = int((self.width - image.shape[1]) / 2.0)
    padH = int((self.height - image.shape[0]) / 2.0)
    image = cv2.copyMakeBorder(image, padH, padH, padW, padW, cv2.BORDER_REPLICATE)
    image = cv2.resize(image, (self.width, self.height), interpolation=self.inter)
    return image