
from typing import Tuple, Any, Dict
from .dataset_interface import DatasetInterface
import csv

# recebido dependendo do tipo de teste sendo efetuado

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

    def get(self, idx: int) -> Tuple[Any, str]: #vetorizar imagem e dps vc se vira boco
        return cv2.imread(self.image_classes[idx][0]), self.image_classes[idx][1]
        # ler a i-esima imagem do disco usando a biblioteca cv2 e retornar
        # a imagem e a respectiva classe

        #ler o path, se tiver por exp text.txt, remover o text.txt do path
        #dps tem q adicionar o nome da imagem, sem a classe, ao path
        #(fazer isso com dois indices, um para o indice da lista dentro dos vetores e
        # depois outro indice pra escolher o primeiro espaço dessa lista (nome do arquivo))

        #data/datasets/img_small/test.txt
        #data/datasets/img_small/test/000.png