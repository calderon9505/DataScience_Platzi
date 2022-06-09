# App Engine

Inicializar un App Engine

```
gcloud app create --project=$DEVSHELL_PROJECT_ID
```

Crear proyecto **hello_world**

```sh
git clone https://github.com/GoogleCloudPlatform/python-docs-samples
cd python-docs-samples/appengine/standard_python3/hello_world
```

Crear archivo llamado ``Dockerfile``

```
FROM python:3.7
WORKDIR /app
COPY . .
RUN pip install gunicorn
RUN pip install -r requirements.txt
ENV PORT=8080
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 main:app
```

crear contenedor y correr aplicación. Pero presionar `ctrl + c` para abortar el despliegue.

```
docker build -t test-python . 
docker run --rm -p 8080:8080 test-python 
```

para desplegar usando el App Engine

```
cd ~/python-docs-samples/appengine/standard_python3/hello_world
gcloud app deploy
gcloud app browse
```

