## Data

This folder currently contains trial data, which is split into training and test sets. In total, it contains 1217 sentences (533 for English and 684 for German). The files contain the following columns:

```
context_id:     ID of the context of the textual instance.
text:           Textual instance, which may contain a variable mention.
is_variable:    Label, whether the textual instance contains a variable mention (1) or not (0).
variable:       Variables (separated by a comma ",") that are mentioned in the textual instance. The variable ID number is to the left of the hyphen "-", while to the right, "yes" variables are those that are mentioned in the textual instance and "no" variables are those that are semantically relevant, but are not mentioned in the text.
doc_id:         ID of the source document.
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