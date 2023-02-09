from typing import Tuple, Any, Dict
from .dataset_interface import DatasetInterface
import cv2

class ImageDataset(DatasetInterface):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        # ler arquivo contendo os nomes das imagens e as classes e armazenar
        # em uma lista
        self.path = path
        self.Path_Imagem = []
        self.Classe_Imagem = []
        with open(path) as file:
            for line in file:
                self.Path_Imagem.append(line[:-3])
                self.Classe_Imagem.append(line[-2:-1])

    def size(self) -> int:
        self.tamanho = len(self.Path_Imagem)
        return self.tamanho

    def get(self, idx: int) -> Tuple[Any, str]:
        Novo_Path = self.path[:self.path.rfind("/") + 1] + self.Path_Imagem[idx]
        image = cv2.imread(Novo_Path, 0)
        
        Imagem_achatada = []
        for i in range(len(image)):
            for j in range(len(image[0])):
                Imagem_achatada.append(int(image[i][j]))
        
        return Imagem_achatada, self.Classe_Imagem[idx]