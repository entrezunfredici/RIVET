import pytest
from unittest.mock import Mock
from rivet import Radar, RadarMonitor

radar_config = {"min_detection_distance_m": 10, "max_detection_distance_m": 200}

test_monitor_list = [
    (radar_config,150,True),
]

@pytest.mark.parametrize("radar,distance_m,detection",test_monitor_list)
def test_monitor(radar, distance_m, detection):
    radar_instance = Radar(radar["min_detection_distance_m"],radar["max_detection_distance_m"])
    radar_sensor = Mock()
    radar_monitor = RadarMonitor(radar_instance, radar_sensor)

    radar_sensor.read_distance_m.return_value = distance_m

    assert radar_monitor.check_detection() == detection
    radar_sensor.read_distance_m.assert_called_once_with()

test_monitor_failed_sensor_list = [
    # un timeout est converti en RuntimeError
    (radar_config, TimeoutError("Le capteur ne répond pas"), RuntimeError, "La détection a échouée"),
    (radar_config, TimeoutError(), RuntimeError, "La détection a échouée"),
    # les autres erreurs du capteur remontent telles quelles
    (radar_config, ConnectionError("Capteur déconnecté"), ConnectionError, "Capteur déconnecté"),
    (radar_config, OSError("Erreur matérielle"), OSError, "Erreur matérielle"),
    # valeurs invalides renvoyées par le capteur
    (radar_config, -1, ValueError, "La distance ne peut pas être négative"),
    (radar_config, None, TypeError, "not supported"),
    (radar_config, "150", TypeError, "not supported"),
]

@pytest.mark.parametrize("radar,sensor_result,error,message", test_monitor_failed_sensor_list)
def test_monitor_with_fail(radar, sensor_result, error, message):
    radar_instance = Radar(radar["min_detection_distance_m"], radar["max_detection_distance_m"])
    radar_sensor = Mock()
    radar_monitor = RadarMonitor(radar_instance, radar_sensor)

    radar_sensor.read_distance_m.side_effect = [sensor_result]

    with pytest.raises(error, match=message):
        radar_monitor.check_detection()
    radar_sensor.read_distance_m.assert_called_once_with()
