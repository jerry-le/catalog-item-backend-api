# Server-side Catalog Item Rest API

## Installation
#### Clone or download this project
```shell
git clone https://github.com/jerry-le/catalog-item-backend-api
```

#### Create virtual environment
Create a virtual environment from `requirements.txt` and enable it.

- From conda
```shell
conda create -n flask-env python=3.5
pip install -r requirements.txt
source activate flask-env
```

- From virtualenv
```sell
virtualenv flask-env
source flask-env/bin/activate
pip install -r requrements.txt
```

#### Run server
```
(flask-env) export FLASK_APP=autoapp.py

(flask-env) export FLASK_ENVIRONMENT=dev # For development env
(flask-env) export FLASK_ENVIRONMENT=prod # For production env

(flask-env)flask run --with-threads -h 0.0.0.0 -p 5000
```

#### Run test
```
(flask-env) flask test
```

#### Show all available endpoints
```
(flask-env) flask urls
```
