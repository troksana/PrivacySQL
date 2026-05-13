import sqlalchemy
from sqlalchemy import inspect

#Połączenie z bazą
engine = sqlalchemy.create_engine("sqlite:///chinook.db")

def get_schema_for_ai():
    inspector = inspect(engine)
    schema_string = "To jest schemat bazy danych SQLite:\n\n"
    
    tables = inspector.get_table_names()
    
    for table_name in tables:
        schema_string += f"Tabela: {table_name}\n"
        columns = inspector.get_columns(table_name)
        col_names = [f"{c['name']} ({c['type']})" for c in columns]
        schema_string += f"Kolumny: {', '.join(col_names)}\n\n"
        
    return schema_string  #funkcja oddaje gotowy tekst

#Do testowania pliku osobno
if __name__ == "__main__":
    print(get_schema_for_ai())