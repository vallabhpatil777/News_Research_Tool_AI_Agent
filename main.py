import streamlit as st 
import os
from dotenv import load_dotenv
from Analyzer import process_urls, answer_query

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    st.error("GROQ API Key is missing! Check your .env file.")
else:
    os.environ["GROQ_API_KEY"] = GROQ_API_KEY

st.title("News Research Tool 📈 ")

st.sidebar.title("News Article URLs")
urls = []
num_urls = st.sidebar.number_input("How many articles you want to use?",min_value=1,
    max_value=10,
    step=1, 
    value=1)


st.sidebar.title("Provide Article URLs")


for i in range(num_urls):
    url = st.sidebar.text_input(f"Article {i+1}")
    urls.append(url)
process_url_clicked = st.sidebar.button("Process URLs")

placeholder = st.empty()
if process_url_clicked:
    placeholder.text("Data Loading Started...")
    print("Urls list :",urls)
    process_urls(urls=urls)
        
    placeholder.text("Data Processed Successfully!!")
    
user_query = st.text_area("Ask your question about the articles:")

if st.button("Answer"):
    if not user_query:
        st.error("Please enter a question.")
    else:
        response = answer_query(user_query)
        st.header("Answer")
        st.write(response.get("answer", "No answer found."))
        st.header("Source")
        st.write(response.get("sources", "No answer found."))
