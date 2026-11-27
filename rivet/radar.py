from .target import Target

min_detection_distance_m  = 1
max_detection_distance_m  = 200

def analyze_targets(target_distance_m_list : list[float]) -> dict[str, list[float] | int]:
    """
    Analyse une liste de cibles pour savoir lesquelles sont dans le champ
    du radar et lesquelles sont en dehors.

    Args:
        target_distance_m_list (list[float]): Liste des distances des cibles
            (en mètres).

    Returns:
        dict: Dictionnaire contenant la liste des distances des cibles dans
            le champ ("detected"), la liste des distances des cibles hors
            champ ("not_detected") et le nombre de cibles dans le champ
            ("count").
    """

    target_detected_list = []
    target_not_detected_list = []

    radar = Radar()

    for target_distance_m in target_distance_m_list:
        if radar.is_target_detectable(target_distance_m):
            target_detected_list.append(target_distance_m)
        else:
            target_not_detected_list.append(target_distance_m)

    return {
        "detected": target_detected_list,
        "not_detected": target_not_detected_list,
        "count": len(target_detected_list)
    }

class Radar():
    def __init__(self, min_detection_distance_m : float = min_detection_distance_m, max_detection_distance_m : float = max_detection_distance_m):
        for detection_distance in [min_detection_distance_m, max_detection_distance_m]:
            if detection_distance is None or isinstance(detection_distance, bool) or not isinstance(detection_distance, (float, int)):
                raise ValueError("Les distances de detection doivent être des flotants ou des entiers")
        if min_detection_distance_m<0 or max_detection_distance_m<0:
            raise ValueError("une distance de détection ne peut pas être négative")
        if min_detection_distance_m>=max_detection_distance_m: 
            raise ValueError("La distance de detection maximale doit être strictement superieur a celle de détection minimale")
        self.min_detection_distance_m = min_detection_distance_m
        self.max_detection_distance_m = max_detection_distance_m

    def is_target_detectable(self, target_distance_m : float) -> bool:
        """
        Vérifie si une cible se trouve dans la portée du radar.

        Args:
            target_distance_m (float): Distance de la cible en mètres.

        Returns:
            bool: True si la cible est détectable, False sinon.

        Raises:
            ValueError: Si la distance est négative.
        """

        if target_distance_m<0:
            raise ValueError("La distance ne peut pas être négative")

        return self.min_detection_distance_m  <= target_distance_m <= self.max_detection_distance_m

    def detect_target(self, target: Target)  -> bool :
        return self.is_target_detectable(target.target_distance_m)
