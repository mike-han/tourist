from pathlib import Path
import random
from typing import List

import spacy
import typer
from spacy.tokens import Doc, DocBin
from wasabi import msg

def main(
    input_path: Path = typer.Argument(..., exists=True, dir_okay=False),
    training_output_path: Path = typer.Argument(..., dir_okay=False),
    dev_output_path: Path = typer.Argument(..., dir_okay=False),
    limit: int = typer.Option(None, envvar="NUM_DOCS_TO_AUGMENT"),
):

    msg.info(f"Reading data from {input_path}")
    db = DocBin()
    nlp = spacy.blank("en")
    docs = list(db.from_disk(input_path).get_docs(nlp.vocab))
    length = len(docs)
    msg.info(f"Total number of docs: {length}")
    random.shuffle(docs)
    training_docs = docs[:int(length/2)]
    dev_docs = docs[int(length/2):]
    msg.info(f"Total number of training docs: {len(training_docs)}")
    msg.info(f"Total number of dev docs: {len(dev_docs)}")

    training_db = DocBin(docs=training_docs)
    dev_db = DocBin(docs=dev_docs)
    training_db.to_disk(training_output_path)
    dev_db.to_disk(dev_output_path)
    msg.info(f"Total number of docs: {length}")
    msg.info(f"Augment training data successfully saved to {training_output_path} and {dev_output_path}!")
if __name__ == "__main__":
    typer.run(main)
