# TP_OOP - Travaux Pratiques en Programmation Orientée Objet

## 📋 Description

Ce projet regroupe des exercices pratiques en Python couvrant les **structures de données fondamentales** et les **bonnes pratiques de programmation**.

## 📂 Structure du projet

```
tp0/
├── tuples.py           # Exercices sur les tuples (immuables)
├── ensembles.py        # Exercices sur les ensembles (sets)
├── dictionnaires.py    # Exercices sur les dictionnaires
├── qualite.py          # Exercices de qualité de code
├── test_recalibrer.py  # Tests unitaires pour recalibrer()
└── README.md           # Ce fichier
```

## 🎯 Contenu des exercices

### 1. **tuples.py** - Tuples et déballage
- `afficher_releve()` : Affichage formaté d'un relevé capteur
- `recalibrer()` : Recalibration de la valeur d'un capteur dans une liste de tuples

**Concepts** : Déballage de tuples, indexation, immuabilité

### 2. **ensembles.py** - Opérations sur les ensembles
- Intersection, union, différence entre deux ensembles
- Ajout et retrait d'éléments dans un ensemble
- Vérification que les opérations ne modifient pas les ensembles originaux

**Concepts** : Sets, opérateurs `&`, `|`, `-`, immutabilité

### 3. **dictionnaires.py** - Dictionnaires imbriqués
- Accès aux valeurs dans un dictionnaire
- Modification des quantités de pièces
- Ajout de nouveaux modèles
- Agrégation de données (total par type de pièce)

**Concepts** : Dictionnaires, boucles imbriquées, agrégation

### 4. **qualite.py** - Amélioration de la qualité du code
- Refactorisation d'une fonction de calcul de coût
- Élimination des enchainements de `elif` répétitifs
- Suppression du code mort

**Concepts** : Lisibilité, maintenabilité, DRY (Don't Repeat Yourself)

## 🧪 Tests unitaires

### Exécuter les tests pour `recalibrer`

```bash
python -m pytest tp0/test_recalibrer.py -v
```

Ou avec unittest :

```bash
python tp0/test_recalibrer.py
```

### Couverture des tests

10 cas de test incluant :
- ✅ Recalibration (premiers, milieu, dernier capteur)
- ✅ Préservation des autres capteurs
- ✅ Gestion des cas limites (zéro, négatif, inexistant)
- ✅ Vérification des types et structures

## ⚙️ Installation

Aucune dépendance externe requise. Python 3.6+ suffit.

```bash
# Cloner le repository
git clone https://github.com/AnassChhibi/TP_OOP.git
cd TP_OOP

# Exécuter un fichier
python tp0/tuples.py
```

## 📝 Exemples d'utilisation

### Recalibrer un capteur

```python
from tp0.tuples import recalibrer

releves = [
    ("laser_avant", 2.35, "m"),
    ("laser_arriere", 1.10, "m"),
    ("gyroscope", 87.5, "deg")
]

# Recalibrer le laser avant à 2.40 m
nouveaux_releves = recalibrer(releves, "laser_avant", 2.40)
print(nouveaux_releves[0])  # ("laser_avant", 2.40, "m")
```

### Opérations sur les ensembles

```python
from tp0.ensembles import robots_double_mission

robots_exploration = {"R2", "R5", "R7"}
robots_transport = {"R5", "R9", "R7", "R3"}

# Robots avec les deux missions
double_mission = robots_double_mission(robots_exploration, robots_transport)
print(double_mission)  # {"R5", "R7"}
```

### Gestion de stock

```python
from tp0.dictionnaires import quantite_piece, total_pieces

pieces_stock = {
    "ModeleA": {"moteurs": 10, "capteurs": 25, "roues": 40},
    "ModeleB": {"moteurs": 6, "capteurs": 15, "roues": 24},
}

# Calculer le total de pièces
totaux = total_pieces(pieces_stock)
print(totaux)  # {"moteurs": 16, "capteurs": 40, "roues": 64}
```

## 🚨 Points d'amélioration

### ⚠️ Fonction `recalibrer()` - Mutation de liste
La fonction modifie la liste originale. Il est recommandé d'utiliser `releves.copy()` pour éviter les effets de bord.

### 🔧 Fonction `cout_deplacement_propre()` - Refactorisation
Trop de conditions `elif` répétitives. Utiliser un dictionnaire pour mapper les terrains à leurs coefficients.

## 📚 Concepts Python couverts

| Concept | Fichier | Remarques |
|---------|---------|----------|
| Tuples | `tuples.py` | Immuables, déballage |
| Sets | `ensembles.py` | Opérateurs `&`, `\|`, `-` |
| Dictionnaires | `dictionnaires.py` | Imbriqués, boucles |
| Tests unitaires | `test_recalibrer.py` | unittest, setUp |
| Refactorisation | `qualite.py` | DRY, lisibilité |
