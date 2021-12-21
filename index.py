import spacy

nlp = spacy.blank('en')

ner = nlp.create_pipe("ner")
nlp.add_pipe(ner)
ner.add_label("GADGET")