# Compute Engine

In this lab, you will create virtual machines (VMs) and connect to them. You will also create connections between the instances.

## Crear VM desde la consola

> **Compute Engine** > **VM instances** > **create instance**

El nombre de la VM es **my-vm-1**. Permitir trafico HTTP. Esta VM se crea en **us-central1-a**

## Crear VM desde el Cloud Shell

Definir default zone

```
gcloud config set compute/zone us-central1-b
```

Crear VM **my-vm-2**

```
gcloud compute instances create "my-vm-2" \
--machine-type "n1-standard-1" \
--image-project "debian-cloud" \
--image-family "debian-10" \
--subnet "default"
```

En este momento tengo dos VM en distintas zonas, pero la misma región.

## Conectar las instancias

Conectarme por SSH a **my-vm-2** (desde consola).

Luego, hacer ping a la VM 1

```
ping my-vm-1.us-central1-a
```

Conectarme por ssh a VM

```
ssh my-vm-1.us-central1-a
```