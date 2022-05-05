# Kubernetes

API necesarias para usar kubernetes

- Kubernetes Engine API
- Container Registry API

Crear un cluster kubernetes administrado por Kubernetes Engine. El cluste se llamará **webfrontend** y tendrá dos nodos.

```
gcloud container clusters create webfrontend --zone us-central1-a --num-nodes 2
```

Kubernetes Engine se trata de una instancia de VM que implementa contenedores. Por tanto se pueden visualizar como cualquier VM.

Crear servidor Nginx en el contenedor 

```
kubectl create deploy nginx --image=nginx:1.17.10
```

para ver los **pod** corriendo en el contenedor

```
kubectl get pods
```

para exponer el contenedor nginx a internet

```
kubectl expose deployment nginx --port 80 --type LoadBalancer
```

para ver el servicio

```
kubectl get services
```

# `kubectl` commands

kubectl es una herramienta de línea de comandos que puedes usar para interactuar con tus clústeres de GKE.

```
kubectl version
```