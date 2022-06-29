## Data

This folder currently contains training data. In total, there are 4,248 sentences. The data file is made up of the following columns:

```
sentence:       Textual instance, which may contain a variable mention.
is_variable:    Label, whether the textual instance contains a variable mention (1) or not (0). This column can be used for Task 1 (Variable Detection).
variable:       Variables (separated by a comma ";") that are mentioned in the textual instance. This column can be used for Task 2 (Variable Disambiguation). Variables with the "unk" tag could not be mapped to a unique variable.
research_data:  Research data IDs (separated by a ";") that are relevant for each instance (and in general for each "doc_id").
doc_id:         ID of the source document. Each document is written in one language (either English or German).
uuid:           Unique ID of the instance in uuid4 format.
```

The language for each document can be found in the document-language mapping file [here](https://github.com/vadis-project/sv-ident/blob/main/data/train/document_languages.json), which maps `doc_id` to a language code (`en`, `de`). The variables metadata (i.e., the vocabulary) can be downloaded from this [link](https://bit.ly/3Nuvqdu). We recommend downloading it into this directory (`/sv-ident/data/train/`). Note, that each `research_data` contains hundres of variables (these can be understood as the corpus of documents to choose the most relevant from). If the variable has an "unk" tag, it means that the sentence contains a variable that has not been disambiguated. Such sentences could be used for Task 1 and filtered out for Task 2. The metadata file has the following format:

```
{
  "research_data_id_1": {
    "variable_id_1": VARIABLE_METADATA,
    ...
    "variable_id_n": VARIABLE_METADATA,
  },
  ...
  "research_data_id_n": {...},
}
```

Each variable may contain all (or some) of the following values:
```
study_title:        The title of the research data study.
variable_label:     The label of the variable.
variable_name:      The name of the variable.
question_text:      The question of the variable in the original language.
question_text_en:   The question of the variable in English.
sub_question:       The sub-question of the variable.
item_categories:    The item categories of the variable.
answer_categories:  The answers of the variable.
topic:              The topics of the variable in the original language.
topic_en:           The topics of the variable in English.
```

An example of a single variable can be seen below:
```
{
  "study_title": "International Social Survey Programme:  National Identity II - ISSP 2003",
  "variable_label": "Q3g Important: To feel [Country Nationality]",
  "variable_name": "V17",
  "question_text": "Some people say that the following things are important for being truly [NATIONALITY]. Others say they are not important. How important do you think each of the following is... ",
  "question_text_en": "Some people say that the following things are important for being truly [NATIONALITY]. Others say they are not important. How important do you think each of the following is... ",
  "sub_question": "Q.3g - To feel [COUNTRY NATIONALITY]",
  "item_categories": "To have been born in [COUNTRY];To have [COUNTRY] citizenship;To have lived in [COUNTRY] for most of one's life;To be able to speak [COUNTRY LANGUAGE] [Dominant language(s): If two or more languages are recognized nationwide both are included in the question. However, if there is one national lingua franca (Spanish, Russian) just give this language];To be a [religion] [The dominant religion or denomination in your country should be given (eg. Christian in the US and Canada, Catholic in Ireland and Italy, Russian Orthodox in Russia)];To respect [COUNTRY NATIONALITY] political institutions and laws",
  "answer_categories": "Very important;Fairly important;Not very important;Not important at all;Can't choose;No answer, refused",
  "topic": [
    "Migration",
    "Kulturelle und nationale Identität",
    "Soziales Verhalten und soziale Einstellungen",
    "Politische Verhaltensweisen und Einstellungen/Meinungen"
  ],
  "topic_en": [
    "Migration",
    "Cultural and national identity",
    "Social behaviour and attitudes",
    "Mass political behaviour, attitudes/opinion"
  ]
}
```

### Usage

To load the data, you can simply use HuggingFace Datasets:

![Example for loading the dataset using the Datasets library.](https://github.com/vadis-project/sv-ident/blob/main/data/train/figures/load_dataset.png)


### License
All documents originate from the Social Science Open Access Repository (SSOAR) and are licensed accordingly. The original document URLs are provided in `document_urls.json`. For more information on licensing, please refer to the terms and conditions on the [SSAOR Grant of Licenses page](https://www.gesis.org/en/ssoar/home/information/grant-of-licences).
