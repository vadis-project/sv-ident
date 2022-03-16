# SV-Ident: Survey Variable Identification Shared Task (2022)

This is the repository for the shared task SV-Ident: Survey Variable Identification, which will be held at the [Third Workshop on Scholarly Document Processing](https://sdproc.org/2022/) at [COLING 2022](https://coling2022.org).

## Task Description
The task aims to build systems that, given a social science publication, can robustly identify all mentions of relevant survey variables. 

The shared task is split into two sub-tasks:

- Task 1 - Variable Detection: identifying whether a sentence contains a variable mention or not.
- Task 2 - Variable Disambiguation: identifying which variable from a given vocabulary is mentioned in a sentence.

Visit our [homepage](https://vadis-project.github.io/sv-ident-sdp2022/) for more details on the task and submission.

## Data
The data folder currently contains trial data, which is split into training and test sets.  In total, it contains 1217 sentences (533 for English and 684 for German). The files contain the following columns:

```
doc_id:         ID of the source document.
context_id:     ID of the context of the textual instance.
text:           Textual instance, which may contain a variable mention.
is_variable:    Label, whether the textual instance contains a variable mention (1) or not (0).
variable:       Variables (separated by a comma ",") that are mentioned in the textual instance. The variable ID number is to the left of the hyphen "-", while to the right, "yes" variables are those that are mentioned in the textual instance and "no" variables are those that are semantically relevant, but are not mentioned in the text.
uuid:           Unique ID of the instance in uuid4 format.
```

The context files contain 185 paragraphs (89 for English and 96 for German). The files contain the following columns:

```
context_id:     ID of the context.
context:        Textual context containing multiple sentences. These make up (parts-of) paragraphs from source documents.
```

The vocabulary contains 406 items (182 for English and 224 for German). The files contain the following columns:

```
id:             ID of the variable.
label:          Label of the variable.
topic:          Topic of the variable.
question:       Variable question text.
answer:         Comma "," separated possible answer choices to the question.
```

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