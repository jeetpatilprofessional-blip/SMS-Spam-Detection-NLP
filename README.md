# SMS Spam Detection using NLP

An NLP-based SMS classification application that predicts whether a text message is **Spam** or **Ham (legitimate)** using a TF-IDF and machine-learning pipeline served through Streamlit.

## Features
- Classifies messages as Spam or Ham
- Streamlit interactive app
- Saved preprocessing + model pipeline (`model.pkl`)
- Training and evaluation notebook provided

## Tech Stack
Python • Streamlit • Scikit-learn • Pandas • NumPy • TF-IDF

## Project Structure
```
SMS-Spam-Detection-NLP/
├── app.py
├── model.pkl
├── requirements.txt
├── SMS_Spam_Training_Evaluation.ipynb
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
The notebook `SMS_Spam_Training_Evaluation.ipynb` demonstrates loading and cleaning data, exploring label distribution, train/test splitting, TF-IDF vectorization, Multinomial Naive Bayes training, metrics and confusion-matrix plotting, and saving the complete pipeline as `model.pkl`.

**Dataset prerequisite:** Place the tab-separated file `spam.tsv` (containing `label` and `message` columns) beside the notebook. The notebook uses `pd.read_csv('spam.tsv', sep='\\t')`. The dataset is not included in this repository.

Run every notebook cell to generate a new `model.pkl`. The notebook's pipeline is designed to accept raw message strings, matching the app's prediction call.

## Evaluation
Run the notebook to produce your own Accuracy, Precision, Recall, F1-score and confusion matrix. No results are published here until the notebook has been executed.

## Screenshots
Screenshots of the Streamlit application and evaluation results are not yet included.

## Limitations
This model may misclassify messages. Do not rely on its predictions for sensitive or consequential decisions. Only load pickle model files from trusted sources.
