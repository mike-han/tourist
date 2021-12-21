import spacy
from spacy.language import Language
from spacy.matcher import PhraseMatcher
from spacy.tokens import Doc, Token, Span
nlp = spacy.load("en_core_web_sm")

products = ["ExB", "Survey", "Earth"]
products_patterns = list(nlp.pipe(products))
matcher = PhraseMatcher(nlp.vocab)
matcher.add("PRODUCT", products_patterns)

@Language.component("product_component")
def product_component(doc):
   matches = matcher(doc)
   spans = [Span(doc, start, end, label="PRODUCT") for match_id, start, end in matches]
   doc.ents = spans
   return doc

nlp.add_pipe('product_component', first=True)

def get_google_url(span):
    if span.label_ in ("PERSON", "ORG", "GPE", "LOCATION", "PRODUCT"):
        entity_text = span.text.replace(" ", "_")
        return "https://https://www.google.com/search?q=" + entity_text


Span.set_extension('google_url', getter=get_google_url)

doc = nlp("Esri has many very good products, such as Survey, Earth and ExB")

for ent in doc.ents:
  print(ent.text, ent._.google_url)