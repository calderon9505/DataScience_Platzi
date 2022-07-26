# Qué es el cómputo en la nube?

- Autoservicio y bajo demanda
- Conectado a la red (conectado a interned)
- Economías de escala (las grandes empresas compran en masa)
- Elasticidad (Crece la infraestructua de maneta automática cuando se necesitan los recursos)
- Servicio medido (se cobra lo que se usa)

> El computo en la nube es "una computadora enorme" de escala mundial a la cual tengo acceso, y donde GCP es el sitema operativo. (David Aroesti)

- A **region** is a specific geographical location where you can run your resources

- A **zone** is a deployment area for Google Cloud Platform resources within a region.

- A **point of presence** (PoP) is where Google's network is connected to the rest of the internet

[Measure your latency to Google Cloud regions](https://gcping.com/)

[Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator)

[Capa gratuita](https://cloud.google.com/free?hl=es)


# Jerarquía de recursos

- **Organización** (billling account, grupos de administradores, permisos principales, identidades)

- **Carpetas**. Pueden tener proyectos o otras carpetas.

- **Proyectos**. Tienen los recursos dentro de GCP.

- **Recurso**. Todo en GCP es un recurso: una VM, un disco duro, una GKE, un app engine, un switch de red, una regla de seguridad del firewall, etc.


# IAM

* **Group**: Es un conjunto de  **users**. Un user puede ser una persona o un susbsistema. Los subistemas se identifican con los **Service Account**

* **Role**: Es un conjunto de **permissions**. Un permission es una acción determinada sobre un recurso determinado.

* **Policy**: Una política relaciona un **group** (who) con un **role** (can do what) sobre un **resource** (On which resource).

Aunque se pueden asignar permisos a usuarios de manera directa, lo correcto sería asignar roles a grupos.

Se pueden generar policys en cualquier punto de la jerarquia (Projects, folders, and organization nodes. Some GCP resources let you put policies on individual resources too, like GCS) y dicha política se hereda hacia abajo. Es decir, si alguien tiene el permiso de crear buckets a nivel organización, tambien tienen permiso para generar buckets en todos los proyectos de dicha organización. Pero si la política va en una carpeta, solo tendrías acceso a los proyectos que contenga dicha carpeta. Igual a nivel proyecto.

> El **Zero Trust** es un concepto de seguridad que hace referencia a que se tiene cero confianza, esto es, todo va cifrado y todo requiere permisos, incluso dentro del perímetro de seguridad.