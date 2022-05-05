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
