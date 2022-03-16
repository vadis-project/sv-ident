# SV-Ident: Survey Variable Identification Shared Task (2022)

This is the repository for the shared task SV-Ident: Survey Variable Identification, which will be held at the [Third Workshop on Scholarly Document Processing](https://sdproc.org/2022/) at [COLING 2022](https://coling2022.org).

## Task Description
The task aims to build systems that, given a social science publication, can robustly identify all mentions of relevant survey variables. 

The shared task is split into two sub-tasks:

- Task 1 - Variable Detection: identifying whether a sentence contains a variable mention or not.
- Task 2 - Variable Disambiguation: identifying which variable from a given vocabulary is mentioned in a sentence.

Visit our [homepage](https://vadis-project.github.io/sv-ident-sdp2022/) for more details on the task and submission.

## Data
The data folder currently contains trial data, which is split into training and test sets.  In total, it contains 1227 sentences. The vocabulary contains 406 items.

We will release a larger training set at a later stage (see the timeline [here](https://vadis-project.github.io/sv-ident-sdp2022/)).

## Baselines
We provide lexical and neural baselines for both tasks. The [notebooks](https://github.com/vadis-project/sv-ident/tree/main/notebooks) can be used as a starting point.

### Installation
The code was tested using Python 3.8

```
python3 -m venv venv
source /venv/bin/activate
pip3 install --upgrade pip setuptools wheel
pip3 install -r requirements.txt
```

If you just wish to only install the dependencies for the evaluation, you can install those using `requirements.eval.txt`.

## Evaluation
To evaluate your performance, you can use the [evaluation scripts](https://github.com/vadis-project/sv-ident/tree/main/scripts) for each task.

## Repository Structure
```
├── data
│   ├── trial
│   │   ├── train
│   │   │   ├── en.tsv
│   │   │   └── de.tsv
│   │   ├── test
│   │   │   ├── en.tsv
│   │   │   └── de.tsv
│   │   ├── vocabulary
│   │   │   ├── en.tsv
│   │   │   └── de.tsv
├── notebooks
│   ├── variable_detection
│   │   ├── bow_lr_classification.ipynb
│   │   └── neural_text_classification.ipynb
│   ├── variable_disambiguation
│   │   ├── bow_similarity.ipynb
│   │   └── dense_retrieval.ipynb
├── scripts
│   ├── evaluate_task1.py
│   └── evaluate_task2.ipynb
├── .gitignore
├── README.md
├── requirements.eval.pdf
└── requirements.txt
```