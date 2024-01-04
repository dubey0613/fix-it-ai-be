from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Define a set of questions and responses
questions_and_responses = {
    "hey": "hello",
    "how are you?": "I am great, what about you?",
    "who are you?": "I am a chatbot",
    "how do you work": "I provide solutions!!",
}

# Configure CORS
origins = ["https://fix-it-ai-frontend.vercel.app"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(input_text: str):
    #print("Received input_text:", input_text)
    # Check if the input_text matches any predefined question
    response = questions_and_responses.get(input_text.lower())  # Case-insensitive matching
    if response:
        return {"response": response}
    else:
        return {"response": "Sorry, I don't have an answer for that yet."}
