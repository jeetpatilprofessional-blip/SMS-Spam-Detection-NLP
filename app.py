import pickle
from pathlib import Path

import streamlit as st

st.set_page_config(page_title="SMS Spam Detector", page_icon="📩", layout="centered")

MODEL_PATH = Path(__file__).parent / "model.pkl"


@st.cache_resource
def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError("model.pkl was not found in the project folder.")
    with MODEL_PATH.open("rb") as file:
        return pickle.load(file)


st.title("📩 SMS Spam Detector")
st.write("Check whether an SMS message is likely to be **Spam** or **Ham (legitimate)**.")
st.divider()

message = st.text_area(
    "SMS message",
    placeholder="Paste or type your message here...",
    height=150,
)

if st.button("Predict Message", type="primary", use_container_width=True):
    if not message.strip():
        st.warning("Please enter a message before predicting.")
    else:
        try:
            model = load_model()
            prediction = str(model.predict([message.strip()])[0]).strip().lower()

            if prediction == "spam":
                st.error("🚨 This message is predicted to be SPAM.")
            elif prediction == "ham":
                st.success("✅ This message is predicted to be HAM (legitimate).")
            else:
                st.warning(f"The model returned an unexpected label: {prediction}")
        except FileNotFoundError as error:
            st.error(str(error) + " Please add the trained model file.")
        except Exception:
            st.error(
                "Prediction failed. The model may be incompatible with the installed "
                "scikit-learn version or the model file may be invalid."
            )

st.caption("Machine-learning predictions can be incorrect. Treat suspicious messages cautiously.")
