# FRG

## Préparation
- Créer son environnement virtuel et l'activer.

```bash
python3 -m venv venv

# Ubuntu command
source venv/bin/activate

# FreeBSD command
. venv/bin/activate
```
- Installer les prérequis.

```bash
pip install -r requirements.txt
```

- S'assurer que les variables d'environnement dans le fichier .flaskenv sont bien définies telles que ci-dessous, les modifier sinon.

```bash
FLASK_APP=frg.py
FLASK_RUN_HOST=0.0.0.0
FLASK_RUN_PORT=5000
```

## Lancer Flask

```bash
flask run
```
## Accès à l'API à distance

POST :
```bash
curl --request POST '<instance-adress-DNS-public-IPv4)>:5000/api/files' \
--form 'file=@/home/quarz/Documents/FRG/fichiers_test/text_csv.csv'
```
'file=@' est à adapter en fonction du chemin du fichier. Différents formats de fichiers sont accessibles dans le répertoire FRG/fichiers_test/.

# Serverless

## Préparation
- Se placer dans la racine de l'application flask
- Installer les dépendances suivantes

```bash
npm install --save-dev serverless-wsgi serverless-python-requirements 
```

## Déployer serverless

```bash
sls deploy
```
## Curl serverless
Commande à utiliser pour POST un fichier sur serverless

```bash
curl  --request POST 'https://y4dq8zt776.execute-api.eu-west-1.amazonaws.com/dev/api/files' \
	--form 'file=@/home/quarz/Documents/FRG/fichiers_test/text_plain_2.txt'
```
'file=@' est à adapter en fonction du chemin du fichier.

## Stockage sur S3
Pour permettre à lambda d'accéder à s3, il est nécessaire de rajouter en plus dans le fichier serverless.yml (si ce n'est pas déjà fait) sous "provider" :

```bash
provider:
  iamRoleStatements:
    - Effect: Allow
      Action:
        - s3:PutObject
      Resource: 'arn:aws:s3:::bucketdemarde/*'
```

## Suppression des fichiers au bout d'un an (théorie)
Pour configurer la suppréssion de fichier périodique, il est nécessaire d'ajouter une règle de cycle de vie au niveau du bucket considéré.

### Nom de portée
- Saisir un nom de règle
- Cocher : "S'appliquer à tous les objets du compartiment"

### Transitions
Ne rien cocher.

### Expiration
- Cocher "Version actuelle" : faire expirer la version actuelle de l'objet après 365 jours  suivant la création de l'objet.
- Cocher "Versions précédentes" : Supprimer définitivement les versions précédentes 1 jours après être devenue une version précédente

## Suppression des fichiers au bout d'un an (pratique)
Voir la règle de cycle de vie du bucket "bucketdemarde"

# SOA
## Prérequis

Lancer flask : voir § FRG.

## Accès à Swagger

Swagger est accessible à l'adresse suivante :

\[instance-adress-DNS-public-IPv4)\]:5000/swagger

