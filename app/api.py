from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from typing import List

from app.load import Livros, engine 

app = FastAPI()


def get_session():
    with Session(engine) as session:
        yield session

@app.get("/")
def home():
    return {"mensagem": "API de Livros Online"}

# Rota para carregar os dados do banco de dados
@app.get("/livros", response_model=List[Livros])
def listar_livros(session: Session = Depends(get_session)):
    # Puxa todos os registros da tabela 'Livros'
    statement = select(Livros)
    resultados = session.exec(statement).all()
    return resultados

# Endpoint para carregar cada livro separadamente pelo id
@app.get("/livros/{livro_id}", response_model=Livros)
def buscar_livro_por_id(livro_id: int, session: Session = Depends(get_session)):
    # O método .get() do SQLModel busca diretamente pelo ID
    livro = session.get(Livros, livro_id)
    
    # Se o ID não existir no banco, retornamos um erro 404
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
        
    return livro