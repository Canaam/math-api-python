# API RESTful de Operações Matemáticas

## Descrição
API RESTful para somar e calcular a média de vetores de inteiros.

## Requisitos
- Python 3.x
- Flask
- Flask-Swagger-UI

## Instalação

1.  Clone o repositório:
    ```
    git clone <URL do repositório>
    ```

2.  Navegue até o diretório do projeto:
    ```
    cd <nome do diretório>
    ```

3.  (Opcional) Crie um ambiente virtual (recomendado para isolar as dependências do projeto):
    ```
    python3 -m venv venv
    ```

4.  (Se você criou um ambiente virtual) Ative o ambiente virtual:
    *   No Linux/macOS:
        ```
        source venv/bin/activate
        ```
    *   No Windows:
        ```
        .\venv\Scripts\activate
        ```

5.  Instale as dependências:
    ```
    pip install -r requirements.txt
    ```

## Execução

1.  Execute a aplicação:
    ```
    python run.py
    ```

2.  A API estará disponível em `http://0.0.0.0:5000/`.

## Documentação

A documentação da API está disponível em `http://0.0.0.0:5000/swagger`. A documentação segue o padrão OpenAPI (Swagger).

## Testes

Para executar os testes unitários, execute o seguinte comando:

python -m unittest discover -p "test*.py" -s tests

Os testes unitários cobrem as classes `Number` e `Numbers` da biblioteca principal.

## Estrutura do Código

O código está organizado da seguinte forma:

-   `app/`: Contém o código da aplicação.
    -   `models/`: Define as classes de modelo (`Number` e `Numbers`).
    -   `routes/`: Define as rotas da API (endpoints).
    -   `services/`: Contém a lógica de negócios da aplicação.
    -   `app.py`: Inicializa e configura a aplicação Flask.
-   `tests/`: Contém os testes unitários.
    -   `test_api.py`: Testes para os endpoints da API.
    -   `test_numbers.py`: Testes para as classes `Number` e `Numbers`.
-   `run.py`: Script para executar a aplicação.
-   `requirements.txt`: Lista as dependências do projeto.

## Modelo RESTful

A API foi desenvolvida utilizando os princípios RESTful:

-   Uso de métodos HTTP (POST) para operações.
-   Troca de dados no formato JSON.
-   Endpoints bem definidos para cada operação (/sum e /average).

## Observações Adicionais

-   O projeto foi desenvolvido com foco na organização do código, seguindo as boas práticas de engenharia de software.
-   A documentação da API está disponível através do Swagger UI, facilitando a compreensão e o uso da API.
-   Os testes unitários garantem o correto funcionamento das operações matemáticas e a robustez da API.

### Principais Ajustes e Validações:

*   **Ambiente Virtual Opcional:** Deixei claro que a criação de um ambiente virtual é opcional, mas recomendada.
*   **Condicional para Ativação do Ambiente Virtual:** Adicionei uma nota indicando que a ativação do ambiente virtual só é necessária se você o criou.
*   **Estrutura do Código:** Adicionei uma seção detalhando a estrutura do código, incluindo a descrição de cada diretório e arquivo.
*   **Modelo RESTful:** Adicionei uma seção explicando como os princípios RESTful foram aplicados no desenvolvimento da API.
*   **Observações Adicionais:** Incluí algumas observações adicionais para destacar os pontos fortes do projeto.

Com essas adições, o `README.md` agora cobre todos os requisitos do PDF de forma clara e concisa.




