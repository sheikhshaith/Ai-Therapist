# AI Therapist

An AI-powered therapeutic conversation assistant built with Streamlit and OpenAI.

## ⚠️ Important Disclaimer

**This application is for educational and demonstration purposes only.**

- This is NOT a replacement for professional mental health treatment
- It does not provide medical advice, diagnosis, or treatment
- If you're experiencing mental health crisis, please contact:
  - Emergency services (911 in US)
  - National Suicide Prevention Lifeline: 988
  - Crisis Text Line: Text HOME to 741741
- Always consult with qualified healthcare professionals for serious mental health concerns

## Installation

1. **Clone the repository:**
```bash
git clone <repository-url>
cd AI-Therapist
```

2. **Create virtual environment:**
```bash
python -m venv venv
```

3. **Activate virtual environment:**
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

4. **Install dependencies:**
```bash
pip install -r requirements.txt
```

5. **Set up environment variables:**
Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your-actual-api-key-here
```

## Usage

Run the application:
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Requirements

- Python 3.7+
- OpenAI API key (get from https://platform.openai.com/account/api-keys)
- Dependencies listed in `requirements.txt`

## Environment Setup

1. Get your OpenAI API key from https://platform.openai.com/account/api-keys
2. Create a `.env` file in the project root
3. Add your API key: `OPENAI_API_KEY=your-actual-api-key-here`
4. **Never commit your `.env` file to version control**

## Features

- AI-powered conversational interface
- Therapeutic conversation patterns
- Streamlit web interface
- Session management

## Ethical Considerations

- This tool should complement, not replace, professional therapy
- Users should be aware of the limitations of AI in mental health contexts
- Privacy and data security should be prioritized
- Clear boundaries should be maintained about the AI's capabilities

## Project Structure

```
AI-Therapist/
├── app.py          # Main application file
├── .env            # Environment variables (not committed)
├── requirements.txt # Project dependencies
└── README.md       # This file
```

## Support Resources

If you need immediate help:
- **US Crisis Hotline**: 988
- **Crisis Text Line**: Text HOME to 741741
- **International**: Visit https://findahelpline.com