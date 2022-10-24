# SV-Ident: Survey Variable Identification Shared Task (2022)

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/overview-of-the-sv-ident-2022-shared-task-on/variable-disambiguation-on-sv-ident)](https://paperswithcode.com/sota/variable-disambiguation-on-sv-ident?p=overview-of-the-sv-ident-2022-shared-task-on)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/overview-of-the-sv-ident-2022-shared-task-on/variable-detection-on-sv-ident)](https://paperswithcode.com/sota/variable-detection-on-sv-ident?p=overview-of-the-sv-ident-2022-shared-task-on)

This is the repository for the shared task **SV-Ident**: **S**urvey **V**ariable **Ident**ification, which will be held at the [Third Workshop on Scholarly Document Processing](https://sdproc.org/2022/) at [COLING 2022](https://coling2022.org).

## News
> **October 17, 2022:**
> The [shared task competition on CodaLab](https://codalab.lisn.upsaclay.fr/competitions/6400) is now open-ended with no deadline and there are no submission limits.

> **October 12, 2022:**
> We have published an overview of the results for the shared task [[3](https://aclanthology.org/2022.sdp-1.29/)].

> **July 18, 2022:**
> We have released the test data and are evaluating submissions via [CodaLab](https://codalab.lisn.upsaclay.fr/competitions/6400)

> **July 5, 2022:**
> We have extended the registration deadline **until July 14th!** Register [here](https://forms.gle/qErcUKBc2mCednJ79) to participate!

> **June 23, 2022:**
> We opened registration (if you wish to participate, please fill out [this form](https://forms.gle/qErcUKBc2mCednJ79))

> **June 8, 2022:**
> We released the official training data

> **March 15, 2022:**
> We released trial data

## Task Description
The task aims to build systems that, given a scientific social science publication, can robustly identify all mentions of relevant survey variables [[1](https://aclanthology.org/W17-2907/), [2](https://aclanthology.org/L18-1084/), [3](https://aclanthology.org/2022.sdp-1.29/)].

The shared task is split into two sub-tasks:

- Task 1 - Variable Detection: identifying whether a sentence contains a variable mention or not.
- Task 2 - Variable Disambiguation: identifying which variable from a given vocabulary is mentioned in a sentence. **NOTE**: for this task, you will need to also download the variable metadata from [here](https://bit.ly/3Nuvqdu).

Visit our [homepage](https://vadis-project.github.io/sv-ident-sdp2022/) for more details on the task and submission.

## Data
This repository contains trial data (found [here](https://github.com/vadis-project/sv-ident/tree/main/data/trial)) and training data (found [here](https://github.com/vadis-project/sv-ident/tree/main/data/train)). The training data also resides under the `vadis/sv-ident` tag on [HuggingFace Datsets](https://huggingface.co/datasets/vadis/sv-ident). For details on the data format, please have a look at the README files for each data directory. For Task 2 (Variable Disambiguation), in addition to the training data, the variable vocabulary is necessary to disambiguate among the thousands of possible variables. The vocabulary can be downloaded from [here](https://bit.ly/3Nuvqdu). We recommend downloading it into this directory (`/sv-ident/data/train/`). For the trial data, the variable vocabulary is already provided in the respective directory.

![Example for loading the training dataset using the Datasets library.](https://github.com/vadis-project/sv-ident/blob/main/data/train/figures/load_dataset.png)

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
To evaluate your performance, you can use the [evaluation scripts](https://github.com/vadis-project/sv-ident/tree/main/scripts) for each task. Task 1 will be evaluated using sklearn's F1-macro (as implemented in `scripts/evaluate_task1.py`). Task 2 will be evaluated using (Mean) Average Precision with a cutoff of 10 (MAP@10) using [ranx](https://amenra.github.io/ranx/metrics/#mean-average-precision) (as implemented in `scripts/evaluate_task2.py`).

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

### Citation
If you use this dataset, please cite it as below:
```
@inproceedings{tsereteli-etal-2022-overview,
    title = "Overview of the {SV}-Ident 2022 Shared Task on Survey Variable Identification in Social Science Publications",
    author = "Tsereteli, Tornike  and
      Kartal, Yavuz Selim  and
      Ponzetto, Simone Paolo  and
      Zielinski, Andrea  and
      Eckert, Kai  and
      Mayr, Philipp",
    booktitle = "Proceedings of the Third Workshop on Scholarly Document Processing",
    month = oct,
    year = "2022",
    address = "Gyeongju, Republic of Korea",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.sdp-1.29",
    pages = "229--246",
    abstract = "In this paper, we provide an overview of the SV-Ident shared task as part of the 3rd Workshop on Scholarly Document Processing (SDP) at COLING 2022. In the shared task, participants were provided with a sentence and a vocabulary of variables, and asked to identify which variables, if any, are mentioned in individual sentences from scholarly documents in full text. Two teams made a total of 9 submissions to the shared task leaderboard. While none of the teams improve on the baseline systems, we still draw insights from their submissions. Furthermore, we provide a detailed evaluation. Data and baselines for our shared task are freely available at \url{https://github.com/vadis-project/sv-ident}.",
}
```

### License
Please view the license section in the README of each data directory (trial and [train](https://github.com/vadis-project/sv-ident/tree/main/data/train#license)).

### References
[1] Andrea Zielinski and Peter Mutschke. 2017. Mining Social Science Publications for Survey Variables. In Proceedings of the Second Workshop on NLP and Computational Social Science, pages 47–52, Vancouver, Canada. Association for Computational Linguistics.

[2] Andrea Zielinski and Peter Mutschke. 2018. Towards a Gold Standard Corpus for Variable Detection and Linking in Social Science Publications. In Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018), Miyazaki, Japan. European Language Resources Association (ELRA).

[3] Tornike Tsereteli, Yavuz Selim Kartal, Simone Paolo Ponzetto, Andrea Zielinski, Kai Eckert, and Philipp Mayr. 2022. Overview of the SV-Ident 2022 Shared Task on Survey Variable Identification in Social Science Publications. In Proceedings of the Third Workshop on Scholarly Document Processing, pages 229–246, Gyeongju, Republic of Korea. Association for Computational Linguistics.
