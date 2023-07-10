cd backend/app;
docker build -t flask-app:latest .;
docker save -o flask-app.tar flask-app:latest;
kubectl load -f deploy.yaml