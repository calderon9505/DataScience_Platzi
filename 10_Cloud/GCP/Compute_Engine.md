# Compute Engine

Servicio de GCP que permite crear VMs.

A VM is **similar but not identical** to a hardware computer. VMs consists of a virtual CPU, some amount of memory, disk storage, and an IP address. A VM offers many options that can't exist in physical hardware:

* A micro VM shares a CPU with other virtual machine, so you can get a VM with less capacity at a lower cost.

* Some VMs offer a burst capability meaning that the virtual CPU will run a buffets rated capacity for a brief period using the available shared physical CPU.

## Network

It will scale at:

* 2 Gb/s for each CPU core
* 10 Gb/s for instances with 2 or 4 CPUs
* 32 Gb/s for instances with 16 o more CPUs
* 100 Gb/s for instances that have T4 or V100 GPUs

## Disk

* Standar: higher amount of capacity/dollar
* SSD: higher number of IOPS/dollar
* local SSD: even higer throughput and lower latency than SSD. The data persists only until the instance is stoped.


## Access

To access via SSH it requires firewall rule to allow tcp:22 (for Linux)

To access via RDP(remote desktop protocol) it requires firewall rule to allow tcp:3389 (for Linux)



# `gcloud` commands

El grupo de comandos **gcloud** permite administar los recursos de **Compute Engine**

para listar las cuentas activas
```
gcloud auth list
```

para listar la configuración del proyecto
```
gcloud config list
gcloud config list project
```

para cambiar el proyecto al que apunta el Cloud Shell
```
gcloud config set <PROJECT_ID>
```

Propiedades predeterminadas de mi VM
```
gcloud compute project-info describe --project <PROJECT_ID>
```

Para ver la region/zona predeterminada

```
gcloud config get-value compute/region
gcloud config get-value compute/zone
```

Para listar regiones/zonas disponibles

```
gcloud compute regions list
gcloud compute zones list
gcloud compute zones list | grep us
```

Los comandos `gcloud compute` requieren marcas para `--region` o `--zone`. Se puede establecer una región o zona *predeterminada* y así evitar el uso de las marcas. Si a un comando se le pasa marca de región/zona, se anulan la region/zona predeterminada. 

La región/zona predeterminada se puede hacer de tres maneras(cada una sobreescribe la otra):
- En el servidor de metadatos
- En el cliente local
- En las variables de entorno

Para establecer region/zona en el cliente local

```
gcloud config set compute/region REGION
gcloud config set compute/zone ZONE
```

Para listar las instancias

```
gcloud compute instances list
```