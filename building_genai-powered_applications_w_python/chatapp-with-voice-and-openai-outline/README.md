# coding-project-template


## cd to folder
cd building_genai-powered_applications_w_python
cd chatapp-with-voice-and-openai-outline


# Cert folder
mkdir certs
cp /usr/local/share/ca-certificates/rootCA.crt certs

# Docker
docker build . -t voice-chatapp-powered-by-openai
docker run -p 8000:8000 voice-chatapp-powered-by-openai

# STT
base_url = "https://sn-watson-stt.labs.skills.network"

# TTS
base_url = "https://sn-watson-tts.labs.skills.network"