# Virtual Teaching Assistant (TDS)

This project is a Flask-based API that answers questions about the TDS course using OpenRouter's GPT.

## Features

- Scrapes course content from the IITM TDS portal
- Exposes a simple `/ask?q=your_question` API
- Returns AI-generated answers using context

## Setup Instructions

1. Clone this repo
2. Create a virtual environment and activate it
3. Install dependencies: `pip install -r requirements.txt`
4. Run the app: `python app.py`
