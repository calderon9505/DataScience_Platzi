# VPC

- A region is a specific geographical location where you can run your resources

- A zone is a deployment area for Google Cloud Platform resources within a region.

- A point of presence (PoP) is where Google's network is connected to the rest of the internet

Una VPC es un conjunto exhaustivo de objetos de red administrados por Google.

# projects, networks and subnetworks

Los proyectos asocian objetos y servicios con la facturación. Los proyectos cotienen redes enteras (5 redes por defecto).

Las redes se pueden compatir con otros proyectos, or emparejar con otras redes de otros proyectos. Un red tiene IPs individuales (no rangos).

Dentro de una red, se puede dividir los recuros en subredes regionales.

Cada proyecto tiene una VPC. Existen tres tipos de red: default, auto y custom. Se puede pasar de auto a custom, pero no al reves.

* **default**: VPC por defecto con una subred para cada región y reglas de firewall preestablecidas.

* **auto**: Se crea una subred para cada región en modo automático con un rango de IPs predefinidos con máscara `/20` que se puede expandir a `/16`

* **custom**: No crea subredes por defecto. completo control sobre subredes y rangos IP.

> Dos VM se pueden comunicar con IPs internas si están en la misma red (aunque estén en distinta region)

> Dos VM se **deben** comunicar con IPs externas si están en distinta red (aunque estén en la misma región)

El tráfico entre redes en realidad no toca el internet púclibo, sino quevan a través de Google edge rooters.

Así como una red puede ser multi-region, una subred puede ser multi-zone. Las subredes son rangos IPs que se pueden usar (0 y 1 están reservadas para compuertas de red y subred. la última y penulima están reservadas para broadcast).

# IP addresses

Cada VM tiene dos IPs asignadas, interna y externa. Cada VM que se inicia y cualquier servicio que dependa de VMs obtiene una IP interna.

El nombre de instancia(hostname) de VM se registra en un DNS que traduce el nombre a la IP interna. El DNS tiene alcance dentro de la red, pero no en otras redes.

para conocer el FQDN(Fully Qualified domain name) interno: 
 > [hostname].[zone].c.[project-id].internal

La IP externa es opcional (si se va a exponer a internet). La IP externa es efímera, excepto si se tiene IP reservada (estática).

# Firewall rules

Las **Rutas** permiten a las instancias enviar tráfico directamente de la una a la otra (incluso a través de subredes). Una Ruta se crea cuando se crea una red o subred.

El tráfico no fluirá sin relacionar la reglas del firewall, Estas protegen la VM de conecciones no aprovadas(de entrada y salida).

Cada red VPC funciona como un firewall distribuido. El firewall se aplica a la red como un todo, pero las VM pueden permitirlo o denegarlo.

Egress firewall rules controls outgoing conections originated inside the GCP (Allow or deny the destinations, the protocols and the ports).

Ingress firewall rules protect against incoming connections to the instance from any source(Allow or deny the sources, the protocols and the ports).




# Private Google Access and Cloud NAT

las instancias de VM que solo tienen IP interna pueden usar el **Private Google Access** para acceder a las direcciones IP externas de los servicios y las API de Google. Cuando se inhabilita el Acceso privado a Google ya no se pueden realizar dichos accesos.

> El acceso privado a Google no tiene efecto en las instancias que tienen IP externa.

Pero, para poder tener acceso a todo internet para actualizaciones y parches, se hace necesario el uso de un NAT.

La traducción de direcciones de red (**NAT**) surgieron como respuesta a la  escaces de direcciones IP. La idea es sencilla, hacer que redes de ordenadores utilicen un **rango de direcciones especiales** (IPs privadas) y se conecten a Internet usando una única dirección IP (IP pública). Gracias a este “parche”, las grandes empresas sólo utilizarían una dirección IP y no tantas como máquinas hubiese en dicha empresa. También se utiliza para conectar redes domésticas a Internet.



Although vm-internal can now access certain Google APIs and services without an external IP address, the instance cannot access the internet for updates and patches. Configure a Cloud NAT gateway, which allows vm-internal to reach the internet.