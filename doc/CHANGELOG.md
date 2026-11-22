# Changelog

## Sommaire

1. [Mise en place de l'environnement](#1-mise-en-place-de-lenvironnement)
2. [Fonction `is_target_detectable`](#2-fonction-is_target_detectable)
3. [Fonction `analyze_targets`](#3-fonction-analyze_targets)
4. [Développement en TDD de `analyze_targets`](#4-développement-en-tdd-de-analyze_targets)

---

## 1. Mise en place de l'environnement

Mise en place des tests unitaires avec **pytest** :

```bash
python -m pip install pytest
```

---

## 2. Fonction `is_target_detectable`

Détecter si une cible est détectable par le radar.

### User story

> En tant qu'utilisateur, je veux savoir si la cible est dans l'intervalle de détection du radar (entre 1 et 200 m). Si c'est le cas, la fonction retourne `True`, sinon elle retourne `False`.

### Exigences supplémentaires

- Si la distance est négative, la fonction lève une exception `ValueError`.
- La fonction n'affiche rien dans le terminal.
- La fonction possède une *docstring* explicative de son comportement.

### Données d'entrée

| Variable                 | Description                               |
| ------------------------ | ----------------------------------------- |
| `target_distance`        | Distance séparant la cible et le radar    |
| `max_detection_distance` | Distance de détection maximale            |
| `min_detection_distance` | Distance de détection minimale            |

### Algorithme

```text
si target_distance < 0 :
    lever ValueError

si min_detection_distance <= target_distance <= max_detection_distance :
    retourner True
sinon :
    retourner False
```

La comparaison `min_detection_distance <= target_distance <= max_detection_distance` retourne directement `True` ou `False`. L'algorithme se simplifie donc en :

```text
si target_distance < 0 :
    lever ValueError

retourner min_detection_distance <= target_distance <= max_detection_distance
```

> Les bornes (1 m et 200 m) sont incluses dans la zone de détection.

---

## 3. Fonction `analyze_targets`

Analyser plusieurs distances et classer les cibles.

### User story

> En tant qu'utilisateur, j'aimerais connaître la distance entre le radar et chaque objet : recevoir une liste de distances, savoir lesquelles sont dans la zone de détection et lesquelles ne le sont pas, ainsi que le nombre de cibles détectées.

### Contraintes supplémentaires

- Le programme propage un message d'erreur dès qu'une distance est négative, et s'arrête.
- La liste reçue en paramètre n'est pas modifiée.

### Exemple de résultat attendu

Pour les distances `[0, 10, 50, 250, 200]`, la fonction doit retourner :

```python
{
    "detected": [10, 50, 200],
    "not_detected": [0, 250],
    "count": 3
}
```

---

## 4. Développement en TDD de `analyze_targets`

| Étape | Action                                                                                          | Résultat                                       |
| ----- | ----------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| 1     | Rédaction du test unitaire                                                                      |                                                |
| 2     | Lancement du test sans fonction                                                                 | Échec                                          |
| 3     | Scénario « liste de cibles vide » : création de la fonction à vide (`pass`)                    | Échec                                          |
| 4     | Ajout d'un retour avec valeurs à zéro                                                           | Réussite                                       |
| 5     | Ajout d'un scénario avec des valeurs                                                            | Premier scénario réussi, second scénario échoué |
| 6     | Amélioration de la fonction : détection via `is_target_detectable`                              | Les deux scénarios réussis                     |
| 7     | Ajout du scénario avec une valeur négative                                                      |                                                |
| 8     | Relance des tests                                                                               | Les 3 scénarios réussis                        |
