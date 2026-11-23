# SMS Spam Detection using NLP

An NLP-based SMS classification application that predicts whether a text message is **Spam** or **Ham (legitimate)** using a TF-IDF and machine-learning pipeline served through Streamlit.

## Features
- Classifies messages as Spam or Ham
- Streamlit interactive app
- Saved preprocessing + model pipeline (`model.pkl`)
- Training and evaluation notebook
- Test metrics and testing report

## Tech Stack
Python • Streamlit • Scikit-learn • Pandas • NumPy • TF-IDF

## Project Structure
```
SMS-Spam-Detection-NLP/
├── app.py
├── model.pkl
├── spam.tsv (local dataset; not committed)
├── requirements.txt
├── SMS_Spam_Training_Evaluation.ipynb
├── TESTING_REPORT.md
├── .gitignore
└── README.md
```

## Run the application
1. Clone:
   ```bash
   git clone https://github.com/jeetpatilprofessional-blip/SMS-Spam-Detection-NLP.git
   cd SMS-Spam-Detection-NLP
   ```
2. Create a virtual environment (optional):
   ```bash
   python -m venv venv
   ```
   Windows: `venv\\Scripts\\activate`

   macOS/Linux: `source venv/bin/activate`
3. Install:
   ```bash
   pip install -r requirements.txt
   ```
4. Run:
   ```bash
   streamlit run app.py
   ```

## Train and evaluate
The notebook `SMS_Spam_Training_Evaluation.ipynb` loads `spam.tsv` (tab-separated), cleans the data, explores class distribution, performs a stratified train/test split, trains a TF-IDF + Multinomial Naive Bayes pipeline, evaluates the model, and saves the pipeline as `model.pkl`.

Place `spam.tsv` beside the notebook. The file should contain `label` and `message` columns. The dataset itself is not included in this repository.

## Results from a local run
- **Accuracy:** 96.23%
- **Ham F1-score:** 97.87%
- **Spam F1-score:** 83.59%
- **Spam recall:** 71.81%

See [TESTING_REPORT.md](TESTING_REPORT.md) for the complete report. Spam recall is lower than overall accuracy; the classifier misses some spam messages, so accuracy alone is not sufficient to evaluate it.

## Limitations
This model may misclassify messages. Do not rely on its predictions for sensitive or consequential decisions. Only load pickle model files from trusted sources.
