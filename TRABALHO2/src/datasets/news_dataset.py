
from typing import Tuple, Any, Dict
from .dataset_interface import DatasetInterface


class NewsDataset(DatasetInterface):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.path = path
        self.text_classes = []
        with open(path, "r") as file:
            for line in file:
                line = line.split(" ")
                self.text_classes.append(line)

    def size(self) -> int:
        return len(self.text_classes)

    def get(self, idx: int) -> Tuple[Any, str]:
        self.superlista=[]
        for i in range(len(self.text_classes)):

        # fazer aquela parada de escrever todas as palavras nessa superlista, somente caso essa palavra nao esteja
        # previamente nessa lista, remover todas as palavras da stopwords e contar a frenquencia delas
        # to do: de forma parecida com o dataset de imagens, temos que retornar uma lista que contem
        # diversas tuplas que contem o texto do arquivo de forma vetorizada(n sei como vetorizar, é mais dificil
        # do que a de imagens, e mais chata de acordo com o antonio), e também sua classe, por exp.:
        # (texto vetorizado, classe) 
        
        # ler a i-esima noticia do disco e retornar o texto como uma string e
        # a classe
            return 0, ""
