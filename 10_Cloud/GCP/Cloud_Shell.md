# Cloud Shell

It is a browser-based interactive shell(CLI) enviroment for GCP that you can access from the GCP console.

Cloud Shell is a **temporary Virtual Machine** with 5 GB of persistent disk storage that has the **Cloud SDK pre-installed**. It has built-in authorization for access to resources and instances.


It is similar to the **gcloud command line** tool, which is whitin the Cloud SDK. The Google Cloud SDK provides the commands to manage the resources. Some commands are:

- `gcloud`
- `gsutil`
- `bq`
- `kubectl`

Para crear variables de entorno que no desaparezcan al cerrar el Shell

```sh
mkdir infraclass
touch infraclass/config
echo INFRACLASS_REGION=$INFRACLASS_REGION >> ~/infraclass/config
echo INFRACLASS_PROJECT_ID=$DEVSHELL_PROJECT_ID >> ~/infraclass/config
cat ~/infraclass/config
```
```sh
nano .profile

# at the end of the file
source infraclass/config
```