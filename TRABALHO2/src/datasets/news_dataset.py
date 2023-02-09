
from typing import Tuple, Any, Dict
from .dataset_interface import DatasetInterface
from .stopwords import Stop_words

class NewsDataset(DatasetInterface):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.path = path
        self.text = []
        self.new_path = []
        self.news_classes = [] 
        self.path_definitivo = []
        with open(path, "r") as file:
            for line in file:
                line = line.split(" ")
                self.text.append(line)
                self.news_classes.append(line[1])
        if "train" in self.path:
            self.superlista=[]
            self.nova_superlista = []
            self.repeticao_palavra = {}
            

            for i in range(len(self.text)):
                if 'test.txt' in self.path:
                    self.new_path= self.path.replace('test.txt', self.text[i][0])
                else:
                    self.new_path= self.path.replace('train.txt', self.text[i][0])
                with open(self.new_path) as file:
                    noticia = file.readline().split()
                    for word in noticia:
                        if word not in Stop_words.stop_words:
                            if word in self.superlista:
                                if word in self.repeticao_palavra:
                                    self.repeticao_palavra[word] += 1
                                else:
                                    self.repeticao_palavra[word] = 1
                            else:
                                self.superlista.append(word)
            arquivo = open("superlista.txt", "w")
            for word in self.superlista:
                arquivo.write(f'{word} ')
            arquivo.close()

        with open("superlista.txt", "r") as file:
                self.nova_superlista = file.read().split()
    def size(self) -> int:
        return len(self.text)

    def get(self, idx: int) -> Tuple[Any, str]:
        frequencia = []
        palavras = []
        for i in range(len(self.text)):
            if 'test.txt' in self.path:
                self.path_definitivo= self.path.replace('test.txt', self.text[i][0])
            else:
                self.path_definitivo= self.path.replace('train.txt', self.text[i][0])

        for i in range(len(self.nova_superlista)):
            frequencia.append(0)
        with open(self.path_definitivo) as file:
            palavras = file.read().split()
        
        for word in palavras:
            if word in self.nova_superlista:
                i = self.nova_superlista.index(word)
                frequencia[i]+=1
                
        return frequencia, self.news_classes[idx]
