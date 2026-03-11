# Projeto API: Scrapping de livros mais vendidos na Amazon Brasil

### Índice

1.  [Visão geral do projeto](#1-Visão-geral-do-projeto)
      * [API em Produção](#API-em-Produção)
      * [Arquitetura](#Arquitetura)
2.  [Utilização da API](#2-Utilização-da-API)
      * [Execução local](#Execução-local)
3.  [Documentação das Endpoints](#3-Documentação-das-Endpoints)
4.  [Exemplos](#4-Exemplos)

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
Para utilizarmos os dados de tdos os livros da API dentro do nosso ambiente local, execute os seguintes passos:

```bash
import requests

url = "https://api.exemplo.com/produtos](https://amazon-top-sellers-api-5.onrender.com/livros"

response = requests.get(url)

data = response.json()

print(data)
```
Se desejar utilizar o scrapper, é necessario instalar as dependencias do Playwright e executar o script `etl/extract.py`, isso vai resultar em um arquivo .xlsx com nome de parciais no seu caminho de usuário.

## 3\. Documentação das Endpoints
A documentação interativva para as rotas está disponivel https://amazon-top-sellers-api-5.onrender.com/docs/  
Abaixo está a descrição das rotas

### Status
* GET /api/v1/health

### Livros
* GET /api/v1/livros
* GET /API/v1/livros/'Ranking do livro'

## 4\. Exemplos
### Buscar todos os livros
* **Resquest:**
```bash
GET https://amazon-top-sellers-api-5.onrender.com/livros
```
* **Response(exemplo)**
  ```bash
  {
  "id":1,
  "Autor":"Antoine de Saint-Exupéry",
  "Nota":4.8,
  "Ranking":1,
  "Preço":"R$ 14,02",
  "Titulo":"O Pequeno Príncipe - Edição de Luxo Almofadada",
  "Qtd_Avaliacoes":17148
  }
  {"id":2,
  "Autor":"Júnior Rostirola",
  "Nota":4.9,"Ranking":2,
  "Preço":"R$ 18,90",
  "Titulo":"Café com Deus Pai 2025: Porções Diárias de Transformação",
  "Qtd_Avaliacoes":8468}
  .
  .
  .
  ```

### Buscar pelo ranking
* **Resquest:**
```bash
GET https://amazon-top-sellers-api-5.onrender.com/livros/55
```
* **Response(exemplo)**
  ```bash
  {"id":55,
  "Autor":"King Books",
  "Nota":4.8,
  "Ranking":55,
  "Preço":"R$ 21,57",
  "Titulo":"Mulheres com Deus - 365 Dias de Fé - Devocional 2026",
  "Qtd_Avaliacoes":200}
  ```

