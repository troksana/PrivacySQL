import streamlit as st
import sqlalchemy
import pandas as pd
from check_schema import get_schema_for_ai
from ai_engine import ask_ai_for_sql

# Konfiguracja strony
st.set_page_config(page_title="PrivacySQL", page_icon="🤖")

st.title("🤖 PrivacySQL \n(Privacy-Preserving SQL-Talker)")
st.markdown("""
Zadaj pytanie swojej bazie danych w języku naturalnym. 
Dane są bezpieczne – AI widzi tylko strukturę tabel!
""")

# Połączenie z bazą
engine = sqlalchemy.create_engine("sqlite:///chinook.db")

# Pobieramy schemat raz
schema = get_schema_for_ai()

# Pole do wpisywania pytania
user_question = st.text_input("O co chcesz zapytać?", placeholder="np. Kto wydał najwięcej pieniędzy?")

if user_question:
    with st.spinner("AI analizuje schemat i generuje zapytanie..."):
        try:
            # 1. Generowanie SQL
            sql_query = ask_ai_for_sql(user_question, schema)
            
            # Pokazujemy wygenerowany SQL w rozwijanym menu (dla debugowania)
            with st.expander("Zobacz wygenerowany kod SQL"):
                st.code(sql_query, language="sql")
            
            # 2. Wykonanie zapytania
            with engine.connect() as connection:
                df = pd.read_sql(sql_query, connection)
            
            # 3. Wyświetlanie wyników
            if df.empty:
                st.warning("Baza danych nie zwróciła żadnych wyników dla tego zapytania.")
            else:
                st.success("Znaleziono wyniki:")
                st.dataframe(df, use_container_width=True) # Ładna, interaktywna tabela
                
        except Exception as e:
            st.error("⚠️ Przepraszam, nie mogłam przetworzyć tego zapytania.")
            st.info(f"Szczegóły błędu: {e}")
            st.write("Spróbuj sformułować pytanie inaczej.")

# Stopka
st.divider()
st.caption("Projekt PrivacySQL with Schema Privacy | Powered by Ollama")