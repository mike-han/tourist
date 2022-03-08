# 🪐 spaCy Project: Detecting widgets in ArcGIS Experience builder (Named Entity Recognition)

This project use the train raw data from [`cyanbird`](https://github.com/mike-han/cyanbird) to bootstrap an NER model to detect the [`widgets`](https://doc.arcgis.com/en/experience-builder/configure-widgets/widgets-overview.htm) in [`ArcGIS Experience builder`](https://www.esri.com/en-us/arcgis/products/arcgis-experience-builder/overview)

## 📋 project.yml
The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. ∏
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `install` | Install necessary dependencies |
| `preprocess` | Convert the data to spaCy's binary format |
| `augment` | Split processed data into training and evaluation datasets |
| `train` | Train a named entity recognition model |
| `evaluate` | Evaluate the model and export metrics |
| `package` | Package the trained model so it can be installed |
| `visualize-model` | Visualize the model's output interactively using Streamlit |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | ``preprocess` &rarr; `augment` &rarr; `train` &rarr; `evaluate` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| [`assets/project_raw.json`](assets/project_raw.json) | Local | JSON-formatted training data exported from [`cyanbird`](https://github.com/mike-han/cyanbird), annotated with `EXB_WIDGET` entities |
| [`assets/widget_patterns.json`](assets/widget_patterns.json) | Local | JSON-formatted the widget patterns of ArcGIS Experience builder doc size|
| [`assets/fashion_brands_patterns.jsonl`](assets/fashion_brands_patterns.jsonl) | Local | Patterns file generated with the `widgets of ArcGIS Experience builder` and used to pre-highlight during annotation |

### Visualize the model

The [`visualize_model.py`](scripts/visualize_model.py) script is powered by
[`spacy-streamlit`](https://github.com/explosion/spacy-streamlit) and lets you
explore the trained model interactively.

```bash
python -m spacy project run visualize-model
```

### Training and evaluation data format

The training and evaluation datasets are distributed in cyanbird's simple JSON
format. Each entry contains a `"name"` and a list of
`"data"` with the text which contains a description of the widget. Here's a
simplified example entry:

```json
{
    "name": "bookmark-widget",
    "data": [
      "The Bookmark widget stores a collection of spatial bookmarks for a selected map. Specify 2D or 3D geographic locations with different extents, view angles (for 3D), layer visibility, and drawing marks."
    ]
  },
```
