# Qué es el cómputo en la nube?

- Autoservicio y bajo demanda
- Conectado a la red (conectado a interned)
- Economías de escala (las grandes empresas compran en masa)
- Elasticidad (Crece la infraestructua de maneta automática cuando se necesitan los recursos)
- Servicio medido (se cobra lo que se usa)

> El computo en la nube es "una computadora enorme" de escala mundial a la cual tengo acceso, y donde GCP es el sitema operativo. (David Aroesti)

[Measure your latency to Google Cloud regions](https://gcping.com/)

[Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator)

[Capa gratuita](https://cloud.google.com/free?hl=es)


# Jerarquía de recursos

> Todo en GCP es un recurso (una VM, un disco duro, una GKE, un app engine, un switch de red, una regla de seguridad del firewall, etc)

- **Organización** (billling account, grupos de administradores, permisos principales, identidades)

- **Carpetas**. Pueden tener proyectos o otras carpetas.

- **Proyectos**. Tienen los recursos dentro de GCP.

- **Recuros**.


# IAM

- **Quién**. Es el "miembro". Puede referirse a una persona real o a un subsistema (una aplicación por ejemplo). El **Zero Trust** es un concepto de seguridad que hace referencia a que se tiene cero confianza, esto es, todo va cifrado y todo requiere permisos, incluso dentro del perímetro de seguridad. Un **Service Account** es la identidad de una aplicación.

- **Puede hacer qué**. (Generar buckets de storage, prender VMs, generar ususario, generar bases de datos, borrarlas, actualizarlas, etc)

- **En cuál recurso**. Las **políticas de seguridad** se asignan a cada uno de los recursos. 

Todo esto para indicar qué miembros tiene qué roles sobre qué recurso.

Normalmente los permisos no se asignan de manera directa, sino que se genera un rol. Un rol es una colección de permisos. (rol de administrador de red, por ejemplo, con permisos para redes, subredes, conexiones entre redes, rangos IP, etc). Los roles no suelen asignarse a personas, sino a grupos. 

Se pueden generar políticas en cualquier punto de la jerarquia y dicha política se hereda hacia abajo. Es decir, si alguien tiene el permiso de crear buckets a nivel organización, tambien tienen permiso para generar buckets en todos los proyectos de dicha organización. Pero si la política va en una carpeta, solo tendrías acceso a los proyectos que contenga dicha carpeta. Igual a nivel proyecto.

Yo creo una politica, en donde relaciono roles y miembros, y dicha política se la pego a un determinado recurso.