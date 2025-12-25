# 🛡️ Outils d'Automatisation & Sécurité (Python)

Ce dépôt regroupe une collection de scripts Python développés dans le cadre de mon apprentissage en Cybersécurité et Administration Système.

L'objectif de ces outils est d'automatiser des tâches récurrentes de maintenance, d'audit et de prévention des risques en entreprise .

##  Contenu du projet

### 1. Audit & Conformité
- **`audit_pc.py`** : Vérifie instantanément l'état du Pare-feu Windows via des commandes système (`netsh`). Permet de détecter une vulnérabilité basique sur un poste de travail.

### 2. Gestion & Inventaire
- **`inventaire.py`** : Simule un scan réseau et génère automatiquement un rapport au format CSV (Excel) listant les machines connectées (IP, État, Type). Lutte contre le *Shadow IT*.
- **`ping_sweep.py`** : Outil de cartographie réseau basique utilisant le protocole ICMP pour identifier les machines actives sur une plage IP donnée.

### 3. Prévention & Risques
- **`coach_mdp.py`** : Outil pédagogique de vérification de mot de passe. Il applique une politique de sécurité stricte (Longueur, caractères spéciaux) et empêche l'utilisation du nom de l'entreprise dans le mot de passe.
- **`radar_ip.py`** : Système de détection d'intrusion simple (IDS) basé sur une liste blanche (Whitelisting). Alerte si une adresse IP inconnue se connecte au réseau local.

##  Utilisation
Ces scripts sont conçus pour fonctionner nativement sous Windows avec Python 3 installé.
Aucune installation complexe n'est requise, ils utilisent principalement des bibliothèques standards (`os`, `csv`, `socket`).

---
*Projet réalisé par Haitam - Étudiant en Cybersécurité*
