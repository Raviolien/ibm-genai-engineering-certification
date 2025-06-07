# Set up

## Cd to folder
cd building_genai-powered_applications_w_python

## Clode from git
git clone https://github.com/ibm-developer-skills-network/wbphl-build_own_chatbot_without_open_ai.git chatbot_for_your_data
cd chatbot_for_your_data

## Create venv
python3.11 -m venv venv

## Activate venv
source venv/bin/activate

## Install dependencies (takes a while)
python3.11 -m pip install -r requirements.txt

# Run

## Cd to folder
cd building_genai-powered_applications_w_python
cd chatbot_for_your_data

## Activate venv
source venv/bin/activate

## Run app not in container
python3.11 server.py

## Docker
docker build . -t chatbot_for_your_data
docker run -p 8000:8000 chatbot_for_your_data
