from sqlmodel import SQLModel, create_engine, Field

class Livros(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    Ranking: int  
    Titulo: str
    Autor: str
    Preço: str
    Nota: float
    Qtd_Avaliacoes: int

sqlite_file_name = 'database.db'
connection_string = f'sqlite:///{sqlite_file_name}'

engine = create_engine(connection_string, echo=True)

if __name__ == '__main__':
    SQLModel.metadata.create_all(engine)

