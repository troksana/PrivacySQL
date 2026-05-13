import sqlalchemy
import pandas as pd #ułatwi nam wyświetlanie wyników w tabelce
from check_schema import get_schema_for_ai 
from ai_engine import ask_ai_for_sql

#Połączenie z bazą
engine = sqlalchemy.create_engine("sqlite:///chinook.db")

def main():
    print("--- Witaj w SQL-Talker z Ollamą! ---")
    
    #Pobieranie prawdziwy schemat z skryptu
    schema = get_schema_for_ai()
    
    user_question = input("\nO co chcesz zapytać bazę danych? ")
    
    if user_question:
        print("\n[1/2] AI myśli nad zapytaniem SQL...")
        sql_query = ask_ai_for_sql(user_question, schema)
        
        print(f" Wygenerowany SQL: {sql_query}")
        print("\n[2/2] Wykonuję zapytanie i pobieram dane...")
        
        try:
            #Używamy pandas, żeby ładnie wyświetlić wynik
            with engine.connect() as connection:
                df = pd.read_sql(sql_query, connection)
                
            if df.empty:
                print("Baza nie zwróciła żadnych wyników.")
            else:
                print("\n--- WYNIKI ---")
                print(df)
                
        except Exception as e:
            print(f"Błąd podczas wykonywania SQL: {e}")

if __name__ == "__main__":
    main()