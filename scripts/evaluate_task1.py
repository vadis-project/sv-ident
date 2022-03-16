from sklearn.metrics import precision_score, recall_score, f1_score
from argparse import ArgumentParser
import os
import json
from typing import List


METRICS = {"f1": f1_score, "p": precision_score, "r": recall_score}
DEFAULT_METRICS = ["f1@macro", "p@macro", "r@macro"]


def evaluate(pred_path: str, true_path: str, metrics_str: List[str]):
    """
        pred_path and true_path should have the following format:
            {
                'DOC_ID': 'LABEL/SCORE',
                ...
            }
    """

    assert os.path.exists(pred_path)
    assert os.path.exists(true_path)

    with open(pred_path, "r") as f:
        pred_json = json.load(f)

    with open(true_path, "r") as f:
        true_json = json.load(f)

    pred_keys = sorted(list(pred_json.keys()))
    true_keys = sorted(list(true_json.keys()))

    assert pred_keys == true_keys

    pred = [pred_json[k] for k in pred_keys]
    true = [true_json[k] for k in true_keys]

    metrics = {}
    for m in metrics_str:
        parts = m.split("@")
        if len(parts) == 2:
            name = ""
            avg = None

            try:
                name, avg = parts[0].lower(), parts[1]
            except:
                print(f"Invalid format for metric: {m}")

            if name in METRICS:
                score = METRICS[name](y_pred=pred, y_true=true, average=avg, zero_division=False)
                metrics[name] = score

        elif len(parts) == 1:
            name = m.lower()

            if name in METRICS:
                score = METRICS[name](y_pred=pred, y_true=true, average=avg, zero_division=False)
                metrics[name] = score
    
    print(metrics)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-p", "--pred", type=str, required=True)
    parser.add_argument("-t", "--true", type=str, required=True)
    parser.add_argument("-m", "--metrics", default=DEFAULT_METRICS, type=str, nargs='+', required=False)
    args = parser.parse_args()
    
    evaluate(pred_path=args.pred, true_path=args.true, metrics_str=args.metrics)
