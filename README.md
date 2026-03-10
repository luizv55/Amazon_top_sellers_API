# Projeto API: Scrapping de livros mais vendidos na Amazon Brasil

### Índice


-----
## 1\. Visão geral do projeto

### Descrição
Este projeto desenvolve uma solução integrada para extração, ingestão e consulta de dados dos 100 livros mais vendidos pela Amazon Brasil, utilizando um scrapper com uma API REST e armazenando os dados em um banco de dados SQLite.

- **Web Scraper** (`etl/extract.py`) utiliza playwright para extrair dados sobre livros da Amazon dos 100 livros mais vendidos e guarda em um excel.
- **API** (`app/api.py`): Desenvolvida com FastAPI, possuindo alguns endpoints. A API inclui funcionalidades de pesquisa de livro por ranking e a geração de todos os 100 livros.

O projeto também possui o algoritmo de ingestão de dados em um banco de dados SQLite.

## API em Produção

A API está implantada e disponível em:  
**[https://amazon-top-sellers-api-5.onrender.com/](https://amazon-top-sellers-api-5.onrender.com/)**

A documentação pode ser acessada em:  
**https://amazon-top-sellers-api-5.onrender.com/docs**

### Arquitetura
<img width="1158" height="471" alt="esquema de dados" src="https://github.com/user-attachments/assets/4101b805-1e45-46b4-b6a6-b854cd154c6a" />

  * **/app**: Contém a lógica da API e a ingestão no banco de dados.
  * **/etl**: Contém o algoritmo de scrapping com a limpeza dos dados.
## 2\. Utilização da API
### 2\.1 Utilização pela documentação
É possivel explorar os dados pela propria documetação da API de forma interativa.  
Acesse o link da documentação no navegador e consulte o endpoint que desejar e clique em executar.  

### 2\.2 Execução local

