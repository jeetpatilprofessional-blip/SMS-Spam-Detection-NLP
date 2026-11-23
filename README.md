# SMS Spam Detection using NLP

An NLP-based SMS classification application that predicts whether a text message is **Spam** or **Ham (Legitimate)** using a trained machine-learning model and an interactive Streamlit interface.

## Features
- Classifies user-entered SMS messages as Spam or Ham
- Simple interactive interface built with Streamlit
- Uses a saved machine-learning model (`model.pkl`)
- Lightweight deployment and local execution

## Tech Stack
- Python
- Streamlit
- Scikit-learn
- Pickle (model serialization)

## Repository Structure
```
SMS-Spam-Detection-NLP/
├── app.py
├── model.pkl
├── requirements.txt
└── README.md
```

## Run the application locally

1. Clone the repository:
   ```bash
   git clone https://github.com/jeetpatilprofessional-blip/SMS-Spam-Detection-NLP.git
   cd SMS-Spam-Detection-NLP
   ```

2. (Optional but recommended) Create and activate a virtual environment:
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

4. Launch Streamlit:
   ```bash
   streamlit run app.py
   ```

## How it works
1. Enter a message in the text box.
2. Click **Predict**.
3. The saved model classifies the message.
4. The app displays a Spam or Ham result.

## Project Scope & Future Improvements
- Add model evaluation (precision, recall, F1-score and confusion matrix).
- Compare multiple classification algorithms.
- Document preprocessing and model-training workflow in a notebook.
- Add screenshots and a more detailed dataset description.

## Disclaimer
This project is for educational and portfolio purposes. Predictions may be incorrect; do not rely on the classifier for sensitive decisions.
