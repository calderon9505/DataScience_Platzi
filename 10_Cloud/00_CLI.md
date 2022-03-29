# Command Line Interface

Instalación del CLI en Linux
```
pip3 install awscli
```

Instalación de CLI version 2 en Linux. [AWS CLI V2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-path.html)
```sh
$ sudo apt remove --purge awscli
$ sudo curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
$ unzip awscliv2.zip
$ sudo ./aws/install
$ nano .profile
export PATH=/usr/local/bin:$PATH
$ source ~/.profile
```

---

Configuración del entorno
```sh
$ aws configure
```
```
AWS Access Key ID [None]: AKIAIO...
AWS Secret Access Key [None]: wJalrXU...
Default region name [None]: us-east-1
Default output format [None]: ENTER
```
Configuración del entorno desde el archivo de credenciales
```
$ aws configure import --csv file://calderon950527_credentials.csv
```

---

Creación de *Security Group* para **EC2** con salida json.
```sh
$ aws ec2 create-security-group --group-name security-group-from-cli --description "Security group creado desde CLI"
```
```sh
{
    "GroupId": "sg-02e7b920dca4cb1b6"
}
```

---

