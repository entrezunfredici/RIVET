# Conventions de code Python

Ce document résume les conventions de style à respecter dans le projet, basées sur la [PEP 8](https://peps.python.org/pep-0008/).

## Sommaire

1. [Conventions de nommage](#1-conventions-de-nommage)
2. [Mise en forme et structure](#2-mise-en-forme-et-structure)
3. [Bonnes pratiques courantes](#3-bonnes-pratiques-courantes)
4. [Tests](#4-tests)
5. [Pour approfondir](#5-pour-approfondir)

---

## 1. Conventions de nommage

| Élément                                | Convention                                                                   | Exemples                            |
| ---------------------------------------- | ---------------------------------------------------------------------------- | ----------------------------------- |
| Variables, fonctions, méthodes, modules | `snake_case` (minuscules séparées par des *underscores*)               | `calculer_total`, `ma_variable` |
| Classes et exceptions                    | `PascalCase` / `CapWords` (majuscule à chaque mot, sans *underscore*) | `MaClasse`, `ErreurConnexion`   |
| Constantes                               | `MAJUSCULES_AVEC_UNDERSCORES`                                              | `TAUX_TVA = 0.2`                  |
| Usage interne                            | un *underscore* initial                                                    | `_attribut_interne`               |
| Usage privé                             | deux *underscores* initiaux (déclenche le *name mangling*)              | `__prive`                         |
| Noms spéciaux (*dunders*)             | entourés de deux *underscores*, réservés au langage                     | `__init__`, `__name__`          |

---

## 2. Mise en forme et structure

- **Indentation** : 4 espaces par niveau (espaces plutôt que tabulations).
- **Longueur de ligne** : 79 caractères maximum (72 pour les commentaires et *docstrings*).
- **Lignes vides** :
  - 2 lignes vides entre les fonctions et classes de premier niveau ;
  - 1 ligne vide entre les méthodes d'une classe.
- **Imports** : en haut du fichier, un par ligne, regroupés dans cet ordre et séparés par une ligne vide :
  1. bibliothèque standard ;
  2. bibliothèques tierces ;
  3. modules locaux.

```python
import os
import sys

import requests

from rivet import config
```

---

## 3. Bonnes pratiques courantes

### Comparaisons et booléens

Utiliser `is None` / `is not None`, et tester directement la valeur de vérité.

```python
# Correct
if valeur is None:
    ...
if items:
    ...

# À éviter
if valeur == None:
    ...
if len(items) > 0:
    ...
```

### Vérification de type

Préférer `isinstance` à une comparaison directe de types.

```python
# Correct
if isinstance(obj, MonType):
    ...

# À éviter
if type(obj) is MonType:
    ...
```

### Annotations de type

Ajouter des *type hints* sur les signatures complexes pour faciliter la relecture et l'analyse statique.

```python
def saluer(nom: str) -> str:
    return f"Bonjour {nom}"
```

### Lever une exception

Utiliser le mot-clé `raise`.

```python
def diviser(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Le diviseur ne peut pas être nul")
    return a / b
```

### Opérations booléennes entre deux variables

Utiliser les opérateurs `and`, `or` et, pour le « ou exclusif » (xor), l'opérateur `^`.

| Opération  | Opérateur | Exemple     |
| ----------- | ---------- | ----------- |
| ET          | `and`    | `a and b` |
| OU          | `or`     | `a or b`  |
| OU exclusif | `^`      | `a ^ b`   |

> `xor` n'existe pas en Python : il n'y a pas de mot-clé de ce nom. Pour deux booléens, `a ^ b` (ou `a != b`) donne le résultat attendu.

### Outils d'automatisation

Appliquer ces règles automatiquement avec un formateur ou un *linter* : **Ruff**, **Black** ou **Flake8**.

---

## 4. Tests

### Itérer sur un dictionnaire

`.items()` permet de récupérer à la fois les clés et les valeurs.

```python
for target_distance, response in test_distance_dict.items():
    ...
```

### Séries de valeurs de test

Quand une même logique de test est appliquée à plusieurs valeurs, utiliser `@pytest.mark.parametrize` plutôt qu'une boucle `for` dans le test. Chaque valeur devient un test indépendant : un échec n'interrompt pas les autres et pytest indique précisément la valeur fautive.

Regrouper les cas dans un dictionnaire `{entrée: résultat attendu}` et le passer à `parametrize` via `.items()`. Une réponse de type `str` désigne le message d'une exception attendue.

```python
test_distance_dict = {-1: "La distance ne peut pas être négative", 0: False, 1: True, 200: True, 200.1: False}


@pytest.mark.parametrize("target_distance, response", test_distance_dict.items())
def test_target_distance_detection(target_distance, response):
    if isinstance(response, str):
        with pytest.raises(ValueError, match=response):
            is_target_detectable(target_distance)
    else:
        assert is_target_detectable(target_distance) == response
```

### Valeurs limites

Tester les valeurs situées juste en dessous, sur et juste au-dessus de chaque borne. Pour une portée radar de 1 à 200 m :

| Distance | Résultat attendu |
| -------- | ---------------- |
| 0,5 m    | `False`          |
| 199,9 m  | `True`           |
| 200 m    | `True`           |
| 200,1 m  | `False`          |

### Nom des fonctions de test

Chaque fonction de test doit avoir un nom unique dans son module : une seconde définition du même nom écrase la première, qui n'est alors jamais exécutée.

---

## 5. Pour approfondir

- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [Tutoriel PEP 8 (DataCamp)](https://www.datacamp.com/fr/tutorial/pep8-tutorial-python-code)
- [Découvrez les conventions Python (OpenClassrooms)](https://openclassrooms.com/fr/courses/7160741-ecrivez-du-code-python-maintenable/7187494-decouvrez-les-conventions-python)
- [Conventions PEP 8 (koor.fr)](https://koor.fr/Python/SupportObjet/slide13.wp)
- [PEP 8 (forge.apps.education.fr)](https://schane-lune.forge.apps.education.fr/1nsi/05_langage-programmation/pep8/)
