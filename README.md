# TODOs App

## Install
```sh
git clone https://github.com/PyDevNik/todos-app.git
cd todos-app
```

## Setup
```sh
cd deploy
sudo sh setup.sh
```

## Run
```sh
cd backend/app
gunicorn wsgi:app
```

## Deploy
- `Nginx`
- `Docker`
- `Kubernetes`
