from visit import *
from OperatorClip import OperatorClip
from OperatorSlice import OperatorSlice
from OperatorThreshold import OperatorThreshold


class OperatorSettings(object):
    """Add operator and its settings."""

    def __init__(self, File, OperSet, myList, Centroids, tags):
        self.File = File
        self.tags = tags
        self.myList = myList
        self.OperSet = OperSet
        self.Centroids = Centroids

    def Slice(self):
        OperatorSlice(self.File, self.OperSet, self.myList)

    def Clip(self):
        OperatorClip(self.File, self.OperSet, self.myList, self.Centroids)

    def Threshold(self):
        OperatorThreshold(self.OperSet, self.myList, self.tags)
