from keras.utils import np_utils
import numpy as np
import h5py


class HDF5DatasetGenerator:
  def __init__(self, dbpath, batchSize, preprocessors=None, aug=None):
    self.dbpath = dbpath
    self.batchSize = batchSize
    self.preprocessors = preprocessors

    self.db = h5py.File(self.dbpath)
    self.noImages = self.db['labels'].shape[0]

    def generator(self, passes=np.inf):
      ephochs = 0
      while epochs < passes:
        for i in np.arange(0, self.numImages, self.batchSize):
          images = self.db["images"][i: i + self.batchSize]
          labels = self.db["labels"][i: i + self.batchSize]
          if self.preprocessors is not None:
          procImages = []
          for image in images:
            for p in self.preprocessors:
              image = p.preprocess(image)
            procImages.append(image)
          images = np.array(procImages)
          if self.aug is not None:
            (images, labels) = next(self.aug.flow(images, labels, batch_size=self.batchSize))
          yield (images, labels)
        epochs += 1

    
    def close(self):
      self.db.close()

