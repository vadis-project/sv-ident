from ranx import evaluate
import os
import json
from typing import Dict, Tuple, List
from argparse import ArgumentParser


DEFAULT_METRICS = ["map@10", "map@20", "map@30", "r-precision"]


def _evaluate(
    qrels: Dict[str, Dict[str, int]], 
    results: Dict[str, Dict[str, float]], 
    measures: List[str]
    ) -> Tuple[Dict[str, float], Dict[str, float], Dict[str, float], Dict[str, float]]:
        
        scores = evaluate(qrels, results, measures)

        return scores


def main(qrels_path: str, run_path: str, metrics: List[str]):
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

    scores = _evaluate(qrels, run, metrics)
    formatted_scores = {k.replace("_","@"): v for k,v in scores.items()}
    print(formatted_scores)
    return scores


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-q", "--qrels", type=str, required=True)
    parser.add_argument("-r", "--run", type=str, required=True)
    parser.add_argument("-m", "--metrics", default=DEFAULT_METRICS, type=str, nargs='+', required=False)
    args = parser.parse_args()
    
    main(qrels_path=args.qrels, run_path=args.run, metrics=args.metrics)
