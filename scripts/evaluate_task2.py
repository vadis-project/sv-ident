from audioop import avg
from ranx import evaluate
import os
import json
from typing import Dict, Tuple, List
from argparse import ArgumentParser
from collections import defaultdict


DEFAULT_METRICS = ["map@10", "map@20", "map@30", "r-precision"]


def get_ranx_scores(
    qrels: Dict[str, Dict[str, int]], 
    results: Dict[str, Dict[str, float]], 
    measures: List[str]
    ) -> Tuple[Dict[str, float], Dict[str, float], Dict[str, float], Dict[str, float]]:
        
        scores = evaluate(qrels, results, measures)

        if isinstance(scores, float) and len(measures) == 1:
            scores = {measures[0]: scores}

        return scores


def main(qrels_path: str, run_path: str, metrics: List[str], langs_file: str, docs_file: str):
    """qrels_path and run_path should have the following format:
        {
            'DOC_ID': {
                'VAR_ID': 'LABEL/SCORE'
                ...
            },
            ...
        }
    """

    metrics = [str(metrics)] if isinstance(metrics, str) else metrics
    
    assert os.path.exists(qrels_path)
    assert os.path.exists(run_path)
    assert os.path.exists(langs_file)
    assert os.path.exists(docs_file)

    with open(qrels_path, "r") as f:
        qrels = json.load(f)
    
    with open(run_path, "r") as f:
        run = json.load(f)

    with open(langs_file, "r") as f:
        uuid_langs = json.load(f)

    with open(docs_file, "r") as f:
        uuid_docs = json.load(f)

    used_uuids = []
    lang_doc_scores = {"en": {}, "de": {}}
    for lang in ["en", "de"]:
        docs = list(set([uuid_docs[k] for k,_ in qrels.items()]))

        docs_scores = {}
        for doc in docs:

            qrels_lang = {k:v for k,v in qrels.items() if uuid_langs[k] == lang and uuid_docs[k] == doc}
            run_lang = {k:v for k,v in run.items() if uuid_langs[k] == lang and uuid_docs[k] == doc}

            if len(qrels_lang) > 0 and len(run_lang) > 0:
                assert len(qrels_lang) == len(run_lang)
                for k in qrels_lang:  # make sure the score for each uuid is only scored once
                    assert k not in used_uuids
                    used_uuids.append(k)

                scores = get_ranx_scores(qrels_lang, run_lang, metrics)
                scores = {k.replace("_","@"):v for k,v in scores.items()}
                docs_scores[doc] = scores
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
    print (result)
    return result


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-q", "--qrels", type=str, required=True)
    parser.add_argument("-r", "--run", type=str, required=True)
    parser.add_argument("-m", "--metrics", default=DEFAULT_METRICS, type=str, nargs='+', required=False)
    parser.add_argument("-l", "--langs-file", type=str, required=True)
    parser.add_argument("-d", "--docs-file", type=str, required=True)
    args = parser.parse_args()
    
    main(qrels_path=args.qrels, run_path=args.run, metrics=args.metrics, langs_file=args.langs_file, docs_file=args.docs_file)
