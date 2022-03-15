import spacy

# text form geonet https://community.esri.com/t5/arcgis-experience-builder-questions/
text = "I have set up an Edit widget in my Experience Builder app (an ESRI product)."
nlp = spacy.load('en_core_web_lg')
doc = nlp(text)
print("\nEntities found before training:")
for ent in doc.ents:
    print(ent.label_, ent.text)

nlp = spacy.load('./training/model-last')
doc = nlp(text)

print("\nEntities found after training:")
for ent in doc.ents:
    print(ent.label_, ent.text)