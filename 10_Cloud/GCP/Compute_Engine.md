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

To access via RDP(remote desktop protocol) it requires firewall rule to allow tcp:3389 (for Windows)



# Familias de VMs

## Propósito general

* **E2**: *Económicas*. Se usan en ambientes Dev & Test. Se usan en ambientes productivos con tráficos no altos. Bases de datos. Microservicios.

* **N2/N2D**: *Balanceadas*. Mayores capacidades de cómputo. Soportan tráficos altos. Mucha transaccionalidad.

* **TAU/T2D**: *Escalables*. picos de tráfico. Web servers. Microservicios contenerizados. Grandes aplicaciones Java.

## Trabajo optimizado

* **C2**: *Optimización cómputo*. Mejor desempeño CPUs. Gaming. Modelado científico.

* **M1/M2**: *Optimización memoria*. Mayor memoria (RAM). Real-time data analytics. In-memory cache. DBs. SAP HANA (database in memory)

* **A2**: *Optimización aceleración*. GPUs de alto desempeño. ML. Computación en paralelo masiva.

## Personalizadas

Se escoge alguna máquina preestablecida y se personalizan los cores y la memoria.



## Conectarme a una VM

GCP ofrece un mecanismo de seguridad basado en el entorno del usuario: **IAP** (Identity-Aware Proxy). Por medio de esto se puede conectar a la VM. La ventaja de esto es que no se requiere IP pública para conectarse.

Se debe crear una regla de Firewall en la VPC seleccionada. Esta regla permitirá la conexión SSH pero solo a través de AIP para tráfico de entrada. El **Source IP ranges** debe ser 35.235.240.0/20 (esto viene de la documentación). Protocolo **tcp** puerto 22.

```sh
gcloud compute ssh <VM_NAME> --zone us-east1-b --tunnel-through-iap
```

GCP ofrece el servicio de **Cloud NAT** para permitir un canal de salida a internet para máquinas que no tienen acceso a internet (no tienen IP pública). Cloud NAT se asigna a una VPC en una región específica. Se debe crear un Router en la región.