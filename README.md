# 🛡️ Le Bouclier de Production - CI/CD Pipeline

## 📋 Description du Projet

Ce projet démontre la mise en place d'un pipeline d'Intégration Continue (CI) utilisant **GitHub Actions** pour protéger la branche `main` contre les déploiements de code non testé.

### Problème résolu
> *"Hier, lors du déploiement de notre application Campus-Event, un développeur a poussé directement sur la branche main un code contenant une faute de syntaxe. Conséquence : les serveurs ont crashé, et l'application a été indisponible pendant 3 heures."*

**Solution :** Un robot (GitHub Actions) vérifie automatiquement chaque Pull Request avant fusion.

---

## 🎯 Fonctionnalités

- ✅ Déclenchement automatique sur chaque Pull Request vers `main`
- 🔍 Vérification de la syntaxe avec **Flake8** (linter)
- 🧪 Exécution des tests unitaires avec **Pytest**
- 🔒 Protection de branche obligeant les checks à passer
- 🚫 Blocage automatique du merge en cas d'échec

---

## 🏗️ Structure du Projet
<img width="587" height="471" alt="image" src="https://github.com/user-attachments/assets/6ddb004a-d6c8-4468-af67-c3d25bb87e82" />



---

## 🛠️ Technologies Utilisées

| Technologie | Version | Rôle |
|-------------|---------|------|
| Python | 3.11 | Langage de développement |
| GitHub Actions | - | Pipeline CI/CD |
| Flake8 | 7.3.0 | Linter (vérification syntaxe) |
| Pytest | 9.0.3 | Framework de tests |
| Ubuntu Latest | - | Environnement d'exécution |

---

## 📦 Installation Locale

```bash
# 1. Cloner le dépôt
git clone https://github.com/DjamelSteephen/ContinousIntegration.git

# 2. Se déplacer dans le dossier
cd MyProjectCDCI

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Vérifier la syntaxe
flake8 app.py test_app.py

# 5. Exécuter les tests
pytest test_app.py -v


# Workflow GitHub Actions (ci.yml)
name: Le Bouclier de Production

on:
  pull_request:
    branches: [ main ]

jobs:
  security-shield:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    - uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    
    - name: Installer les dépendances
      run: |
        pip install flake8 pytest
    
    - name: Linter avec flake8
      run: flake8 . --count --select=E9,F63,F7,F82 --show-source
    
    - name: Exécuter les tests
      run: python -m pytest test_app.py -v
