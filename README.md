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
🔄 Workflow GitHub Actions (ci.yml)
yaml
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
📸 Démonstration
1️⃣ Configuration de la Protection de Branche
<img width="967" height="819" alt="Capture d'écran 2026-04-13 233404" src="https://github.com/user-attachments/assets/c8150367-958e-402e-8419-b96f16887ff4" /><img width="360" height="881" alt="Capture d'écran 2026-04-13 233634" src="https://github.com/user-attachments/assets/f78448de-4edc-44d4-b0dd-60b75e899e74" /><img width="968" height="659" alt="Capture d'écran 2026-04-13 234615" src="https://github.com/user-attachments/assets/eabdb1b5-a635-42d7-875d-73b0d4a2dce4" />
2️⃣ Test d'Échec - Code Cassé
Pull Request avec code contenant une erreur :

<img width="964" height="841" alt="Capture d'écran 2026-04-13 235020" src="https://github.com/user-attachments/assets/91642f82-0e2b-4498-886a-281858d403af" /><img width="968" height="683" alt="Capture d'écran 2026-04-13 235458" src="https://github.com/user-attachments/assets/e4bf3adb-7055-47b6-abfc-ba6f9005f174" />
3️⃣ Test de Succès - Code Corrigé
<img width="973" height="767" alt="Capture d'écran 2026-04-14 000101" src="https://github.com/user-attachments/assets/c86f8105-96ca-48e2-9681-c6afef2f600a" /><img width="965" height="725" alt="Capture d'écran 2026-04-14 000245" src="https://github.com/user-attachments/assets/32607600-e6bd-4613-8dae-d92eb740c7b2" />
🧪 Tests Unitaires
python
def test_calculer_prix_total(self):
    # Panier vide → 0€
    self.assertEqual(calculer_prix_total([]), 0)
    
    # Un article → 20€
    panier = [(10, 2)]
    self.assertEqual(calculer_prix_total(panier), 20)
    
    # Multiples articles → 35€
    panier = [(10, 2), (5, 3)]
    self.assertEqual(calculer_prix_total(panier), 35)

def test_verifier_age(self):
    self.assertEqual(verifier_age(15), "Mineur")
    self.assertEqual(verifier_age(18), "Majeur")
    self.assertEqual(verifier_age(25), "Majeur")
Résultat des tests
bash
$ pytest test_app.py -v

==================== test session starts =====================
collected 2 items

test_app.py::TestApp::test_calculer_prix_total PASSED [✓]
test_app.py::TestApp::test_verifier_age PASSED [✓]

===================== 2 passed in 0.02s ======================
🔐 Règle de Protection Configurée
Paramètre	Valeur	Statut
Branche cible	main	✅
Require status checks	Activé	✅
Checks requis	"Le Bouclier de Production"	✅
Require branches up to date	Activé	✅
Détail de la configuration
yaml
Branch protection rule:
  - Branche cible: main
  - Require status checks: ✅ Activé
  - Checks requis: "Le Bouclier de Production"
  - Require branches up to date: ✅ Activé
📊 Résumé des Comportements
Situation	Statut Pipeline	Bouton Merge
Code cassé (erreur syntaxe)	❌ Échec (rouge)	🚫 Bloqué (grisé)
Code corrigé (tests OK)	✅ Succès (vert)	🔓 Actif (vert)
👤 Auteur
DjamelSteephen

Projet réalisé dans le cadre de la formation CI/CD

📅 Date
14 Avril 2026
