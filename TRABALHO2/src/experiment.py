
from typing import Union, Dict, List
from src.datasets.dataset_interface import DatasetInterface
from src.classifiers.classifier_interface import ClassifierInterface
from src.metrics import accuracy
import time

class Experiment:
    def __init__(self,
                 train_dataset: DatasetInterface,
                 test_dataset: DatasetInterface):
        self.train_dataset = train_dataset
        self.test_dataset = test_dataset
        self.true_classes = self._get_true_classes_from_dataset(
            self.test_dataset)

    def run(self, classifier: ClassifierInterface) -> Dict[str, float]:
        """ executa o experimento """
        classifier.train(self.train_dataset)
        pred_classes = classifier.predict(self.test_dataset)

        Inicio_Cronometro = time.time()
        classifier.train(self.train_dataset)
        Fim_Cronometro = time.time()
        pred_classes = classifier.predict(self.test_dataset)

        Tempo_Inferencia = time.time() - Fim_Cronometro
        Tempo_Treino = Fim_Cronometro - Inicio_Cronometro


        metrics = {
            "accuracy": accuracy(self.true_classes, pred_classes),
            "training time per sample": Tempo_Treino / self.train_dataset.size,
            "inference time per sample": Tempo_Inferencia / self.test_dataset.size
        }

        return metrics


    def _get_true_classes_from_dataset(self, dataset: DatasetInterface) -> List[str]:
        true_classes = []
        for idx in range(dataset.size()):
            _, sample_class = dataset.get(idx)
            true_classes.append(sample_class)
        return true_classes
