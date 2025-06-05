## cd to folder
cd building_genai-powered_applications_w_python
cd chat_bot

### Create venv
python3 -m venv venv

### Activate venv
source venv/bin/activate

# Install dependencies
python3 -m pip install transformers torch flask flask_cors
python -m pip install -r LLM_application_chatbot/requirements.txt

# Curl for testing app
curl -X POST -H "Content-Type: application/json" -d '{"prompt": "Hello, how are you today?"}' 127.0.0.1:5000/chatbot

# 
cd LLM_application_chatbot
flask run