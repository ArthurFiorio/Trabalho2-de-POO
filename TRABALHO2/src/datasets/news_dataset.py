
from typing import Tuple, Any, Dict
from .dataset_interface import DatasetInterface
from stopwords import Stop_words

class NewsDataset(DatasetInterface):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.path = path
        self.text = []
        self.news_classes = []
        with open(path, "r") as file:
            for line in file:
                line = line.split(" ")
                self.text.append(line)
                self.news_classes.append(line[-4:-1])

    def size(self) -> int:
        return len(self.text)

    def get(self, idx: int) -> Tuple[Any, str]:
        self.superlista=[]

        for i in range(len(self.text)):
            if 'test.txt' in self.path:
                self.path= self.path.replace('test.txt', self.text[i][0])
            else:
                self.path= self.path.replace('train.txt', self.text[i][0])
            with open(self.path) as file:
                noticia = file.readline().split()
                if noticia[i] in self.superlista:
                    pass
                else:
                    self.superlista.append(noticia[i])
                
                for word in self.superlista:
                    if word in Stop_words.stop_words:
                        self.superlista.remove(word)
        return self.superlista, self.news_classes[idx]


#tirar stopwords do self.superlista e retornar uma lista gigante com todas as palabras com os indicies de repetição
        # fazer aquela parada de escrever todas as palavras nessa superlista, somente caso essa palavra nao esteja
        # previamente nessa lista, remover todas as palavras da stopwords e contar a frenquencia delas
        # to do: de forma parecida com o dataset de imagens, temos que retornar uma lista que contem
        # diversas tuplas que contem o texto do arquivo de forma vetorizada(n sei como vetorizar, é mais dificil
        # do que a de imagens, e mais chata de acordo com o antonio), e também sua classe, por exp.:
        # (texto vetorizado, classe) 
        
        # ler a i-esima noticia do disco e retornar o texto como uma string e
        # a classe
