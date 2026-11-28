import pytest
from rivet import Radar, Target

target_tracking_list = [
    (
        {
            "min_detection_distance_m":10,
            "max_detection_distance_m":200,
        },
        {
            "target_id": "T001",
            "target_distance_m": 220,
            "radial_velocity_m_s": -10,
        },
        [
            (0,220,False),
            (2,200,True),
            (21,10,True),
            (22,0,False),
        ]
    ),
]

@pytest.mark.parametrize("radar,target,test_points",target_tracking_list)
def test_moving_target(radar, target, test_points):
    radar_instance = Radar(radar["min_detection_distance_m"],radar["max_detection_distance_m"])
    moving_target = Target(target["target_id"], target["target_distance_m"], target["radial_velocity_m_s"])
    last_time_s = 0
    for time_s, distance_m, result in test_points:
        moving_target.advance_time(time_s-last_time_s)
        last_time_s=time_s
        assert moving_target.target_distance_m == distance_m
        assert radar_instance.detect_target(moving_target) == result
        assert moving_target.radial_velocity_m_s == target["radial_velocity_m_s"]
        assert moving_target.target_id == target["target_id"]
