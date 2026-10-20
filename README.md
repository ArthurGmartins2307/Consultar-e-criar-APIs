# Python API Studies

Repositório dedicado ao estudo prático de **APIs com Python**, explorando tanto o consumo de APIs existentes quanto o desenvolvimento de APIs próprias.

O objetivo é compreender como aplicações se comunicam, como os dados são transmitidos via HTTP e como essas integrações podem ser utilizadas em projetos reais.

## Objetivos de estudo

- Compreender os fundamentos de APIs, HTTP e JSON.
- Consumir APIs externas utilizando a biblioteca `requests`.
- Realizar requisições HTTP e interpretar suas respostas.
- Extrair, organizar e manipular dados retornados por APIs.
- Desenvolver APIs próprias com Python e FastAPI.
- Explorar endpoints, métodos HTTP, validação de dados e tratamento de erros.
- Aplicar esses conhecimentos em projetos práticos.

## Tecnologias

- **Python** — linguagem utilizada no desenvolvimento.
- **Requests** — consumo de APIs externas.
- **FastAPI** — desenvolvimento de APIs próprias.
- **JSON** — formato de intercâmbio de dados.
- **Git e GitHub** — versionamento e organização dos estudos.

## Projetos e práticas

### Consumo de APIs

Exercícios voltados à integração com serviços externos, realização de requisições e interpretação de respostas JSON.

Um dos exemplos é a consulta de cotações de moedas por meio da [DolarAPI](https://br.dolarapi.com/v1/cotacoes/usd).

### Criação de APIs

Desenvolvimento de APIs com FastAPI, explorando a criação de endpoints, o recebimento de dados, a validação de entradas e o retorno de respostas HTTP.

## Como executar

Clone o repositório e acesse a pasta do projeto:

```bash
git clone URL_DO_REPOSITORIO
cd NOME_DO_REPOSITORIO
```

Crie e ative um ambiente virtual.

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux:**

```bash
python -m venv .venv
source .venv/bin/activate
```

Instale as dependências necessárias para o exercício que deseja executar. Por exemplo:

```bash
python -m pip install requests
```

Para executar um script Python:

```bash
python nome_do_arquivo.py
```

Os comandos e as dependências podem variar conforme o projeto ou exercício.

## Organização

Os arquivos são organizados de acordo com os exercícios e as aplicações desenvolvidas ao longo do aprendizado, mantendo os exemplos independentes e fáceis de consultar.

## Objetivo do repositório

Este repositório faz parte da minha evolução em desenvolvimento de software, com foco na compreensão prática de APIs, integração entre sistemas e desenvolvimento backend com Python.

Mais do que reproduzir exemplos, a proposta é entender como cada componente funciona e como aplicar esses conhecimentos na construção de aplicações reais.

---

**Status:** Em desenvolvimento contínuo.
