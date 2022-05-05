# Elastic Beanstalk

With Elastic Beanstalk, you can quickly deploy and manage applications in the AWS Cloud without having to learn about the infrastructure that runs those applications. Elastic Beanstalk reduces management complexity without restricting choice or control. You simply upload your application, and Elastic Beanstalk automatically handles the details of capacity provisioning, load balancing, scaling, and application health monitoring.

Application name: miprimerElasticBeanstalk

Con esto ya puedo acceder a mi página web `http://miprimerelasticbeanstalk-env.eba-nqhkegww.us-east-1.elasticbeanstalk.com/` con un diseño por defecto.

Descargamos el `.zip` de `https://github.com/mauropm/aws-platzi-python.git` pero usando la rama `elastic-beanstalk`. Descomprimimos. creamos el archivo `requirements.txt` con el texto `Flask==1.0.2`. Borramos `.ebextension`, `README.md` y `LICENCE`. Comprimimos de nuevo. Este nuevo zip lo subimos a Elastic Beanstalk en el ambiente creado `Miprimerelasticbeanstalk-env`.

Ahora la página ya tiene el mismo diseño que implementamos anteriormente cuando creamos la EC2.