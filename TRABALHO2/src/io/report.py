
from typing import Dict

#todo função que abre o .txt, escreve os dados e fecha ele
def write_report(path, config: Dict, metrics_values) -> None:
    report= open(path, "w")
    report.write(f'dataset:{config["type"]}\n'
                 f'path:{config["path"]}\n'
                 f'classifier:{config["classifier"]}\n'
                 f'training time per sample:{metrics_values["train_sample"]}\n'
                 f'inference time per sample:{metrics_values["inference_sample"]}\n'
                 f'accuracy:{metrics_values["accuracy"]}')
