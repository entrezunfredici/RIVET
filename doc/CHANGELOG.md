Mise en place de l'environnement

miuse en palce des tests unitaires:

installation de pytest:

python -m pip install pytest



Développement

Développement de la fonction permettant de detecter si une cible est détectable par le radar:

User storie

En tant qu'utilisateur je veux savori si la cible est dans l'intervale de détection du radar (entre 1 et 200m), si c'ets el cas je veux que la fonction me retourne True le cas echant qu'elle me retounr false.

Exigences supplémentaires

si la distance est négative la fonction doir retourner une exeption value error

la fonction ne doit rien afficher dans le terminal

la fonction doit avoir une docstring explicative de son comportement

données d'entrées

target_distance ⇒ distance séparant la cible et le radar

max_detection_distance ⇒ distance de detection maximale

min_detection_distance ⇒ distance de detection minimale

Algorythme

si target_distance<0:

	lever ValueError

si min_detection_distance < target_distance < max_detection_distance:

	retourner true

sinon:

	retoruner false

sachant que la comparaison min_detection_distance < target_distance < max_detection_distance peut directement retrouner true ou false

on peut simplifier l'algorythme en :

si target_distance<0:

	lever ValueError

retourner min_detection_distance < target_distance < max_detection_distance

Développer une fonction capable d'analyser plusieurs distances et de classer les cibles.

US : en tant qu'utilisateur j'ailmerais savoir qu'lelle est la distance qu'il y a entre le radar et chaques objets, et donc recevoir une liste de distances, savoir lesquells sont dans la zien de detectione t lesquelles ne le sont pas. Ainsiq ue connaitre le nnombre de cibles détectées 

Contrainte supplémedntaire:

Le programme doit propager un message d'erreur des qu'il y a une distancfe negative, et donc s'arrêter

ne pas modifier la liste reçue en paramètre

### **Exemple de resultat attendu**

Pour les distances `[0, 10, 50, 250, 200]`, la fonction doit retourner :

```
{
    "detected": [10, 50, 200],
    "not_detected": [0, 250],
    "count": 3
}
```
