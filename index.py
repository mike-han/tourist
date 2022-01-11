import spacy

text = "ArcGIS Experience builder is a great product. Earth is a great product. Survey123 is a great product."

nlp = spacy.load('en_core_web_lg')
doc = nlp(text)
print("\nEntities found before training:")
for ent in doc.ents:
    # if ent.label_=='PRODUCT':
    print(ent.label_, ent.text)

nlp = spacy.load('./training/model-last')
doc = nlp(text)

print("\nEntities found after training:")
for ent in doc.ents:
    # if ent.label_=='PRODUCT':
    print(ent.label_, ent.text)