
# Requirements

-   [python v3.10](https://www.python.org/downloads/) - version 3.10, as it is the last one supported by Rasa.
-   [spacy](https://spacy.io/usage)
-   [Rasa](https://rasa.com/docs/rasa/installation/installing-rasa-open-source)


# Getting Started

Install Polish spaCy pipeline
```bash
$ python -m spacy download pl_core_news_sm
```
Train rasa model
```bash
$ python -m rasa train
```
Run rasa server
```bash
$ python -m rasa run actions
```
Run conversation with bot
```bash
$ python -m rasa shell
```



