# SMS Spam Detection using NLP

An end-to-end NLP classification project that predicts whether an SMS message is **Spam** or **Ham (legitimate)**. The text-processing and classification steps are bundled into a saved Scikit-learn pipeline and served through an interactive Streamlit app.

## Application Screenshots

### Streamlit application interface
![SMS Spam Detector interface](Interface/SMS%20Interface.png)

### Spam message prediction
![SMS Spam Detector - Spam prediction](Interface/Prediction%201.webp)

### Ham (legitimate) message prediction
![SMS Spam Detector - Ham prediction](Interface/Prediciton%202.png)

The screenshots demonstrate the app interface and example classifications for one spam-style promotional message and one ordinary conversational message. These are sample demonstrations; model predictions can be incorrect.

## Features

- Interactive SMS classification app built with Streamlit.
- TF-IDF text representation using unigrams and bigrams.
- Multinomial Naive Bayes classifier.
- Saved preprocessing and model pipeline (`model.pkl`).
- Training and evaluation notebook.
- Dataset, evaluation plots, testing report, and application screenshots.

## Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- TF-IDF
- Multinomial Naive Bayes
- Streamlit
- Matplotlib

## Repository Structure

```
SMS-Spam-Detection-NLP/
├── Interface/
│   ├── SMS Interface.png
│   ├── Prediction 1.webp
│   └── Prediciton 2.png
├── .streamlit/
│   └── config.toml
├── app.py
├── model.pkl
├── spam.tsv
├── requirements.txt
├── SMS_Spam_Training_Evaluation.ipynb
├── confusion_matrix.png
├── label_distribution.png
├── TESTING_REPORT.md
└── README.md
```

## Run Locally

1. Clone this repository and enter the folder:

   ```bash
   git clone https://github.com/jeetpatilprofessional-blip/SMS-Spam-Detection-NLP.git
   cd SMS-Spam-Detection-NLP
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv .venv
   ```

   **Windows PowerShell:**

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

   **macOS/Linux:**

   ```bash
   source .venv/bin/activate
   ```

3. Install the requirements:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:

   ```bash
   streamlit run app.py
   ```

## Deploy on Streamlit Community Cloud

1. Visit [Streamlit Community Cloud](https://share.streamlit.io/) and sign in with GitHub.
2. Click **Create app**.
3. Select this repository: `jeetpatilprofessional-blip/SMS-Spam-Detection-NLP`.
4. Choose branch `main` and entrypoint file `app.py`.
5. Click **Deploy** and wait for the build to finish.

The app uses `requirements.txt` and the included `model.pkl`. No secrets are required.

## Model Training

The `SMS_Spam_Training_Evaluation.ipynb` notebook contains the reproducible training workflow:

1. Load the TSV dataset.
2. Clean and retain valid `ham`/`spam` labels and message text.
3. Explore label distribution.
4. Split the data into stratified training and test sets (80/20).
5. Extract TF-IDF unigram and bigram features.
6. Train a Multinomial Naive Bayes classifier.
7. Evaluate the model and plot the confusion matrix.
8. Save the complete pipeline as `model.pkl`.

The dataset is included. The notebook expects the fields `label` and `message`; additional columns are ignored.

## Reported Evaluation

The documented held-out test run reported:

| Metric | Result |
|---|---:|
| Accuracy | 96.23% |
| Ham F1-score | 97.87% |
| Spam F1-score | 83.59% |
| Spam recall | 71.81% |

More metrics and smoke-test notes are in [TESTING_REPORT.md](TESTING_REPORT.md). The relatively lower spam recall means some spam messages may be classified as legitimate. Metrics are run-specific, not a guarantee of future performance.

## Limitations

- The model may miss spam messages or incorrectly flag legitimate messages.
- This is a learning/demo project, not a production spam-filtering service.
- Only load pickle model files from trusted sources; pickle files can execute code during loading.

## Author

**Jeet Patil** — [GitHub profile](https://github.com/jeetpatilprofessional-blip)
