import streamlit as st
import pickle
import numpy as np

# =========================
# Load Model & Vectorizer
# =========================
@st.cache_resource
def load_resources():
    try:
        with open("logistic_regression_model.pkl", "rb") as model_file:
            model = pickle.load(model_file)

        with open("tfidf_vectorizer.pkl", "rb") as vectorizer_file:
            vectorizer = pickle.load(vectorizer_file)

        return model, vectorizer

    except FileNotFoundError:
        st.error("Model or Vectorizer file not found!")
        st.stop()

    except Exception as e:
        st.error(f"Error loading files: {e}")
        st.stop()


model, vectorizer = load_resources()

# =========================
# Streamlit UI
# =========================
st.title("SMS Spam Classifier")
st.write("Enter a message to classify it as Spam or Ham.")

user_input = st.text_area("Enter your message:")

# =========================
# Prediction
# =========================
if st.button("Classify"):

    if not user_input.strip():
        st.warning("Please enter a message.")
    else:

        try:
            # Transform input text
            input_vectorized = vectorizer.transform([user_input]).toarray()

            # Debug info
            #st.write("Input Shape:", input_vectorized.shape)

            # Prediction
            prediction = model.predict(input_vectorized)[0]

            # Output
            if prediction == 0:
                st.error("🚨 This message is SPAM")
            else:
                st.success("✅ This message is HAM")

        except Exception as e:
            st.error(f"Prediction Error: {e}")