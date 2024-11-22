# LLM Projet

## Prérequis

- Python 3.x
- pip (gestionnaire de paquets Python)
- Accès AWS avec les clés `<votre_access_key_id>` et `<votre_secret_access_key>`
- Les bibliothèques Python suivantes :
  - `fitz`
  - `ollama`
  - `boto3`

## Installation

1. Clonez le dépôt :

   ```bash
   git clone <URL_DU_DEPOT>
   cd <NOM_DU_DEPOT>

2. Créez un environnement virtuel et activez-le :
python3 -m venv env
source env/bin/activate

## Configuration

Créez un fichier .env à la racine du projet et ajoutez vos clés AWS :
ACCESS_KEY_ID=<votre_access_key_id>
AWS_SECRET_ACCESS_KEY=<votre_secret_access_key>

## Lancement
Exécutez l'application :

python main.py


## Fonctionnalités
  Sauvegarde de fichiers
  Extraction de texte à partir de fichiers PDF
  Interaction avec le modèle Ollama
  Téléchargement de fichiers depuis un bucket S3

## Structure du projet
  main.py : Contient le code principal de l'application.
  server/documents : Répertoire où les documents sont sauvegardés.
