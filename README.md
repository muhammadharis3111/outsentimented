# OutSentimented

**OutSentimented: BERT-Based Financial News Sentiment Intelligence** is an MGT488 Advanced Deep Learning semester project. The planned module accepts one English financial-news sentence and returns `positive`, `neutral`, or `negative` with a confidence score.

This repository is the Week 8 Milestone 1 package. It contains the proposal, verified dataset workflow, baseline methodology, and an executed EDA notebook. It does not contain a trained baseline, a fine-tuned BERT model, model weights, or measured model performance.

## Team

- Muhammad Haris — FA23-BBD-094
- Sobia Rauf — FA23-BBD-133

## Business use case

The classifier is intended to support analysts who monitor financial news. It can provide a consistent first-pass category, help prioritize potentially negative developments, and reduce repetitive screening. Low-confidence predictions can be routed for manual review. The output is not investment advice and does not predict returns or recommend trades.

## Week 8 deliverables

- [IEEE proposal in DOCX](reports/OutSentimented_Week_8_Proposal.docx)
- [Submission-ready proposal in PDF](reports/OutSentimented_Week_8_Proposal.pdf)
- [Executed Financial PhraseBank EDA notebook](notebooks/01_financial_phrasebank_eda.ipynb)
- Typed classifier interface in `src/outsentimented/api.py`

## Dataset and license

The EDA uses the `sentences_75agree` configuration of [Financial PhraseBank](https://huggingface.co/datasets/takala/financial_phrasebank), introduced by Malo et al. in *Good Debt or Bad Debt: Detecting Semantic Orientations in Economic Texts*.

- Raw configuration size: 3,453 sentences
- Raw labels: 2,146 neutral, 887 positive, and 420 negative
- Source archive SHA-256: `0e1a06c4900fdae46091d031068601e3773ba067c7cecb5b0da1dcba5ce989a6`
- Dataset license: CC BY-NC-SA 3.0
- Repository code and original project documents: MIT

The notebook downloads the source archive into `data/raw/` and generates split CSV files in `data/processed/`. Both directories are ignored by Git except for their placeholders. The MIT license for this repository does not replace or relax the dataset license.

## Verified EDA findings

The executed notebook found no missing or blank fields. It identified five exact duplicate sentences, all neutral and without conflicting labels. Removing one copy from each pair left 3,448 unique sentences.

The notebook then created deterministic stratified partitions with seed `42`:

| Split | Negative | Neutral | Positive | Total | Share |
| --- | ---: | ---: | ---: | ---: | ---: |
| Train | 294 | 1,498 | 621 | 2,413 | 69.98% |
| Validation | 63 | 321 | 133 | 517 | 14.99% |
| Test | 63 | 322 | 133 | 518 | 15.02% |

The sentence sets have zero overlap across the three partitions. Notebook outputs also include class distribution, sentence-length statistics, representative records, and class-level bigrams.

## Reproduce the notebook

The project targets Python 3.10. From the repository root:

```bash
uv venv --python 3.10 .venv
uv pip install --python .venv/bin/python -r requirements.txt
.venv/bin/python scripts/run_notebook.py
.venv/bin/python -m pytest
```

The first notebook run requires internet access to download the verified archive. Later runs can reuse the ignored local copy. The execution script fails on a checksum mismatch, unexpected row count, unexpected label set, failed notebook cell, split overlap, or incomplete partition assignment.

## Planned methodology

### Comparison baseline

Milestone 2 will train TF-IDF features with multinomial logistic regression. Validation trials will compare unigram and bigram features, vocabulary limits, regularization, and class weighting. The TF-IDF vocabulary and estimator will be fit only on the training partition.

### Advanced model

Milestone 3 will fine-tune KerasHub `bert_base_en_uncased` for three classes. The planned input limit is 128 tokens. Experiments will use a small local batch size, early stopping, and documented learning-rate and epoch trials. Training is reserved for an M1 MacBook Pro with 16 GB memory. A separate compatible TensorFlow environment will validate the Metal plug-in before full training, with CPU execution retained as a slower fallback.

### Evaluation

The final comparison will report accuracy, macro precision, macro recall, macro F1, per-class precision, recall and F1, a confusion matrix, and reviewed errors. Macro F1 is the primary model-selection measure because every class matters even though the data is imbalanced. The test set will remain untouched until model and threshold choices are fixed from training and validation evidence.

## Module interface

The typed Week 8 contract is:

```python
classifier(sentence: str) -> {"label": "positive" | "neutral" | "negative", "confidence": float}
```

The repository currently defines this contract but intentionally provides no trained implementation.

## Repository structure

```text
.
├── data
│   ├── processed
│   └── raw
├── notebooks
│   └── 01_financial_phrasebank_eda.ipynb
├── reports
│   ├── OutSentimented_Week_8_Proposal.docx
│   └── OutSentimented_Week_8_Proposal.pdf
├── scripts
│   └── run_notebook.py
├── src
│   └── outsentimented
│       ├── __init__.py
│       └── api.py
├── tests
│   └── test_api.py
├── LICENSE
├── pyproject.toml
└── requirements.txt
```

## Milestone status

| Deliverable | Status |
| --- | --- |
| Proposal and business scope | Complete |
| Dataset source and license verification | Complete |
| Executed EDA and leakage-free partitions | Complete |
| Baseline methodology | Specified, not trained |
| TF-IDF logistic-regression baseline | Planned for Milestone 2 |
| BERT fine-tuning and test evaluation | Planned for Milestone 3 |

## References

1. Malo, P., Sinha, A., Korhonen, P., Wallenius, J., and Takala, P. “Good Debt or Bad Debt: Detecting Semantic Orientations in Economic Texts.” *Journal of the Association for Information Science and Technology*, 65(4), 782–796, 2014.
2. Devlin, J., Chang, M.-W., Lee, K., and Toutanova, K. “BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.” *NAACL-HLT*, 2019.
3. [KerasHub BertTextClassifier documentation](https://keras.io/keras_hub/api/models/bert/bert_text_classifier/)

## License

Original repository code and project documents are available under the [MIT License](LICENSE). Financial PhraseBank remains subject to CC BY-NC-SA 3.0.
