# RAG - Retrieval-Augmented Generation 🧩

Projeto de estudo que implementa um sistema simples de Retrieval-Augmented Generation (RAG) utilizando Python, LangChain, ChromaDB, Ollama e modelos de linguagem (LLMs) locais de código aberto para responder perguntas com base em documentos PDF.

## 🎯 Objetivo do projeto

Construir um sistema RAG funcional básico que permita fazer perguntas sobre documentos PDF locais, utilizando apenas ferramentas open source e modelos que rodam localmente, sem quaisquer custos.

## 🛠️ Tecnologias Utilizadas

- **Python 3.11+** - Linguagem principal
- **LangChain** - Framework para trabalhar com LLMs
- **ChromaDB** - Banco de dados vetorial para armazenar embeddings
- **Ollama** - Executor de modelos LLM locais
- **Gradio** - Interface de chatbot
- **llama3.2:3b** - Modelo LLM
- **mxbai-embed-large** - Modelo de embeddings

## 📋 Pré-requisitos

- Python 3.11 ou superior
- [Ollama](https://ollama.ai) instalado
- 8GB de RAM (mínimo)
- ~4GB de espaço em disco (para os modelos)

## 🚀 Instalação

### 1. Clonar o Repositório
```bash
git clone https://github.com/gabrielf-elipe/Retrieval-Augmented-Generation.git
```

### 2. Criar Ambiente Virtual
```bash
python -m venv .venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Instalar e Baixar Modelos com Ollama
Após instalar o Ollama em https://ollama.ai :
```bash
# Baixar o modelo LLM
ollama pull llama3.2:3b

# Baixar o modelo de embeddings
ollama pull mxbai-embed-large

# OBS: é possível utilizar outros modelos de sua preferência
```

---

## 💻 Como usar
### 1. Adicionar PDFs
Coloque seus arquivos PDFs na pasta 'data/'

### 2. Criar o banco de dados vetorial
```bash
python setup_db.py
```

### 3. Executar o programa principal
```bash
python main.py
```

Isso permitirá o acesso a uma interface no navegador, cujo endereço será informado pelo terminal.

### 4. Fazer Perguntas
Escreva suas perguntas na interface do Gradio e receba respostas baseadas nos seus PDFs!

## 🔮 Proximos passos do projeto
- Trabalhar com diferentes tipos de arquivo, docx. xml, csv...
- Ser capaz de interpretar imagens.
- Analises mais profundas com capacidade de gerar gráficos
- Estudar e implementar os melhores parâmetros para o banco vetorial e para os modelos.