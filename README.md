# Otimização do processo de secagem em planta piloto através da automação e tratamento de dados
Este é o repositorio do trabalho de conclusão de curso desenvolvido por alunos do Instituto Mauá de Tecnologia durante a sua formação em 2023.

## Envolvidos no projeto
Orientador: Armando Zanone

Coorientadora: Kaciane Andreola

Integrantes:
- Gustavo Zamboni do Carmo
- Martin Ropke
- Matheus Raphael Detlinger
- Raphael Marchetti Calciolari

## Contextualização e problema do trabalho
O processo de secagem é crucial em indústrias como a farmacêutica e alimentícia, porém certos equipamentos, como o leito fluidizado, não permitem a medição direta da umidade do material a ser seco, criando um obstáculo a ser estudado.

## Objetivo
O estudo teve como objetivo principal desenvolver um método para medir a umidade no leito fluidizado, usando técnicas de aprendizado de máquina para prever os valores sem intervir no processo.

## Coleta de dados
Devido à dificuldade de obtenção de dados através de colaboradores, houve a necessidade de realizar a coleta de dados em laboratório. Experimentos foram conduzidos com celulose microcristalina, coletando dados de variáveis mensuráveis a cada quinze minutos, juntamente com a umidade real medida por um analisador especializado.

## Análise dos dados e treinamento dos modelos
Os dados foram usados em conjunto com técnicas computacionais para criar uma lógica de determinação da umidade, treinando modelos de aprendizado de máquina disponíveis na biblioteca scikit learn do Python.

## Seleção do melhor modelo e conclusões
A seleção dos modelos se baseou no desempenho, com vários modelos alcançando resultados satisfatórios, sendo o melhor deles o modelo de Ridge com um score de 96,52% na previsão da umidade. Isso permitiu a criação de um método para prever a umidade usando outras variáveis em tempo real durante o processo de secagem no leito fluidizado.

A pesquisa não apenas ofereceu um método preciso para medir a umidade durante a secagem nesse tipo de equipamento, mas também destacou a eficácia das técnicas computacionais, como o aprendizado de máquina, na resolução de desafios específicos para engenheiros químicos ou computacionais.

# Sobre o repositório

## Estrutura de diretórios

O repositório deste projeto está estruturado como o modelo a seguir:

| Arquivo / Diretório                    | Conteúdos                                              |
| -------------------------------------- | ------------------------------------------------------- |
| `data/`                              | Todos os dados coletados durante os ensaios em laboratório |
| `scripts/`                                | Scripts em python utilizados para o treinamento dos modelos |

## Rodar o projeto
### No Windows
1. Abra uma nova instância do cmd
2. execute o seguinte comando, substituindo `<environment_path>` pelo diretório onde você deseja armazenar o seu ambiente virtual.
    ```
    python -m venv <environment_path>
    ```
3. acesse `<environment_path>/Scripts` e execute `activate`. 
    ```
    cd <environment_path>/Scripts
    activate
    ```
4. Certifique-se de que o seu ambiente foi ativado. O nome da pasta onde o seu ambiente virtual está armazenado deve aparecer do lado esquerda da linha do cmd.

5. retorne ao diretório raiz do projeto, substitua `<your_git_repo>` pelo caminho do seu repositório
    ```
    cd <your_git_repo>/projects-tcc-imt-2023
    ```
5. execute o seguinte comando para instalar as dependências 
    ```
    pip install -r .\requirements.txt
    ```
