import ollama

def ask_ai_for_sql(user_question, schema):
    prompt = f"""
    Jesteś ekspertem SQL. Twoim zadaniem jest przygotowanie zapytania SQL dla bazy SQLite.
    
    Oto schemat bazy danych:
    {schema}
    
    Pytanie użytkownika: {user_question}
    
    Zwróć TYLKO czysty kod SQL, bez żadnych wyjaśnień, bez znaczników ```sql.
    """
    
    response = ollama.chat(model='llama3', messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])
    
    return response['message']['content'].strip()

#TEST
if __name__ == "__main__":
    test_schema = "Tabela: Track, Kolumny: Name, UnitPrice"
    test_question = "Pokaż mi 5 najdroższych utworów"
    
    print("Czekam na odpowiedź od lokalnej Ollamy...")
    sql = ask_ai_for_sql(test_question, test_schema)
    print("\nAI wygenerowało taki SQL:")
    print(sql)