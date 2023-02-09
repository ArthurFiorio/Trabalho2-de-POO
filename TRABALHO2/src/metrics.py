
from typing import List


def accuracy(true_classes: List[str], predicted_classes: List) -> float:
    match = 0
    Total = len(true_classes)
    for i in range(len(true_classes)):
        if true_classes[i]==predicted_classes[i]:
            match+=1
    acuracia = match/Total
    return acuracia
