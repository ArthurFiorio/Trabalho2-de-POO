
from typing import Tuple, Any, Dict
from .dataset_interface import DatasetInterface
from .stopwords import Stop_words

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
        self.contagem_palavra = {}

        for i in range(len(self.text)):
            if 'test.txt' in self.path:
                self.path= self.path.replace('test.txt', self.text[i][0])
            else:
                self.path= self.path.replace('train.txt', self.text[i][0])
            with open(self.path) as file:
                noticia = file.readline().split()
                for word in noticia:
                    if word not in Stop_words.stop_words:
                        if word in self.superlista:
                            if word in self.contagem_palavra:
                                self.contagem_palavra[word] += 1
                            else:
                                self.contagem_palavra[word] = 1
                        else:
                            self.superlista.append(word)
    
        return self.contagem_palavra, self.news_classes[idx]
