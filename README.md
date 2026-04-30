# Projet 8 - Déployez et monitorez un modèle de scoring

## Objectif

Ce projet a pour objectif de mettre en production un modèle de scoring de crédit développé précédemment, en mettant en place :

- Une API de prédiction (FastAPI)
- Une conteneurisation avec Docker
- Un pipeline CI/CD (GitHub Actions)
- Un système de monitoring (Streamlit)
- Une analyse du data drift

---

## Contexte métier

L’entreprise "Prêt à Dépenser" souhaite utiliser un modèle de scoring pour traiter les demandes de crédit en quasi temps réel.

Le modèle prédit la probabilité de défaut d’un client, afin d’aider à la prise de décision (acceptation ou refus du crédit).

---

## Modèle

Le modèle de scoring a été entraîné lors du projet précédent (MLOps).

- Algorithme : LightGBM
- Données : Home Credit Default Risk
- Optimisation basée sur un coût métier (FP / FN)
- Seuil de décision optimisé

---

## Fonctionnement de l'API

L’API permet :

d’envoyer les données d’un client
de retourner :
la probabilité de défaut
la classe prédite (accepté / refusé)

---

## Monitoring

Un dashboard permet de suivre :

la distribution des scores
les temps de réponse de l’API
le data drift entre données d’entraînement et production

---

## CI/CD

Un pipeline GitHub Actions permet :

d’exécuter les tests automatiquement
de valider les modifications avant déploiement

---

## Lancement

```bash
# Installation des dépendances
pip install -r requirements.txt

# Lancer l'API
uvicorn app.main:app --reload

---

## Structure du projet

```bash
.
├── app/                # API de scoring (FastAPI)
├── model/              # Modèle entraîné + artefacts
├── tests/              # Tests unitaires
├── monitoring/         # Dashboard de monitoring (Streamlit)
├── notebooks/          # Analyse et data drift
├── data_sample/        # Données de test
├── screenshots/        # Preuves visuelles (monitoring, stockage)
├── .github/workflows/  # CI/CD
├── Dockerfile
├── requirements.txt
├── README.md

