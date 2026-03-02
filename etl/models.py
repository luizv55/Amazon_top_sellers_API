import pandas as pd
from app.load import Livros, engine
from sqlmodel import Session

# Carrega os dados
df = pd.read_excel('parciais2.xlsx')


# Ingestao
with Session(engine) as session:
    for _, row in df.iterrows():
        livro_dados = Livros(**row.to_dict())
        session.add(livro_dados)

    session.commit()