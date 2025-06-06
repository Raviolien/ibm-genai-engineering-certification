# How to

## How to set up

### cd to folder
cd ai-applications-with-python-and-flask
cd first_app

### Create venv
python3 -m venv venv

### Activate venv
source venv/bin/activate

### Install Flask
pip install "Flask==3.0.0"

## How to run

### cd to folder
cd ai-applications-with-python-and-flask
cd first_app

### Activate venv
source venv/bin/activate

### To run app
flask --app server --debug run

### To see app output in the terminal (use new terminal cd into folder)
curl -X GET -i -w '\n' localhost:5000
curl -X GET -i -w '\n' localhost:5000/no_content
curl -X GET -i -w '\n' localhost:5000/exp
curl -X GET -i -w '\n' localhost:5000/data
curl -X GET -i -w '\n' "localhost:5000/name_search?q=Abdel"
curl -X GET -i -w '\n' "localhost:5000/name_search?q=123"
curl -X GET -i -w '\n' "localhost:5000/name_search?q="
curl -X GET -i -w '\n' "localhost:5000/name_search?q=qwerty"
curl -X GET -i localhost:5000/person/66c09925-589a-43b6-9a5d-d1601cf53287
curl -X GET -i localhost:5000/person/not-a-valid-uuid
curl -X GET -i localhost:5000/person/11111111-589a-43b6-9a5d-d1601cf51111
curl -X DELETE -i localhost:5000/person/66c09925-589a-43b6-9a5d-d1601cf53287
curl -X GET -i localhost:5000/count
curl -X POST -i -w '\n' \
  --url http://localhost:5000/person \
  --header 'Content-Type: application/json' \
  --data '{
        "id": "4e1e61b4-8a27-11ed-a1eb-0242ac120002",
        "first_name": "John",
        "last_name": "Horne",
        "graduation_year": 2001,
        "address": "1 hill drive",
        "city": "Atlanta",
        "zip": "30339",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff"
}'

curl -X POST -i -w '\n' \
  --url http://localhost:5000/person \
  --header 'Content-Type: application/json' \
  --data '{}'