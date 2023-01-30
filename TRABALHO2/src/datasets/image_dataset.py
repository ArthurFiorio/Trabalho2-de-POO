
from typing import Tuple, Any, Dict
from .dataset_interface import DatasetInterface


class ImageDataset(DatasetInterface):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        # ler arquivo contendo os nomes das imagens e as classes e armazenar
        # em uma lista

    def size(self) -> int:
        # retornar tamanho do dataset (numero de linhas do arquivo)
        return 0

    def get(self, idx: int) -> Tuple[Any, str]:
        # ler a i-esima imagem do disco usando a biblioteca cv2 e retornar
        # a imagem e a respectiva classe
        return 0, ""
