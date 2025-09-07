from fastapi import FastAPI
from pydantic import BaseModel
import gradio as gr
import agent

app = FastAPI()
qa = agent.make_agent()

class Query(BaseModel):
    text: str

@app.post("/chat")
async def chat(q: Query):
    resp = qa.run(q.text)
    return {"answer": resp}

if __name__ == "__main__":
    def respond(user_input):
        return qa(user_input)
    demo = gr.Interface(fn=respond, inputs="text", outputs="text", title="Joel's Wello")
    demo.launch(share=True)

