from html import entities
import pandas as pd

class Preporcess:
    def __init__(self) -> None:
        pass

    def preprocess_tokens(self,tokens):
        entities = {}
        for token in tokens:

            if token['entityLabel'] in entities.keys():
                entities[token['entityLabel']] = entities[token['entityLabel']] + ','+ token['text']
            else:
                entities[token['entityLabel']] = token['text']
        label = ""
        for k, v in entities.items():
            label += k+':'+v+"\n"
        return label