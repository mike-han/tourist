import spacy
from spacy.language import Language
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span
nlp = spacy.load("en_core_web_lg")

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

doc = nlp("Esri has many very good products, such as Survey, Earth and ExB")

print([(ent.text, ent.label_) for ent in doc.ents])