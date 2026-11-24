MIN_DETECTION_DISTANCE  = 1
MAX_DETECTION_DISTANCE  = 200

def is_target_detectable(target_distance : float) -> bool:
    """
    Vérifie si une cible se trouve dans la portée du radar.

    Args:
        target_distance (float): Distance de la cible en mètres.

    Returns:
        bool: True si la cible est détectable, False sinon.

    Raises:
        ValueError: Si la distance est négative.
    """

    if target_distance<0:
        raise ValueError("La distance ne peut pas être négative")

    return MIN_DETECTION_DISTANCE  <= target_distance <= MAX_DETECTION_DISTANCE 


def analyze_targets(target_distance_list : list[float]) -> dict[str, list[float] | int]:
    """
    Analyse une liste de cibles pour savoir lesquelles sont dans le champ
    du radar et lesquelles sont en dehors.

    Args:
        target_distance_list (list[float]): Liste des distances des cibles
            (en mètres).

    Returns:
        dict: Dictionnaire contenant la liste des distances des cibles dans
            le champ ("detected"), la liste des distances des cibles hors
            champ ("not_detected") et le nombre de cibles dans le champ
            ("count").
    """

    target_detected_list = []
    target_not_detected_list = []

    for target_distance in target_distance_list:
        if is_target_detectable(target_distance):
            target_detected_list.append(target_distance)
        else:
            target_not_detected_list.append(target_distance)

    return {
        "detected": target_detected_list,
        "not_detected": target_not_detected_list,
        "count": len(target_detected_list)
    }

class Radar():
    def __init__(self, min_detection_distance : float = MIN_DETECTION_DISTANCE, max_detection_distance : float = MAX_DETECTION_DISTANCE):
        self.min_detection_distance = min_detection_distance
        self.max_detection_distance = max_detection_distance

    
