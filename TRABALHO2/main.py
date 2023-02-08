
from src.datasets.dataset_factory import create_dataset
from src.classifiers.classifier_factory import create_classifier
from src.experiment import Experiment
from src.io.args import parse_args
from src.io.config import load_config
from src.io.report import write_report
import argparse


def main():
    # obter os nomes dos arquivos de configuracao e de saida da linha de comando
    parser = argparse.ArgumentParser()
    parser.add_argument("config_path", type= str)#arquivo de configuração
    parser.add_argument("report_path", type= str)#arquivo de saida da linha de comando
    args = parser.parse_args()

    # le o arquivo json e retorna como um dicionario
    config = load_config(args.config_path)

    #cria os datasets de acordo com o que foi passado no arquivo json
    train_dataset = create_dataset(config["train_path"], config["type"])
    test_dataset = create_dataset(config["test_path"], config["type"])
    classifier = create_classifier(config["classifier"])

    experiment = Experiment(train_dataset, test_dataset)
    metrics = experiment.run(classifier)

    report_path= 'TRABALHO2\report.txt'

    # escreve o arquivo de saida
    write_report(report_path, config, metrics)

    print("Success.")


if __name__ == "__main__":  
    main()