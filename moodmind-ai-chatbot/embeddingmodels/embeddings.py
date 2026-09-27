from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import GoogleGenerativeAIEmbeddings


embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview"
)


texts = [

    "Hello this is Akarsh Vyas",

    "Hello your name is YouTube",

    "And you all are very beautiful"

]


vector = embeddings.embed_documents(texts)


print(vector)