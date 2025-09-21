# Simulação de Eventos Discretos

Este repositório contém exemplos de simulação de eventos discretos (DES) com as bibliotecas Python **Salabim** e **Simpy**. O objetivo é demonstrar cenários de processos logísticos e de Supply Chain em ambas as libs, explorando cenários e análise de métricas de performance em modelos de simulação discreta.

---

## Cenários

1.  Fila de caminhões em uma doca
2.  Operadores em um armazém
3.  Esteira de inspeção
4.  Cross-docking com filas paralelas
5.  Separação de pedidos com políticas diferentes
6.  Centro de distribuição com gargalo
7.  Rede de transporte com incerteza
8.  Política de reabastecimento (supply chain)
9.  Simulação integrada logística + produção

---

## Tecnologias Utilizadas

Este projeto utiliza um conjunto de bibliotecas e ferramentas para simulação, análise e visualização de dados:

* **Salabim & Simpy**: Ferramentas principais para a construção dos modelos de simulação de eventos discretos.
* **Pandas**: Manipulação e análise de dados tabulares.
* **NumPy**: Cálculos numéricos e operações com arrays.
* **Matplotlib & Seaborn**: Geração de gráficos estáticos para visualização de resultados.
* **Plotly**: Geração de gráficos interativos.
* **SciPy & Statsmodels**: Análise estatística e modelagem de dados.

---

## Estrutura do Projeto

A estrutura de pastas e arquivos está organizada da seguinte forma:

```

.
├── src/
│   ├── data/
│   ├── features/
│   ├── visualize/
│   └── utils/
├── notebooks/
├── .gitignore
├── Dockerfile
├── requirements.txt
└── pyproject.toml

````

---

## Configuração do Ambiente

### 1. Clonar o Repositório

Primeiro, clone este repositório para sua máquina local usando o Git:

```bash
git clone [https://github.com/ederray/projetos_simulacao/simulacao-salabim-simpy.git](https://github.com/ederray/projetos_simulacao/simulacao-salabim-simpy.git)
````

### 2\. Requisitos

Certifique-se de que você tem o Python **3.11.9** ou superior e o **Poetry** instalados em sua máquina.

### 3\. Instalação das Dependências

Você pode instalar as dependências de três maneiras:

#### Opção A: Com Poetry (Recomendado)

O Poetry é a ferramenta de gerenciamento de dependências utilizada no projeto. Navegue até o diretório raiz e execute:

```bash
poetry install
```

#### Opção B: Com `requirements.txt`

Se você preferir usar `pip`, use o arquivo `requirements.txt`. Para manter a lista de dependências sincronizada, gere o arquivo primeiro:

```bash
poetry export -f requirements.txt --output requirements.txt --without-hashes
```

Em seguida, instale as dependências:

```bash
pip install -r requirements.txt
```

#### Opção C: Com Docker

Se você prefere um ambiente isolado, use o Docker.

1.  **Construa a imagem Docker**:

    ```bash
    docker build -t simulacao-des .
    ```

2.  **Execute um contêiner**:

    ```bash
    docker run -it --rm simulacao-des bash
    ```

    Isso iniciará o contêiner e abrirá um terminal dentro dele, onde você pode executar os scripts de simulação.

-----

## Licença

Este projeto é licenciado sob a licença **MIT**.

```
```