# SMS Spam Detection using NLP

An end-to-end Natural Language Processing (NLP) project that classifies SMS messages as **Spam** or **Ham (legitimate)** using a TF-IDF vectorizer and Multinomial Naive Bayes model. The trained pipeline is integrated into a simple interactive Streamlit application.

## Features

- Predict whether a message is spam or legitimate
- Interactive web app built with Streamlit
- TF-IDF text feature extraction (unigrams and bigrams)
- Multinomial Naive Bayes classifier
- Saved preprocessing and model pipeline (`model.pkl`)
- Training and evaluation notebook
- Dataset and evaluation visualizations
- Testing report

## Tech Stack

- Python
- Pandas and NumPy
- Scikit-learn
- TF-IDF
- Multinomial Naive Bayes
- Streamlit
- Matplotlib

## Repository Structure

```
SMS-Spam-Detection-NLP/
├── app.py
├── model.pkl
├── spam.tsv
├── requirements.txt
├── SMS_Spam_Training_Evaluation.ipynb
├── Spam Text Classification.ipynb
├── confusion_matrix.png
├── label_distribution.png
├── TESTING_REPORT.md
└── .gitignore
```

## Run the application locally

1. Clone the repository:

   ```bash
   git clone https://github.com/jeetpatilprofessional-blip/SMS-Spam-Detection-NLP.git
   cd SMS-Spam-Detection-NLP
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   ```

   Windows:

   ```bash
   venv\\Scripts\\activate
   ```

   macOS/Linux:

   ```bash
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the app:

   ```bash
   streamlit run app.py
   ```

## Model training and evaluation

The notebook `SMS_Spam_Training_Evaluation.ipynb` provides the model training workflow:

1. Load and clean the tab-separated dataset (`spam.tsv`).
2. Explore the distribution of spam and ham messages.
3. Split the data into training and test sets using stratification.
4. Convert text into TF-IDF features using English stop words and unigram/bigram features.
5. Train a Multinomial Naive Bayes classifier.
6. Evaluate performance and visualize the confusion matrix.
7. Save the trained vectorizer and classifier together as `model.pkl`.

The dataset is included in this repository. The expected columns are `label` and `message`.

## Evaluation results

Results reported for the held-out test split from the documented local run:

| Metric | Result |
|---|---:|
| Accuracy | 96.23% |
| Ham F1-score | 97.87% |
| Spam F1-score | 83.59% |
| Spam recall | 71.81% |

See [TESTING_REPORT.md](TESTING_REPORT.md) for the additional reported metrics and smoke-test notes. Spam recall is lower than overall accuracy, so some spam messages may be missed.

## Visualizations

- `label_distribution.png` — class distribution in the dataset
- `confusion_matrix.png` — model classification results on the test split

## Limitations and safety

The model may incorrectly classify messages. Do not use its predictions as the sole basis for sensitive or consequential decisions. Only load pickle files from trusted sources.

## Author

**Jeet Patil**

[GitHub Profile](https://github.com/jeetpatilprofessional-blip)
