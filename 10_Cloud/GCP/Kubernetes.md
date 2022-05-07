# Kubernetes

## Ciclo de vida del software

Desarrollo --> Integración --> Testing --> Producción

## Máquinas virtuales

Entorno en que se virtualiza un sistema operativo y un hardware (se usa un pedazo de procesador, ram y disco duro). El OS cree que está en un hardware real pero en realiadad está virtualizado. Las VM son **pesadas**.

## Contenedores

Contienen todo lo que necesita una aplicación para funcionar (y nada más que eso)

Un contenedor es un entorno de ejecución para un software que contiene todas las dependencias que necesita el software. Pero, es un paquete **aislado** del sistema. Es decir, puede tener las versiones necesarias de cada librería sin interferir con las librerías de otros contenedores.

Dicho contenedor es el que se replica en otros entornos (producción por ejemplo).

> Un contenedor no carga todo el OS, solo necesita el kernel. Eso los hace muy rápidos.

### Name spaces

Los namespaces hacen que un conjunto de aplicaciones tenga acceso a un conjunto específico de recursos. Por lo que cada conjunto de procesos no interfiere con los recursos de otro proceso.

### C groups

Permite administrar el uso de recursos de los procesos junto con sus permisos de acceso

### LXC

Es el motor de contenedores de Linux

## Docker

Es un gestor de contenedores. Dejó de usar **LXC** para usar **libcontainer**.

Docker file --> Docker image --> Docker container

* Docker file: **Documento de texto** que contiene todos los comandos e instrucciones para instalar todas las dependencias de una aplicación. Se puede llevar registro de versiones con git (docker registry).

* Docker image: Es un **ejecutable** que contiene todas las dependencias y el código que se va a correr. A partir del docker image se pueden crear los contenedores. 

* Docker container: El contenedor es el docker image ya corriendo!

## Monolítico Vs Microservicios

Una aplicación monolítica tiene todas las funciones en un solo paquete. (para aplicaciones pequeñas)

Una arquitectura de microservicios tiene *mini aplicaciones* con funciones específicas que se comunican entre ellas. (para aplicaciones grandes o que van a crecer)

> Cada microservicio tiene su contenedor. Lo que la hace más robusta pero más compleja.

## Kubernetes

Es un orquestador de contenedores.

Automatiza los procesos con los contenedores, asignación de recursos y despliegues.

> No se hace de forma imperativa (secuencia de pasos a realizar) sino de forma **declarativa** (Se especifica el resultado deseado, no cómo lograrlo)

Se tiene un archivo **control plane** donde se describe el estado deseado.

Cada implementación de Kubernetes se llama **Cluster**.

> Con Kubernetes se buscar optimizar el uso de los recursos de hardware.

![](https://edteam-media.s3.amazonaws.com/infographics/original/bde4a0fa-ce8c-4bbb-8a5e-9bbc58e49568.png)

El **Master Node** se encarga de la comunicación, automatización y gestión de procesos.

En los **Worker Nodes** se encuenteran las aplicaciones. El servicio **Kubelet** de cada worker node se comunica con el servicio **Kube-apiserver** del master node.

Cada worker node tiene un POD (o varios?). Dentro del POD están los contenedores de docker.

> Escalar de manera horizontal significa añadir mas PODs. Escalar de manera vertical significa añadir mas clusters.

