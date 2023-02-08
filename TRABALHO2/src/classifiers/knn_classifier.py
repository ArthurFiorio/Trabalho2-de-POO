from typing import Dict, List
from .classifier_interface import ClassifierInterface
from src.datasets.dataset_interface import DatasetInterface


class KnnClassifier(ClassifierInterface):
    def __init__(self) -> None:
        super().__init__()
        self.DadosTreino = []
        self.AmostrasTeste = []
        self.ContadorAmostras = 0
        self.QuantidadeTestes = 0

    def train(self, train_dataset: DatasetInterface) -> None:
        # salvar as amostras do dataset de treino
        self.ContadorAmostras = train_dataset.size()
        for i in range(self.ContadorAmostras):
            self.DadosTreino.append(train_dataset.get(i))

    def predict(self, test_dataset: DatasetInterface) -> List[str]:
        """ para cada amostra no dataset, buscar os k vizinhos mais proximos e 
        retornar a classe mais frequente entre eles """
        
        K = 5
        distancia = []
        classes = []
        
        #guardando as amostras do test em uma lista
        self.QuantidadeTestes = test_dataset.size()
        for i in range(self.QuantidadeTestes):
            self.AmostrasTeste.append(test_dataset.get(i))

        #calcula a distancia de todos os vetores
        for i in range(self.QuantidadeTestes):
            for j in range(self.ContadorAmostras):
                somatorio = 0
                for x in range(len(self.AmostrasTeste[i][0])):
                    somatorio += (self.DadosTreino[j][0][x] - self.AmostrasTeste[i][0][x]) ** 2
                dist = (somatorio)**(1/2)
                distancia.append((dist, self.DadosTreino[j][1]))
        
        #ve os 5 pontos com menor distancia de cada teste e salva seus index em uma lista de listas
        # explicação abaixo*
        closest_k = []
        for i in range(self.QuantidadeTestes):
            distances_for_sample = [(idx, d) for idx, d in enumerate(distancia) if idx // self.ContadorAmostras == i]
            distances_for_sample.sort(key=lambda x: x[1])
            closest_k.append([x[0] for x in distances_for_sample[:K]])

        classifier = []
        for indices in closest_k:
            class_count = {}
            for idx in indices:
                class_ = distancia[idx][1]
                if class_ not in class_count:
                    class_count[class_] = 0
                class_count[class_] += 1
            classifier.append(max(class_count, key=class_count.get))

        return classifier