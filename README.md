# API RESTful de Opera��es Matem�ticas

## Descri��o
API RESTful para somar e calcular a m�dia de vetores de inteiros.

## Requisitos
- Python 3.x
- Flask
- Flask-Swagger-UI

## Instala��o

1.  Clone o reposit�rio:
    ```
    git clone <URL do reposit�rio>
    ```

2.  Navegue at� o diret�rio do projeto:
    ```
    cd <nome do diret�rio>
    ```

3.  (Opcional) Crie um ambiente virtual (recomendado para isolar as depend�ncias do projeto):
    ```
    python3 -m venv venv
    ```

4.  (Se voc� criou um ambiente virtual) Ative o ambiente virtual:
    *   No Linux/macOS:
        ```
        source venv/bin/activate
        ```
    *   No Windows:
        ```
        .\venv\Scripts\activate
        ```

5.  Instale as depend�ncias:
    ```
    pip install -r requirements.txt
    ```

## Execu��o

1.  Execute a aplica��o:
    ```
    python run.py
    ```

2.  A API estar� dispon�vel em `http://0.0.0.0:5000/`.

## Documenta��o

A documenta��o da API est� dispon�vel em `http://0.0.0.0:5000/swagger`. A documenta��o segue o padr�o OpenAPI (Swagger).

## Testes

Para executar os testes unit�rios, execute o seguinte comando:

python -m unittest discover -p "test*.py" -s tests

Os testes unit�rios cobrem as classes `Number` e `Numbers` da biblioteca principal.

## Estrutura do C�digo

O c�digo est� organizado da seguinte forma:

-   `app/`: Cont�m o c�digo da aplica��o.
    -   `models/`: Define as classes de modelo (`Number` e `Numbers`).
    -   `routes/`: Define as rotas da API (endpoints).
    -   `services/`: Cont�m a l�gica de neg�cios da aplica��o.
    -   `app.py`: Inicializa e configura a aplica��o Flask.
-   `tests/`: Cont�m os testes unit�rios.
    -   `test_api.py`: Testes para os endpoints da API.
    -   `test_numbers.py`: Testes para as classes `Number` e `Numbers`.
-   `run.py`: Script para executar a aplica��o.
-   `requirements.txt`: Lista as depend�ncias do projeto.

## Modelo RESTful

A API foi desenvolvida utilizando os princ�pios RESTful:

-   Uso de m�todos HTTP (POST) para opera��es.
-   Troca de dados no formato JSON.
-   Endpoints bem definidos para cada opera��o (/sum e /average).

## Observa��es Adicionais

-   O projeto foi desenvolvido com foco na organiza��o do c�digo, seguindo as boas pr�ticas de engenharia de software.
-   A documenta��o da API est� dispon�vel atrav�s do Swagger UI, facilitando a compreens�o e o uso da API.
-   Os testes unit�rios garantem o correto funcionamento das opera��es matem�ticas e a robustez da API.

### Principais Ajustes e Valida��es:

*   **Ambiente Virtual Opcional:** Deixei claro que a cria��o de um ambiente virtual � opcional, mas recomendada.
*   **Condicional para Ativa��o do Ambiente Virtual:** Adicionei uma nota indicando que a ativa��o do ambiente virtual s� � necess�ria se voc� o criou.
*   **Estrutura do C�digo:** Adicionei uma se��o detalhando a estrutura do c�digo, incluindo a descri��o de cada diret�rio e arquivo.
*   **Modelo RESTful:** Adicionei uma se��o explicando como os princ�pios RESTful foram aplicados no desenvolvimento da API.
*   **Observa��es Adicionais:** Inclu� algumas observa��es adicionais para destacar os pontos fortes do projeto.

Com essas adi��es, o `README.md` agora cobre todos os requisitos do PDF de forma clara e concisa.




