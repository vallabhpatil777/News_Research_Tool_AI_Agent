# News_Research_Tool_AI_Agent

A tool for researching news articles, built using **Python**, **Langchain**, **LLM**, **Groq API**, **FAISS** for storing vector indices, and **Streamlit** for the user interface. This tool allows users to input article URLs, scrapes the content, processes the text, and then enables question-answering based on the provided articles.

## Features

- **Article URL Input**: Users can provide URLs of news articles (max 10).
- **Web Scraping**: Extracts content from the provided URLs.
- **Text Processing**: Utilizes LLM and Groq API for processing and analyzing the text.
- **Vector Indexing**: Stores processed text as vectors in the FAISS database for fast retrieval.
- **Question Answering**: Users can ask questions based on the content of the articles.

## Technologies Used

- **Python**
- **Langchain**
- **LLM (Large Language Models)**
- **Groq API**
- **FAISS** (for vector indexing)
- **Streamlit** (UI)

## How It Works

1. **Input**: Provide the URL of a news article.
2. **Web Scraping**: The tool scrapes the article’s content.
3. **Text Processing**: The text is processed using advanced language models for better understanding.
4. **Vectorization**: Text is converted into vectors using FAISS for quick search and retrieval.
5. **Question Answering**: Ask questions based on the article's content, and get relevant answers.
   
## Steps

### 1. Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```


### 2. Create Virtual Environment : 

For MacOS/Linux : 
```bash
python3 -m venv venv
source venv/bin/activate
```

For Windows :
```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install required libraries : 
```bash
pip install -r requirements.txt
```


### 4. Setup Groq Cloud API : 

Link : https://console.groq.com/login

### 5. Create .env file into the directory : 

Copy paste your API key into the file and save it.
```bash
GROQ_API_KEY = "your_groq_api_key"
```

### 6. Run the streamlit app : 

```bash
streamlit run main.py
```

