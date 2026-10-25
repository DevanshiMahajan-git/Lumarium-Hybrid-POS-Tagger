# Evaluation on test set

160 sentences, 3476 tokens.

## Ablation

| System | Accuracy | Macro-F1 | Weighted-F1 |
|---|---|---|---|
| HMM only | 0.8657 | 0.8342 | 0.8651 |
| Transformer only | 0.8867 | 0.8460 | 0.8864 |
| Rules → HMM | 0.8619 | 0.8300 | 0.8615 |
| Hybrid — blueprint (0.85, rules final) | 0.8852 | 0.8475 | 0.8844 |
| Hybrid — tuned on dev (0.70, hmm) | 0.8907 | 0.8579 | 0.8902 |

Rules alone fire on 24.3% of tokens with 95.7% precision.
HMM accuracy on OOV tokens: 50.7% (483 tokens).

## Which tier made the final call

| Source | Tokens | Share | Accuracy |
|---|---|---|---|
| transformer | 2249 | 64.7% | 92.1% |
| rule | 820 | 23.6% | 98.4% |
| hmm | 230 | 6.6% | 38.3% |
| transformer+hmm | 177 | 5.1% | 72.9% |

## Per-tag scores (final hybrid)

| Tag | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| X | 0.987 | 0.977 | 0.982 | 790 |
| VERB | 0.905 | 0.921 | 0.913 | 669 |
| NOUN | 0.843 | 0.874 | 0.858 | 516 |
| ADP | 0.915 | 0.931 | 0.923 | 346 |
| PROPN | 0.860 | 0.793 | 0.825 | 271 |
| PRON | 0.849 | 0.854 | 0.851 | 198 |
| PART | 0.846 | 0.819 | 0.832 | 188 |
| ADJ | 0.755 | 0.688 | 0.720 | 170 |
| DET | 0.824 | 0.888 | 0.855 | 116 |
| ADV | 0.788 | 0.780 | 0.784 | 100 |
| CCONJ | 0.877 | 0.831 | 0.853 | 77 |
| NUM | 0.814 | 1.000 | 0.897 | 35 |

## Most common errors (gold → predicted)

| Gold | Predicted | Count |
|---|---|---|
| NOUN | VERB | 26 |
| PROPN | NOUN | 20 |
| VERB | NOUN | 19 |
| ADJ | NOUN | 16 |
| ADJ | PROPN | 14 |
| ADP | PART | 12 |
| NOUN | ADJ | 11 |
| NOUN | PROPN | 11 |
| VERB | PRON | 11 |
| PART | VERB | 10 |
