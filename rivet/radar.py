
def is_target_detectable(target_distance: float) -> bool:
    """
    Vérifie si une cible se trouve dans la portée du radar.

    Args:
        target_distance (float): Distance de la cible en mètres.

    Returns:
        bool: True si la cible est détectable, False sinon.

    Raises:
        ValueError: Si la distance est négative.
    """

    min_detection_distance = 1
    max_detection_distance = 200

    if target_distance<0:
        raise ValueError("La distance ne peut pas être négative")

    return min_detection_distance <= target_distance <= max_detection_distance
