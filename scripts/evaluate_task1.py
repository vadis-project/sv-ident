from sklearn.metrics import precision_score, recall_score, f1_score
from argparse import ArgumentParser
import os
import json
from typing import List
from collections import defaultdict


METRICS = {"f1": f1_score, "p": precision_score, "r": recall_score}
DEFAULT_METRICS = ["f1@macro", "p@macro", "r@macro"]


def main(true_path: str, pred_path: str, metrics_str: List[str], langs_file: str, docs_file: str):
    """true_path and pred_path should have the following format:
            {
                'DOC_ID': 'LABEL/SCORE',
                ...
            }
    """

    assert os.path.exists(true_path)
    assert os.path.exists(pred_path)
    assert os.path.exists(langs_file)
    assert os.path.exists(docs_file)

    with open(true_path, "r") as f:
        true_json = json.load(f)
    
    with open(pred_path, "r") as f:
        pred_json = json.load(f)

    with open(langs_file, "r") as f:
        uuid_langs = json.load(f)

    with open(docs_file, "r") as f:
        uuid_docs = json.load(f)

    used_uuids = []
    lang_doc_scores = {"en": {}, "de": {}}

    for lang in ["en", "de"]:
        docs = list(set([uuid_docs[k] for k,_ in true_json.items()]))

        docs_scores = {}
        for doc in docs:
            true_keys = sorted([k for k,_ in true_json.items() if uuid_langs[k] == lang and uuid_docs[k] == doc])
            pred_keys = sorted([k for k,_ in pred_json.items() if uuid_langs[k] == lang and uuid_docs[k] == doc])

            assert true_keys == pred_keys

            true = [true_json[k] for k in true_keys]
            pred = [pred_json[k] for k in pred_keys]

            if len(true) > 0 and len(pred) > 0:
                for k in true_keys:
                    assert k not in used_uuids
                    used_uuids.append(k)

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
                docs_scores[doc] = metrics
                lang_doc_scores[lang] = docs_scores
    
    avg_lang_scores = {}
    avg_scores = defaultdict(list)

    for lang,doc_scores in lang_doc_scores.items():
        scores = defaultdict(list)
        for d,ds in doc_scores.items():
            for sn,s in ds.items():
                scores[sn].append(s)
        
        scores = {k:sum(v)/len(v) for k,v in scores.items()}

        avg_lang_scores[lang] = scores
        
        for sn,s in scores.items():
            avg_scores[sn].append(s)

    avg_scores = {k:sum(v)/len(v) for k,v in avg_scores.items()}
    
    result = {"macro_scores": avg_scores, "macro_language_scores": avg_lang_scores, "document_scores": lang_doc_scores}
    print(result)
    return result


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-p", "--pred", type=str, required=True)
    parser.add_argument("-t", "--true", type=str, required=True)
    parser.add_argument("-m", "--metrics", default=DEFAULT_METRICS, type=str, nargs='+', required=False)
    parser.add_argument("-l", "--langs-file", type=str, required=True)
    parser.add_argument("-d", "--docs-file", type=str, required=True)
    args = parser.parse_args()
    
    main(pred_path=args.pred, true_path=args.true, metrics_str=args.metrics, langs_file=args.langs_file, docs_file=args.docs_file)
