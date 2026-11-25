
class Target():
    def __init__(self, target_id: str, distance_m: float, radial_velocity_m_s: float):
        if not isinstance(target_id, str) or not target_id.strip():
            raise ValueError("l'id ne peut pas être vide")
        if distance_m is None or isinstance(distance_m, bool) or not isinstance(distance_m, (int, float)):
            raise ValueError("la distance doit être un flottant ou un int")
        if radial_velocity_m_s is None or isinstance(radial_velocity_m_s, bool) or not isinstance(radial_velocity_m_s, (int, float)):
            raise ValueError("la vélocitée radiale doit être un flottant ou un int")
        if distance_m < 0:
            raise ValueError("une distance ne peut pas être négative")
        self.target_id = target_id
        self.distance_m = distance_m
        self.radial_velocity_m_s = radial_velocity_m_s

