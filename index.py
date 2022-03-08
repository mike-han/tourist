import spacy

# text form geonet https://community.esri.com/t5/arcgis-experience-builder-questions/
text = "I have set up an Edit widget in my Experience Builder app. Before the user selects a feature to edit, the widget displays a title at the top, which is taken from the name I have given the widget. However when the user selects a feature, that title changes to the word \"undefined\". I can't figure out where it is getting \"undefined\" from or what to do to fix it. I've tried using both customised settings and the web map settings for the data source, and I\'ve tried changing things in the web map pop-ups and form builder, but none of those make any difference."
nlp = spacy.load('en_core_web_lg')
doc = nlp(text)
print("\nEntities found before training:")
for ent in doc.ents:
    # if ent.label_=='PRODUCT':
    print(ent.label_, ent.text)

nlp = spacy.load('./training/model-best')
doc = nlp(text)

print("\nEntities found after training:")
for ent in doc.ents:
    # if ent.label_=='PRODUCT':
    print(ent.label_, ent.text)