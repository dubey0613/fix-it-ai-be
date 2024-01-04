Fix-It AI Backend Documentation
Overview:
Fix-It AI Backend is built using FastAPI and serves as the server-side logic for the Fix-It AI web application. It handles incoming requests from the frontend, processes them, and provides responses to user queries.

Features:
1. FastAPI Backend
Question-Response Mapping: Contains a set of predefined questions and responses used by the chatbot.

API Endpoint: Exposes an API endpoint (/chat) for communication with the frontend. Handles HTTP POST requests. 

CORS Configuration: Configured to allow cross-origin resource sharing with the Fix-It AI Frontend.

Deployment:
The Fix-It AI Backend is deployed using a hosting service such as Heroku or AWS. Ensure that the deployment configurations are correctly set up, including environment variables and dependencies.

Getting Started:
To run the backend locally, follow these steps:

1. Clone the repository.
git clone https://github.com/dubey0613/fix-it-ai-be.git


2.Install dependencies.
pip install -r requirements.txt


3.Run the backend.
uvicorn main:app --reload

