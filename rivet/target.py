
class Target():
    def __init__(self, target_id: str, target_distance_m: float, radial_velocity_m_s: float):
        if not isinstance(target_id, str) or not target_id.strip():
            raise ValueError("l'id ne peut pas être vide")
        if target_distance_m is None or isinstance(target_distance_m, bool) or not isinstance(target_distance_m, (int, float)):
            raise ValueError("la distance doit être un flottant ou un int")
        if radial_velocity_m_s is None or isinstance(radial_velocity_m_s, bool) or not isinstance(radial_velocity_m_s, (int, float)):
            raise ValueError("la vélocitée radiale doit être un flottant ou un int")
        if target_distance_m < 0:
            raise ValueError("une distance ne peut pas être négative")
        self.target_id = target_id
        self.target_distance_m = target_distance_m
        self.radial_velocity_m_s = radial_velocity_m_s

    def advance_time(self, duration_s: float) -> None:
        """
        Modifie la position de la cible en focntion de sa vitesee et de la durée.

        Args:
            duration_s (float): Durée en secondes du déplacement.

        Raises:
            ValueError: Si la durée est négative.
            ValueError: Si la durée n'est pas au bon format.
            ValueError: Si la durée si la destination est négative.
        """
        if duration_s is None or isinstance(duration_s, bool) or not isinstance(duration_s, (float, int)):
            raise ValueError("Une durée doit être exprimée en entier ou en flotant")
        if duration_s < 0:
            raise ValueError("Une durée ne peut pas être négative")
        destination = self.target_distance_m + (self.radial_velocity_m_s * duration_s)
        if destination >= 0:
            self.target_distance_m = destination
        else:
            raise ValueError("La destination ne peut pas être négative")
        self.target_distance_m = destination
