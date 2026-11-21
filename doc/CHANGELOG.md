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
