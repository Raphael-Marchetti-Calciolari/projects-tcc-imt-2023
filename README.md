# projects-tcc-imt-2023
Repositorio para modelos e dados referentes ao trabalho de conclusão de curso "Otimização do processo de secagem em planta piloto através da automação e tratamento de dados"

# Criando um novo virtual environment

## Para windows
1. Abra uma nova instância do cmd
2. execute o seguinte comando, substituindo **<environment_path>** pelo diretório onde você deseja armazenar o seu ambiente virtual.
    ```
    python -m venv <environment_path>
    ```
3. acesse `<environment_path>/Scripts` e execute `activate`. 
    ```
    cd <environment_path>/Scripts
    activate
    ```
4. Certifique-se de que o seu ambiente foi ativado. O nome da pasta onde o seu ambiente virtual está armazenado deve aparecer do lado esquerda da linha do cmd.

5. retorne ao diretório raiz do projeto
    ```
    cd <your_git_repo>/projects-tcc-imt-2023
    ```
5. execute o seguinte comando para instalar as dependências 
    ```
    pip install -r .\requirements.txt
    ```
