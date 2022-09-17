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

    def preprocess_document(self,train_df:pd.DataFrame):

        train_doc = []
        for i in range(train_df.shape[0]):
            ent = train_df.label.iloc[i]
            docu = train_df.document.iloc[i].replace("\n", " ")
            if len(ent) != 0:
                train_doc.append(docu+"\n\nExtracted Text:" +'\n'+ent+"----\n")

        with open('../data/training_prompt.txt', 'w') as f:
            for item in train_doc:
                # write each item on a new line
                f.write("%s\n" % item.strip())
        return train_doc

    def entity_extraction(self,test_df:pd.DataFrame):
        test_doc = test_df.document.apply(lambda x: x.replace("\n", " ")+'\n\nExtracted Text:').to_list()
        return test_doc