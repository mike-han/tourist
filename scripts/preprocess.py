import json
import typer
import srsly
from pathlib import Path
from spacy.util import get_words_and_spaces
from spacy.tokens import Doc, DocBin
import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span
from spacy.util import filter_spans


def get_widget_patters():
  patterns = {"label": "EXB_WIDGET", "patterns": []}
  with open("assets/widget_patterns.json", encoding="utf8") as f:
    widgets = json.loads(f.read())
    patterns["patterns"] = [widget["patterns"] for widget in widgets]
  return patterns

def process_text(text):
    nlp = spacy.blank("en")
    tokens = [token.text for token in nlp(text)]
    words, spaces = get_words_and_spaces(tokens, text)
    doc = Doc(nlp.vocab, words=words, spaces=spaces)
    matcher = Matcher(nlp.vocab)
    widget_pattern = get_widget_patters()
    matcher.add(widget_pattern["label"], widget_pattern["patterns"])

    doc = nlp(text)
    matches = matcher(doc)
    ents = [Span(doc, start, end, label=widget_pattern["label"]) for match_id, start, end in matches]
    doc.ents = filter_spans(ents)
    return doc

def main(
    input_path: Path = typer.Argument(..., exists=True, dir_okay=False),
    output_path: Path = typer.Argument(..., dir_okay=False),
):
   
    doc_bin = DocBin(attrs=["ENT_IOB", "ENT_TYPE"])
    widgets = srsly.read_json(input_path)
    for widget in widgets:
        texts = widget["data"]
        for text in texts:
            doc = process_text(text)
            doc_bin.add(doc)
    doc_bin.to_disk(output_path)
    print(f"Processed {len(doc_bin)} documents: {output_path.name}")


if __name__ == "__main__":
    typer.run(main)
