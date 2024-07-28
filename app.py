import os
import openai
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# --- Load environment variables from .env file ---
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    st.error("❌ OPENAI_API_KEY not found. Please set it in your .env file.")
    st.stop()

# --- Configure OpenAI Client ---
openai_client = OpenAI(api_key=OPENAI_API_KEY)

# --- Function to query OpenAI ---
def query_openai_api(prompt):
    try:
        messages = [{"role": "user", "content": prompt}]
        response = openai_client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.7,
            max_tokens=1000
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        st.error(f"Error querying OpenAI API: {e}")
        return ""

# --- Streamlit UI ---
st.set_page_config(page_title="AI Therapy or Coaching Companion", layout="wide")
st.title("🧠 AI Therapy & Coaching Companion Bot")

# Mood input
st.subheader("Your Current Mood")
current_mood = st.radio("How are you feeling right now?", ["Happy", "Sad", "Anxious", "Angry", "Neutral", "Excited", "Tired"])

# User input for journaling
st.subheader("What's on your mind?")
user_input = st.text_area("Write about your feelings or anything you'd like to reflect on...")

# Button to submit the journal entry
if st.button("Submit Entry"):
    if user_input.strip():
        combined_prompt = f"The user is currently feeling {current_mood}. Based on their mood and the following thoughts: '{user_input}', provide therapeutic support, validation, and gentle coaching tailored to their emotional state."
        ai_feedback = query_openai_api(combined_prompt)

        st.subheader("📝 AI Therapy & Coaching Feedback")
        st.write(ai_feedback)

        st.subheader("🌟 Mood Summary")
        st.write(f"You reported feeling: {current_mood}")

        st.success("Thank you for sharing your thoughts! You're doing a great job taking care of yourself.")
    else:
        st.warning("Please write something in the journal entry.")
