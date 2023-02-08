
from typing import Tuple, Any, Dict
from .dataset_interface import DatasetInterface
import cv2

class ImageDataset(DatasetInterface):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.image_classes = []
        self.path = path
        with open(path, "r") as file:
            for line in file:
                line = line.split(" ")
                self.image_classes.append(line)

    def size(self) -> int:
        return len(self.image_classes)

    def get(self, idx: int) -> Tuple[Any, str]:
        for i in range (len(self.image_classes)):
            if 'test.txt' in self.path:
                self.path= self.path.replace('test.txt', self.image_classes[i][0])
            else:
                self.path= self.path.replace('train.txt', self.image_classes[i][0])

            images_classes = []
        for line in self.image_classes:
            image, class_ = line
            images_classes.append((cv2.imread(image), class_))
        return images_classes