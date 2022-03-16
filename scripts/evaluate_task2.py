import pytrec_eval
import os
import json
from typing import Dict, Tuple, List
from argparse import ArgumentParser


DEFAULT_METRICS = ["map@20,50", "p@1,3,5,10,20", "r@1,3,5,10,20", "rprec"]
PYTREC_METRIC_MAPPING = {"map": "map_cut", "rprec": "Rprec", "p": "P", "r": "recall"}


def _evaluate(
    qrels: Dict[str, Dict[str, int]], 
    results: Dict[str, Dict[str, float]], 
    measures: Dict[str, str]
    ) -> Tuple[Dict[str, float], Dict[str, float], Dict[str, float], Dict[str, float]]:
        
        evaluator = pytrec_eval.RelevanceEvaluator(qrels, [k for _,k in measures.items()])
        scores = evaluator.evaluate(results)

        metrics = {_k:0.0 for _k,__ in scores[list(scores.keys())[0]].items()}

        for _,query_scores in scores.items():
            for score_name,score in query_scores.items():
                metrics[score_name] += score

        for k,v in metrics.items():
            metrics[k] = round(v/len(scores),5)

        return metrics


def evaluate(qrels_path: str, run_path: str, metrics_str: List[str]):
    """
    qrels_path and run_path should have the following format:
        {
            'DOC_ID': {
                'VAR_ID': 'LABEL/SCORE'
                ...
            },
            ...
        }
    """
    
    assert os.path.exists(qrels_path)
    assert os.path.exists(run_path)

    with open(qrels_path, "r") as f:
        qrels = json.load(f)
    
    with open(run_path, "r") as f:
        run = json.load(f)

    metrics = {}
    for m in metrics_str:
        parts = m.split("@")
        if len(parts) == 2:
            name = ""
            ks = None

            try:
                name, ks = parts[0].lower(), parts[1]
            except:
                print(f"Invalid format for metric: {m}")

            if name in PYTREC_METRIC_MAPPING:
                _metric = PYTREC_METRIC_MAPPING[name]+"."+ks
                metrics[name] = _metric

        elif len(parts) == 1:
            name = m.lower()

            if name in PYTREC_METRIC_MAPPING:
                _metric = PYTREC_METRIC_MAPPING[name]
                metrics[name] = _metric

    scores = _evaluate(qrels, run, metrics)
    formatted_scores = {k.replace("_","@"): v for k,v in scores.items()}
    print(formatted_scores)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-q", "--qrels", type=str, required=True)
    parser.add_argument("-r", "--run", type=str, required=True)
    parser.add_argument("-m", "--metrics", default=DEFAULT_METRICS, type=str, nargs='+', required=False)
    args = parser.parse_args()
    
    evaluate(qrels_path=args.qrels, run_path=args.run, metrics_str=args.metrics)
