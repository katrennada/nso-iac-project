# NSO + Terraform + Ansible Demo Project

## Description

Ce projet démontre l’intégration basique de plusieurs outils incontournables pour un ingénieur réseau automatisation :

- **NSO** : Automatisation et orchestration réseau via API REST
- **Terraform** : Infrastructure as Code pour déployer et orchestrer des ressources
- **Ansible** : Configuration automatique des équipements via playbooks YAML
- **Python** : Exemple de script simple pour interagir avec l’API NSO

---

## Structure

nso-iac-project/
├── ansible/
│ ├── playbook.yml
│ └── inventory.ini
├── terraform/
│ └── main.tf
├── python-scripts/
│ └── nso_api_example.py
├── README.md
└── .gitignore

---

## Prérequis

- NSO installé et accessible sur `http://127.0.0.1:8080` avec utilisateur `admin` / `admin`
- Terraform 1.1.9+
- Ansible installé (version 2.9+ recommandée)
- Python 3 avec `requests`

---

## Installation & utilisation

### 1. Cloner le projet
git clone https://github.com/katrennada/nso-iac-project.git
cd nso-iac-project

### 2. Tester Terraform
cd terraform
terraform init
terraform apply -auto-approve
Tu verras un message confirmant l’exécution d’une ressource simulée.

### 3. Lancer Ansible
cd ../ansible
ansible-playbook -i inventory.ini playbook.yml
Cela pousse une configuration simple vers NSO (simulé ici).

### 4. Tester le script Python
cd ../python-scripts
python3 nso_api_example.py
Il liste les devices présents dans NSO.

### Pourquoi ce projet ?
Même s’il est simple, ce projet illustre la maîtrise simultanée d’outils essentiels du NetDevOps :

Terraform pour gérer l’infrastructure

Ansible pour automatiser la configuration

Python pour interaction directe avec NSO via API

Il peut être étendu facilement, et démontre ta capacité à intégrer plusieurs technologies.

### Améliorations possibles
Ajout d’un vrai environnement NSO avec devices simulés

Playbooks Ansible plus complets et modulaires

Pipelines CI/CD avec Jenkins ou GitHub Actions

Utilisation avancée de Terraform pour déployer des VM ou containers

### Contact
Pour toute question, ouvre une issue sur le repo GitHub.
