
from typing import Dict, List
from .classifier_interface import ClassifierInterface
from src.datasets.dataset_interface import DatasetInterface
from operator import add

class NearestCentroidClassifier(ClassifierInterface):
    def __init__(self) -> None:
        super().__init__()

    def train(self, train_dataset: DatasetInterface) -> None:
        """ calcular os centroides por classe """

        DadosTreino = []
        self.ContadorAmostras = train_dataset.size()

        for idx in range(self.ContadorAmostras):
            DadosTreino.append(train_dataset.get(idx))

        Classes = []
        SomaDasClasses = []
        ContadorDeClasses = []


        for idx in range(self.ContadorAmostras):
            Vetorizado = DadosTreino[0]
            Classe =  DadosTreino[1]
            if Classe not in Classes:
                Classes.append(Classe)
                SomaDasClasses.append(Vetorizado)
                ContadorDeClasses.append(1)
            else:
                SomaDasClasses[Classes.index(Classe)] =  list(map(add, SomaDasClasses[Classes.index(Classe)], Vetorizado))
                ContadorDeClasses[Classes.index(Classe)] += 1

        Centroides = []

        for i in range(len(Classes)):
            Centroides.append(([item / ContadorDeClasses[i] for item in SomaDasClasses[i]], Classe[i]))

        self.Centroides = Centroides
        self.SomaDasClasses = SomaDasClasses


    def predict(self, test_dataset: DatasetInterface) -> List[str]:
        """ para cada amostra no dataset, buscar o centroide mais proximo e respectiva retornar a classe """

        QuantidadeTestes = test_dataset.size
        QuantidadeCentroides = len(self.Centroides)

        AmostrasTeste= []
        
        for idx in range(len(QuantidadeTestes)):
            AmostrasTeste.append(test_dataset.get(idx))

        Distancias = []
        DistanciasTemporarias = []
        for idx in range(QuantidadeTestes):
            for r in range(QuantidadeCentroides):
                Soma = 0
                for k in range(len(AmostrasTeste[0][0])):
                    Soma += (AmostrasTeste[idx][0][k] - self.Centroides[r][0][k]) ** 2
                DistanciasTemporarias.append(Soma ** 0,5)
            Distancias.append(DistanciasTemporarias)
            DistanciasTemporarias = []

        ClassesPredictadas = []
        for i in range(QuantidadeTestes):
            MenorDistancia = min(Distancias[i])
            ClassesPredictadas.append(self.Centroides[Distancias[i].index(MenorDistancia)][1])
            
        return ClassesPredictadas
