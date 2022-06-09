# Virtual Private Cloud

Ambiente de red virtual, aislado y privado que se basa en el concepto de red definida por software.

Es una manera de establecer conectividad entre los recursos de la nube.

- Una VPC tiene alcance global
- Una VPC debe estar asociada a un proyecto
- Las VPC están aisladas de forma lógica unas de otras
- Las VPC se pueden compartir con otros proyectos, o emparejar con otras redes de otros proyectos
- Una VPC tiene IPs individuales (no rangos)
- El tráfico entre redes NO toca el internet público
- Debe existir al menos una subred
- Las subredes tiene un alcance regional
- Las subredes tienen asociados rangos de IP



![](https://cloud.google.com/vpc/images/vpc-overview-example.svg)


> Dos VM se pueden comunicar con IPs internas si están en la misma red (aunque estén en distinta region)

> Dos VM se **deben** comunicar con IPs externas si están en distinta red (aunque estén en la misma región)


## Tipos de VPC

- **Default**. 
    - Presente en cada proyecto. 
    - Una subred por región. 
    - Reglas de firewall por defecto.

- **Auto Mode**
    - Red por defecto.
    - Una subred por región.
    - Subred /20 expandible a /16

- **Custom mode**
    - No se crean redes por defecto
    - Control total del rango de IPs
    - Subred expandible a cualquier tamaño
    - Esta es la red a usar para producción.

Cuando se crea un nuevo proyecto, trae una red por defecto, la cual es Auto mode. El problema con esta red, es que no se tiene control de los rangos IP de las subredes, y si se quisiera unir dos VPC van a haber recursos que tienen el mismo direccionamiento


## IP addresses

Cualquier servicio que dependa de VMs tiene una IP interna.

La IP externa es opcional y sirve para exponer la VM a internet. Es *efímera* (excepto si se tiene IP estática reservada)

Los rangos de IP se usan para asignar IPs privadas a los recursos de la subred. (0 y 1 están reservadas para compuertas de red y subred. la última y penulima están reservadas para broadcast).

El nombre de instancia (hostname) de VM se registra en un DNS que traduce el nombre a la IP interna. El DNS tiene alcance dentro de la red, pero no en otras redes.

para conocer el FQDN(Fully Qualified domain name) interno: 
 > [hostname].[zone].c.[project-id].internal


## Firewall rules

Las **Rutas** permiten a las instancias enviar tráfico directamente de la una a la otra (incluso a través de subredes). Una Ruta se crea cuando se crea una red o subred.

El tráfico no fluirá sin relacionar la reglas del firewall, Estas protegen la VM de conecciones no aprovadas(de entrada y salida).

Cada red VPC funciona como un firewall distribuido. El firewall se aplica a la red como un todo, pero las VM pueden permitirlo o denegarlo.

**Egress firewall rules** controls outgoing conections originated inside the GCP (Allow or deny the destinations, the protocols and the ports).

**Ingress firewall rules** protect against incoming connections to the instance from any source(Allow or deny the sources, the protocols and the ports).


## Private Google Access and Cloud NAT

las instancias de VM que solo tienen IP interna pueden usar el **Private Google Access** para acceder a las direcciones IP externas de los servicios y las API de Google. Cuando se inhabilita el Acceso privado a Google ya no se pueden realizar dichos accesos.

> El acceso privado a Google no tiene efecto en las instancias que tienen IP externa.

Pero, para poder tener acceso a todo internet para actualizaciones y parches, se hace necesario el uso de un NAT.

La traducción de direcciones de red (**NAT**) surgieron como respuesta a la escaces de direcciones IP. La idea es sencilla, hacer que redes de ordenadores utilicen un **rango de direcciones especiales** (IPs privadas) y se conecten a Internet usando una única dirección IP (IP pública). Gracias a este “parche”, las grandes empresas sólo utilizarían una dirección IP y no tantas como máquinas hubiese en dicha empresa. También se utiliza para conectar redes domésticas a Internet.

Although vm-internal can now access certain Google APIs and services without an external IP address, the instance cannot access the internet for updates and patches. Configure a Cloud NAT gateway, which allows vm-internal to reach the internet.

# Servicios de red

* **Ruteo**. Definen rutas de acceso para instancias salientes (tráfico de salida).
* **VPN**
* **DNS**
* **NAT**
* **Balanceo de cargas**
* **Firewall**


