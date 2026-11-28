from .radar import Radar

class RadarMonitor():

    def __init__(self, radar_instance: Radar, radar_sensor):
        self.radar_instance = radar_instance
        self.radar_sensor = radar_sensor

    def check_detection(self) -> bool:
        try:
            return self.radar_instance.is_target_detectable(self.radar_sensor.read_distance_m())
        except TimeoutError as error:
            raise RuntimeError("La détection a échouée") from error
