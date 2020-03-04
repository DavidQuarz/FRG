# FRG

## Préparation
- Créer son environnement virtuel et l'activer.

```bash
python3 -m venv venv
source venv/bin/activate
```
- Installer les prérequis

```bash
pip install -r requirements.txt
```

- Modifier les variables d'environnement dans le fichier .flaskenv

```bash
FLASK_APP=frg.py
FLASK_RUN_HOST=0.0.0.0
FLASK_RUN_PORT=5000
```

## Lancer Flask

```bash
flask run
```
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

## Stockage sur S3
Pour permettre à lambda d'accéder à s3, il est nécessaire de rajouter en plus dans le fichier serverless.yml (si ce n'est pas déjà fait) sous "provider"

provider:
  iamRoleStatements:
    - Effect: Allow
      Action:
        - s3:PutObject
      Resource: 'arn:aws:s3:::bucketdemarde/*'