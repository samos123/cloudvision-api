# CloudVision RESTful API

## Setup dev env

    mkvirtualenv -p python3 cloudvision-api
    pip install -r requirements.txt
    docker run -p 127.0.0.1:27017:27017 --name cloudvision-mongo -d mongo
    python app.py
