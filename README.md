# PrivacySQL 

PrivacySQL is a local Text-to-SQL tool designed with **data privacy** in mind. It allows users to query a database using natural language without sending any actual data to the LLM.

## How it works
1. **Schema Extraction:** The app scans the database structure (tables and columns) but ignores the actual data records.
2. **Local AI:** Using **Ollama (Llama 3)**, the app translates your question into SQL based only on the schema.
3. **Local Execution:** The generated SQL is executed locally on your machine.

## Technologies
- **Python** (Core logic)
- **Ollama** (Local LLM)
- **SQLAlchemy** (Database interaction)
- **Streamlit** (Web Interface)

## How to run
1. Install requirements: `pip install -r requirements.txt`
2. Ensure Ollama is running (`ollama run llama3`)
3. Start the app: `streamlit run gui.py`
