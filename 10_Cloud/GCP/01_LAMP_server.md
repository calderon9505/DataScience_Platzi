# Mi primer despliegue

En este laboratorio se despliega un servidor LAMP

> **Marketplace** > **LAMP packaged by Bitname** > **Launch**

esto me genera una IP de mi página web, la cual puedo visitar desde cualquier navegador. Puedo conectarme a mi máquina por **ssh** desde la consola.

Para poner un código **php** de ejemplo en mi página web debo

```sh
cd /opt/bitnami
sudo sh -c 'echo "<?php phpinfo(); ?>" > apache2/htdocs/phpinfo.php'
exit
```
Para ver el cambio realizado

> http://SITE_ADDRESS/phpinfo.php