# SV-Ident: Survey Variable Identification Shared Task (2022)

This is the repository for the shared task **SV-Ident**: **S**urvey **V**ariable **Ident**ification, which will be held at the [Third Workshop on Scholarly Document Processing](https://sdproc.org/2022/) at [COLING 2022](https://coling2022.org).

## News
> **June 8, 2022:**
> We released the first half of the official training data (the second half is coming soon!)

> **March 15, 2022:**
> We released trial data

## Task Description
The task aims to build systems that, given a scientific social science publication, can robustly identify all mentions of relevant survey variables (see [http://www.aclweb.org/anthology/W17-2907](http://www.aclweb.org/anthology/W17-2907) for more explanations). 

The shared task is split into two sub-tasks:

- Task 1 - Variable Detection: identifying whether a sentence contains a variable mention or not.
- Task 2 - Variable Disambiguation: identifying which variable from a given vocabulary is mentioned in a sentence.

Visit our [homepage](https://vadis-project.github.io/sv-ident-sdp2022/) for more details on the task and submission.

## Data
This repository contains trial data (found [here](https://github.com/vadis-project/sv-ident/tree/main/data/trial)) and training data (found [here](https://github.com/vadis-project/sv-ident/tree/main/data/train)). For details on the data format, please have a look at the README files for each data directory. For Task 2, in addition to the training data, the variable vocabulary is necessary to disambiguate among the thousands of possible variables. The vocabulary can be downloaded from [here](https://drive.google.com/file/d/18slgACOcE8-_xIDX09GrdpFSqRRcBiON/view?usp=sharing). We recommend downloading it into this directory (`/sv-ident/data/train/`). For the trial data, the variable vocabulary is already provided in the respective directory.

## Baselines
We provide lexical and neural baselines for both tasks. The [notebooks](https://github.com/vadis-project/sv-ident/tree/main/notebooks) can be used as starting points.

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
│   │   ├── context
│   │   │   ├── de.tsv
│   │   │   └── en.tsv
│   │   ├── train
│   │   │   ├── de.tsv
│   │   │   └── en.tsv
│   │   ├── test
│   │   │   ├── de.tsv
│   │   │   └── en.tsv
│   │   ├── vocabulary
│   │   │   ├── de.tsv
│   │   │   └── en.tsv
│   ├── train
│   │   ├── document_languages.tsv
│   │   ├── document_urls.json
│   │   ├── subset.tsv
│   │   └── variable_metadata.json (download from external source)
├── notebooks
│   ├── variable_detection
│   │   ├── bow_lr_classification.ipynb
│   │   └── neural_text_classification.ipynb
│   ├── variable_disambiguation
│   │   ├── bow_similarity.ipynb
│   │   └── dense_retrieval.ipynb
├── scripts
│   ├── evaluate_task1.py
│   └── evaluate_task2.py
├── .gitignore
├── README.md
├── requirements.eval.txt
└── requirements.txt
```

### License
Please view the license section in the README of each data directory (trial and [train](https://github.com/vadis-project/sv-ident/tree/main/data/train#license)).
