ARG PYTHON_VERSION=3.10.13
FROM python:${PYTHON_VERSION}-slim as base

# pacote de utilitários
RUN apt-get update && apt-get install -y procps && rm -rf /var/lib/apt/lists/*

# compilador RUST
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# impede que o python escreva arquivos pyc
ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

# copia codigo fonte para o container
COPY . .

# porta de contexao
EXPOSE 8000

# executa a api
CMD ["python", "main.py"]