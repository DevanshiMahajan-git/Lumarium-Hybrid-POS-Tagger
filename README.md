# 🌟 Lumarium: Hybrid POS Tagger & Linguistic Observatory

A hybrid Natural Language Processing (NLP) system for Part-of-Speech (POS) tagging of code-mixed text, combining linguistic rules, transformer-based token classification, and Hidden Markov Models.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Backend](https://img.shields.io/badge/Backend-FastAPI%20%7C%20Uvicorn-009688.svg)](https://fastapi.tiangolo.com/)
[![NLP](https://img.shields.io/badge/NLP-Hybrid%20Tagging-orange.svg)](https://huggingface.co/)
[![Benchmark](https://img.shields.io/badge/Dataset-LinCE%20Hindi--English-success.svg)](https://huggingface.co/datasets/lince-benchmark/lince)

> **Illuminate every word.** Exploring the intersection of linguistic rules, probabilistic models, and contextual NLP for code-mixed language understanding.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [The Problem](#-the-problem)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Technology Stack](#-technology-stack)
- [Benchmark and Evaluation Results](#-benchmark-and-evaluation-results)
- [How It Works](#-how-it-works)
- [Project Structure](#-project-structure)
- [Installation and Quick Start](#-installation-and-quick-start)
- [Training and Evaluation](#-training-and-evaluation)
- [Dataset](#-dataset)
- [Limitations and Future Improvements](#-limitations-and-future-improvements)
- [References](#-references)

---

## 📖 Overview

Code-mixed text frequently combines words from multiple languages within a sentence. Conversational Hinglish, for example, mixes Hindi and English while using informal spellings, Roman transliteration, and language-specific grammatical patterns.

These characteristics make Part-of-Speech (POS) tagging challenging for conventional NLP systems.

**Lumarium** explores a hybrid approach to POS tagging by combining three complementary techniques:

1. **Rule-Based Tagging:** Uses linguistic patterns, lexical information, and morphological rules to identify tokens with recognizable grammatical characteristics.
2. **Transformer-Based Tagging:** Uses contextual representations from a pretrained code-mixed language model to predict POS tags.
3. **Hidden Markov Model (HMM):** Uses probabilistic sequence modelling and the Viterbi algorithm to predict grammatical tag sequences.
4. **Hybrid Arbiter:** Combines available predictions using configurable confidence thresholds, fallback strategies, and rule-based decisions.

The project includes a web application for interacting with the tagging system and exploring linguistic information.

The primary quantitative evaluation uses the **Hindi-English POS dataset from the LinCE benchmark**. Marathi-English patterns are also explored through linguistic rules, but the reported benchmark results should not be interpreted as a quantitative evaluation of Marathi-English tagging.

---

## ⚡ The Problem

POS tagging for code-mixed text presents several challenges:

- **Spelling Variation:** Informal spellings, repeated characters, and inconsistent Roman transliteration.
- **Language Switching:** English and Hindi words can appear together within a single sentence.
- **Morphological Variation:** English roots may occur alongside Hindi or Marathi grammatical markers.
- **Out-of-Vocabulary Tokens:** Unfamiliar words and regional expressions can challenge statistical models.
- **Contextual Ambiguity:** The grammatical role of a token can depend on its surrounding words.
- **Interpretability:** Neural predictions alone may not provide sufficient insight into why a tag was selected.

Lumarium investigates whether combining rule-based, probabilistic, and contextual approaches can improve POS tagging for code-mixed text.

---

## ✨ Key Features

### 🔹 Hybrid POS Tagging
Combines rule-based predictions, a transformer model, and an HMM through a configurable arbitration mechanism.

### 🔹 Linguistic Rule Engine
Uses lexical and morphological patterns to identify tokens that can be tagged through explicit rules.

### 🔹 Contextual Transformer
Uses a pretrained code-mixed Hindi-English POS model to predict tags based on contextual information.

### 🔹 Probabilistic Sequence Modelling
Implements an HMM with Viterbi decoding and suffix-based handling of unknown words.

### 🔹 Confidence-Based Arbitration
Uses rule confidence, transformer confidence, configurable thresholds, and fallback strategies to select final predictions.

### 🔹 Prediction Analysis
Provides information about the selected tagger and the decision made for each token.

### 🔹 Interactive Web Interfaces
Includes a FastAPI-powered web application and a Streamlit dashboard.

### 🔹 Evaluation and Testing
Includes model training, evaluation metrics, ablation comparisons, and automated tests for important pipeline components.

---

## 🏗️ System Architecture

The following diagram illustrates the high-level tagging workflow.

```text
                 ┌──────────────────────────┐
                 │  Input Code-Mixed Text   │
                 └────────────┬─────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │ Tokenization & Text      │
                 │ Preprocessing            │
                 └────────────┬─────────────┘
                              │
             ┌────────────────┼────────────────┐
             │                │                │
             ▼                ▼                ▼
      ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
      │ Rule-Based  │  │ Transformer │  │     HMM     │
      │   Tagger    │  │   Tagger    │  │   Tagger    │
      └──────┬──────┘  └──────┬──────┘  └──────┬──────┘
             │                │                │
             └────────────────┼────────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │     Hybrid Arbiter       │
                 │ Confidence & Fallback    │
                 └────────────┬─────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │ Final POS Tag Sequence   │
                 │ & Decision Information   │
                 └────────────┬─────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │ Web Interface / Analysis │
                 └──────────────────────────┘
```

### Component Responsibilities

| Component | Responsibility |
|---|---|
| Rule-Based Tagger | Identifies tokens using linguistic and morphological rules. |
| Transformer Tagger | Produces contextual POS predictions and confidence scores. |
| HMM Tagger | Predicts tag sequences using learned transition and emission probabilities. |
| Hybrid Arbiter | Selects final tags using configurable decision logic. |
| Evaluation Pipeline | Measures model performance and compares alternative configurations. |
| Web Application | Provides an interface for interacting with the NLP system. |

---

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| NLP and Deep Learning | PyTorch, Hugging Face Transformers |
| Probabilistic Modelling | Hidden Markov Model, Viterbi Algorithm |
| Numerical Computing | NumPy |
| Data Processing | Pandas |
| Backend API | FastAPI, Uvicorn |
| Interactive Dashboard | Streamlit |
| Testing | Pytest |
| Evaluation | Accuracy, Macro-F1, Weighted-F1 |
| Dataset | LinCE Hindi-English POS |
| Development Tools | VS Code, Google Colab |

---

## 📊 Benchmark and Evaluation Results

The project evaluation compares the individual tagging approaches with different hybrid configurations.

### Overall Results

| Model / Configuration | Accuracy | Macro-F1 | Weighted-F1 |
|---|---:|---:|---:|
| HMM Only | 86.57% | 83.42% | 86.51% |
| Transformer Only | 89.24% | 86.62% | 89.24% |
| Rules → HMM | 86.19% | 83.00% | 86.15% |
| Hybrid — Baseline Configuration | 88.92% | 85.41% | 88.86% |
| **Hybrid — Tuned Configuration** | **89.84%** | **86.94%** | **89.83%** |

*Source: `results/report.md` and `results/metrics.json` included with the project.*

### Rule-Based Tagger Performance

The evaluation report records the following results for the rule-based component:

- **Rule coverage:** 24.3% of evaluated tokens.
- **Rule precision:** 95.7%.

These measurements indicate that the rules cover a subset of tokens while achieving high precision on the evaluated data.

### Evaluation Dataset

The recorded evaluation covers:

- **160 sentences**
- **3,476 tokens**
- Hindi-English POS tagging using the LinCE dataset

### Interpretation

The tuned hybrid configuration achieved a reported accuracy of **89.84%**, compared with **89.24%** for the standalone transformer.

The results suggest that combining complementary tagging strategies can improve performance on this evaluation set. However, the improvement is modest, and the results should be interpreted in the context of the dataset, evaluation procedure, and configuration used.

The reported figures are project evaluation results, not a claim of independently reproduced performance.

For detailed per-tag scores, model comparisons, and common tagging errors, see [`results/report.md`](results/report.md).

---

## ⚙️ How It Works

### 1. Text Processing
The input sentence is processed into tokens for the tagging components.

### 2. Rule-Based Prediction
The rule engine checks applicable lexical and morphological patterns and returns a tag when a rule matches.

### 3. Transformer Prediction
The transformer predicts POS labels using contextual representations. The implementation aligns subword predictions with the original word sequence.

### 4. HMM Prediction
The HMM estimates a likely POS sequence using transition and emission probabilities. Viterbi decoding is used to determine the sequence.

### 5. Hybrid Arbitration
The arbiter combines the available predictions according to its configuration, including the confidence threshold, rule override behaviour, and fallback strategy.

### 6. Final Output
The system returns the selected POS tag for each token along with available confidence and decision information.

---

## 📁 Project Structure

```text
lumarium-hybrid-pos-tagger/
│
├── app.py                       # Streamlit dashboard
├── run_all.py                   # Project workflow runner
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
├── .gitignore                   # Git exclusions
│
├── backend/
│   ├── main.py                  # FastAPI application
│   ├── api/
│   │   ├── analyze.py           # Text analysis endpoints
│   │   ├── guide.py             # Linguistic guide endpoints
│   │   ├── health.py            # Health endpoint
│   │   └── practice.py          # Practice endpoints
│   └── services/
│       └── nlp_service.py       # NLP service integration
│
├── components/
│   ├── grammar_guide_data.py
│   ├── nlp_bridge.py
│   ├── quiz_generator.py
│   └── ui_styles.py
│
├── frontend/
│   ├── index.html
│   ├── css/
│   └── js/
│
├── data/
│   ├── train.json
│   ├── dev.json
│   └── test.json
│
├── models/
│   ├── arbiter.json
│   ├── hmm.npz
│   ├── rules.json
│   ├── transformer_dev.json
│   └── transformer_test.json
│
├── results/
│   ├── metrics.json
│   └── report.md
│
├── tests/
│   ├── test_pipeline.py
│   └── test_new_features.py
│
├── rule_tagger.py
├── hmm_tagger.py
├── transformer_tagger.py
├── ensemble.py
├── train.py
├── evaluate.py
├── pipeline.py
├── data_prep.py
├── get_data.py
├── metrics.py
├── tagset.py
├── text_utils.py
├── morphology.py
├── language_identifier.py
├── english_validation.py
├── ner.py
└── translate.py
```

*The structure above highlights the main application, model, data, and evaluation files. Some supporting files and directories have been omitted for readability.*

---

## 🚀 Installation and Quick Start

### Prerequisites

- Python 3.10 or newer
- Git
- Internet access for downloading dependencies and the pretrained transformer, when required

### 1. Clone the Repository

After the repository is published, run:

```bash
git clone https://github.com/YOUR-USERNAME/lumarium-hybrid-pos-tagger.git
cd lumarium-hybrid-pos-tagger
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a Virtual Environment

**Windows — PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

The transformer component requires PyTorch and Hugging Face Transformers. If installation fails because of your hardware or Python environment, consult the official installation instructions for [PyTorch](https://pytorch.org/get-started/locally/) and [Transformers](https://huggingface.co/docs/transformers/installation).

### 4. Launch the FastAPI Web Application

Run:

```bash
uvicorn backend.main:app --reload --port 8001
```

Open the following address in your browser:

```text
http://localhost:8001
```

### 5. Launch the Streamlit Dashboard

Alternatively, open another terminal in the project directory and run:

```bash
streamlit run app.py
```

Streamlit will display the local URL for the dashboard in the terminal.

**Note:** The FastAPI application and Streamlit dashboard are separate entry points. Use the one you want to explore.

---

## 🧪 Training and Evaluation

The repository includes scripts for data preparation, model training, arbitration tuning, and evaluation.

### Prepare the Dataset

If you need to obtain the dataset:

```bash
python get_data.py
```

Then prepare the training and validation data:

```bash
python data_prep.py --train pos_hineng_train.csv --test pos_hineng_validation.csv
```

The validation split is used as the labelled evaluation split in this project. The official LinCE test split may not contain publicly available gold labels.

### Train the Models

Run:

```bash
python train.py
```

The training script calibrates the rule-based tagger, trains the HMM, obtains transformer predictions when enabled, and tunes the arbiter on the development data.

For rule-based and HMM training without the transformer:

```bash
python train.py --no-transformer
```

### Evaluate the Models

Run:

```bash
python evaluate.py
```

The evaluation script generates model comparison results and writes the report to:

```text
results/report.md
```

The numerical metrics are also stored in:

```text
results/metrics.json
```

### Run the Project Workflow

The repository also includes a workflow runner:

```bash
python run_all.py
```

Review the script and ensure the required data and dependencies are available before using it to execute the full workflow.

### Run Tests

Run:

```bash
python -m pytest -q
```

The test suite covers selected pipeline and feature behaviour. Test results may depend on the installed dependencies and available model artifacts.

---

## 📚 Dataset

The primary benchmark used for quantitative evaluation is the **Hindi-English POS dataset from LinCE**, a benchmark for language identification and linguistic analysis of code-switched text.

Dataset information:

- **Dataset:** LinCE Hindi-English POS (`pos_hineng`)
- **Task:** Part-of-Speech tagging
- **Evaluation language pair:** Hindi-English
- **Reported evaluation size:** 160 sentences and 3,476 tokens

Dataset resources:

- [LinCE Benchmark](https://twinlince.org/)
- [LinCE Dataset on Hugging Face](https://huggingface.co/datasets/lince-benchmark/lince)

Please consult the dataset's official terms and attribution requirements before redistributing dataset files.

The project also explores Marathi-English morphological patterns. The reported quantitative results, however, are based on the Hindi-English evaluation and should not be generalized to Marathi-English without a separate labelled evaluation.

---

## ⚠️ Limitations and Future Improvements

Potential directions for further development include:

- **Marathi-English Evaluation:** Build a labelled Marathi-English evaluation set and measure performance independently.
- **Larger Datasets:** Evaluate the system on larger and more diverse code-mixed datasets.
- **Error Analysis:** Investigate frequent confusions among nouns, verbs, adjectives, and proper nouns.
- **Model Comparison:** Compare additional transformer architectures and contextual embedding approaches.
- **HMM Improvements:** Explore alternative transition models and smoothing configurations.
- **Robustness Testing:** Evaluate performance on spelling variations, unseen words, informal text, and different transliteration styles.
- **Reproducibility:** Document the exact training configuration, data splits, model versions, and evaluation procedure.

### Evaluation Considerations

The reported metrics describe performance on the evaluation data included in the project report. They do not establish performance on every domain, language pair, or real-world conversational setting.

---

## 📖 References

1. **LinCE Benchmark:** Linguistic Code-switching Evaluation benchmark.  
   https://twinlince.org/

2. **LinCE Dataset:** Hindi-English POS dataset and related resources.  
   https://huggingface.co/datasets/lince-benchmark/lince

3. **Hugging Face Transformers Documentation:**  
   https://huggingface.co/docs/transformers/

4. **PyTorch Documentation:**  
   https://pytorch.org/docs/

---

## 👩‍💻 About the Project

**Lumarium** explores hybrid NLP system design by combining explicit linguistic rules, probabilistic sequence modelling, contextual transformer predictions, and confidence-based arbitration.

The project focuses on making POS tagging for code-mixed text more adaptable and easier to investigate through model comparisons, evaluation metrics, and an interactive application.