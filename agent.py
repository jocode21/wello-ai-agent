from langchain_community.llms import LlamaCpp
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from tools.weather_tool import get_weather_by_coords
import os

def find_model_file():
    models_dir = "./models"
    for f in os.listdir(models_dir):
        if f.endswith(".gguf"):
            return os.path.join(models_dir, f)
    raise FileNotFoundError("No .gguf model found in ./models/")

model_path = find_model_file()
print(f"Using model: {model_path}")

llm = LlamaCpp(
    model_path=model_path,
    temperature=0.7,
    max_tokens=100,
    n_ctx=512,
    n_batch=32,
    stop=["Question:", "Helpful Answer:"]
)

emb = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

system_prompt = """
You are Wello, a weather and wellness AI assistant.
Your ONLY job is:
- Provide weather updates using the weather tool.
- Give simple wellness or health tips related to weather.
- Talk in a friendly, short, and caring style.
- Never generate trivia, accidents, or random Q&A stories.
- If the user asks about something outside weather/wellness, reply politely:
  "I focus only on weather and wellness, so I may not know that."

Always introduce yourself as:
"Hi, I am Wello, your weather and wellness assistant."
"""

qa_prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=system_prompt + "\n\n{context}\n\nUser: {question}\nWello:"
)


def build_vectorstore_from_file(path="data/example.txt"):
    from langchain.document_loaders import TextLoader
    from langchain.text_splitter import CharacterTextSplitter
    loader = TextLoader(path)
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(loader.load())
    vect = Chroma.from_documents(docs, embedding=emb, persist_directory="./chroma_db")
    vect.persist()
    return vect

def make_agent(vstore=None):
    if vstore is None:
        vstore = Chroma(persist_directory="./chroma_db", embedding_function=emb)
    retriever = vstore.as_retriever(search_type="similarity", search_kwargs={"k":3})
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": qa_prompt}
    )

    def run_agent(query):
        try:
            if "weather" in query.lower():
                # Kochi coordinates
                lat, lon = 9.9312, 76.2673
                data = get_weather_by_coords(lat, lon)

                # safely check if data has what we expect
                if "hourly" in data and "temperature_2m" in data["hourly"]:
                    temp_now = data["hourly"]["temperature_2m"][0]
                    return f"The current temperature in Kochi, Kerala is {temp_now} C."
                else:
                    return "⚠️ Sorry, I couldn't fetch the weather right now."

            # fallback to QA chain
            return qa.run(query)

        except Exception as e:
            return f"⚠️ Sorry, something went wrong: {str(e)}"


    return run_agent
if __name__ == "__main__":
    agent = make_agent()
    print(agent.run("Hello Wello!"))
