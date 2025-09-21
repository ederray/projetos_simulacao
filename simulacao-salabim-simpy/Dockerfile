"""Arquivo Dockerfile"""
# imagem python
FROM python:3.11-slim-bookworm

# diretorio de trabalho no container
WORKDIR /app

# instalação do poetry
RUN pip install poetry

# cópia dos arquivos de configuração do poetry
COPY pyproject.toml poetry.lock ./

# instalação de dependências do projeto
RUN poetry install --only main --no-interaction --no-ansi

# copia dos arquivos da pasta src para o diretorio do container
COPY ..

# cria uma pasta para salvar os resultados dentro da pasta src
RUN mkdir -p src/data

# execução do ambiente
CMD ["/bin/bash"]