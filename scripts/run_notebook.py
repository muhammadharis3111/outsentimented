from pathlib import Path

import nbformat
from nbclient import NotebookClient


root = Path(__file__).resolve().parents[1]
path = root / "notebooks" / "01_financial_phrasebank_eda.ipynb"
notebook = nbformat.read(path, as_version=4)
client = NotebookClient(
    notebook,
    timeout=180,
    kernel_name="python3",
    resources={"metadata": {"path": str(root)}},
    allow_errors=False,
)
client.execute()
nbformat.write(notebook, path)

