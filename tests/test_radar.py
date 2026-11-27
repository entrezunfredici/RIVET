from rivet.radar import analyze_targets
from rivet import Radar, Target
import pytest

test_targets_list = [
    ([],{
        "detected": [],
        "not_detected": [],
        "count": 0
    }),
    ([0, 0.5, 1, 50, 199.9, 200, 200.1],{
        "detected": [1, 50, 199.9, 200],
        "not_detected": [0, 0.5, 200.1],
        "count": 4
    }),
    ([10, -1, 50], "La distance ne peut pas être négative"),
    ([0, 0.5, 0.5, 1, 1, 50, 50, 199.9, 200, 200.1],{
        "detected": [1, 1, 50, 50, 199.9, 200],
        "not_detected": [0, 0.5, 0.5, 200.1],
        "count": 6
    }),
]

@pytest.mark.parametrize("target_distance_m_list, response", test_targets_list)
def test_analyze_targets(target_distance_m_list, response):
    if isinstance(response, str):
        with pytest.raises(ValueError, match=response):
            analyze_targets(target_distance_m_list)
    else:
        assert analyze_targets(target_distance_m_list) == response

test_targets_safe_list = [[0, 0.5, 0.5, 1, 1, 50, 50, 199.9, 200, 200.1]]

@pytest.mark.parametrize("target_distance_m_list", test_targets_safe_list)
def test_safe_list(target_distance_m_list):
    target_distance_m_copy_list=target_distance_m_list.copy()
    analyze_targets(target_distance_m_list)
    assert target_distance_m_list == target_distance_m_copy_list


def test_radar_class_without_values():
    test_radar = Radar()
    assert test_radar.min_detection_distance_m == 1.0
    assert test_radar.max_detection_distance_m == 200.0

test_radar_values_list = [
    (5,100),
    (10,500),
    (0.5,50),
]

@pytest.mark.parametrize("min_detection_distance_m, max_detection_distance_m", test_radar_values_list)
def test_radar_class_with_value(min_detection_distance_m,max_detection_distance_m):
    test_radar = Radar(min_detection_distance_m, max_detection_distance_m)
    assert test_radar.min_detection_distance_m == min_detection_distance_m
    assert test_radar.max_detection_distance_m == max_detection_distance_m

test_radar_impossible_values_list = [
    (-5,200,"une distance de détection ne peut pas être négative"),
    (10,-5,"une distance de détection ne peut pas être négative"),
    (100,100,"La distance de detection maximale doit être strictement superieur a celle de détection minimale"),
    (300,100,"La distance de detection maximale doit être strictement superieur a celle de détection minimale"),
    ("5","100","Les distances de detection doivent être des flotants ou des entiers"),
    (None,100,"Les distances de detection doivent être des flotants ou des entiers"),
    (10,False,"Les distances de detection doivent être des flotants ou des entiers"),
    (10,{"name":"kévin","âge":25},"Les distances de detection doivent être des flotants ou des entiers")
]

@pytest.mark.parametrize("min_detection_distance_m, max_detection_distance_m, error", test_radar_impossible_values_list)
def test_radar_class_with_impossible_values(min_detection_distance_m,max_detection_distance_m, error):
    with pytest.raises(ValueError, match=error):
        Radar(min_detection_distance_m, max_detection_distance_m)

test_distance_dict = {
    -1:"La distance ne peut pas être négative",
    0:False,
    1:True,
    20:True,
    50:True,
    70:True,
    500:False,
    0.5:False,
    199.9:True,
    200:True,
    200.1:False
}

@pytest.mark.parametrize("target_distance_m, response", test_distance_dict.items())
def test_is_target_detectable_by_default_radar(target_distance_m, response):
    test_radar = Radar()
    if isinstance(response, str):
        with pytest.raises(ValueError, match=response):
            test_radar.is_target_detectable(target_distance_m)
    else:
        assert test_radar.is_target_detectable(target_distance_m)==response

test_pair_of_radar_list = (
    (
        {"min_detection_distance_m":10, "max_detection_distance_m":200}, 
        {"min_detection_distance_m":50, "max_detection_distance_m":100},
        70,
    ),
)

@pytest.mark.parametrize("radar_1, radar_2, change_max_detection_distance_m", test_pair_of_radar_list)
def test_is_radar_is_independant(radar_1, radar_2, change_max_detection_distance_m):
    test_radar_1 = Radar(radar_1["min_detection_distance_m"],radar_1["max_detection_distance_m"])
    test_radar_2 = Radar(radar_2["min_detection_distance_m"],radar_2["max_detection_distance_m"])
    assert test_radar_1.max_detection_distance_m == radar_1["max_detection_distance_m"]
    test_radar_1.max_detection_distance_m = change_max_detection_distance_m
    assert test_radar_1.max_detection_distance_m == change_max_detection_distance_m
    assert test_radar_2.max_detection_distance_m == radar_2["max_detection_distance_m"]


test_multiple_radar_values_list = [
    (5,100,{
        -1:"La distance ne peut pas être négative",
        0:False,
        1:False,
        5:True,
        50:True,
        100:True,
        500:False,
        0.5:False,
        199.9:False,
        200:False,
        200.1:False
    }),
    (10,500,{
        -1:"La distance ne peut pas être négative",
        0:False,
        1:False,
        20:True,
        50:True,
        70:True,
        500:True,
        0.5:False,
        199.9:True,
        200:True,
        200.1:True
    }),
    (0.5,50,{
        -1:"La distance ne peut pas être négative",
        0:False,
        1:True,
        20:True,
        50:True,
        70:False,
        500:False,
        0.5:True,
        199.9:False,
        200:False,
        200.1:False
    }),
]

@pytest.mark.parametrize("min_detection_distance_m, max_detection_distance_m, test_distance_dict", test_multiple_radar_values_list)
def test_is_target_detectable_by_customs_radar(min_detection_distance_m, max_detection_distance_m, test_distance_dict):
    test_radar = Radar(min_detection_distance_m, max_detection_distance_m)
    for target_distance_m, response in test_distance_dict.items():
        if isinstance(response, str):
            with pytest.raises(ValueError, match=response):
                test_radar.is_target_detectable(target_distance_m)
        else:
            assert test_radar.is_target_detectable(target_distance_m)==response

test_target_detections_list = [
    (
        {
            "min_detection_distance_m":10,
            "max_detection_distance_m":200,
        },{
            "target_id": "T001",
            "target_distance_m": 150,
            "radial_velocity_m_s": 20,
        },
        True
    ),
    (
        {
            "min_detection_distance_m":10,
            "max_detection_distance_m":200,
        },{
            "target_id": "T001",
            "target_distance_m": 250,
            "radial_velocity_m_s": 20,
        },
        False
    ),
    (
        {
            "min_detection_distance_m":10,
            "max_detection_distance_m":200,
        },{
            "target_id": "T001",
            "target_distance_m": 5,
            "radial_velocity_m_s": 20,
        },
        False
    ),
    (
        {
            "min_detection_distance_m":10,
            "max_detection_distance_m":200,
        },{
            "target_id": "T001",
            "target_distance_m": 10,
            "radial_velocity_m_s": 20,
        },
        True
    ),
    (
        {
            "min_detection_distance_m":10,
            "max_detection_distance_m":200,
        },{
            "target_id": "T001",
            "target_distance_m": 200,
            "radial_velocity_m_s": 20,
        },
        True
    ),
    (
        {
            "min_detection_distance_m":50,
            "max_detection_distance_m":100,
        },{
            "target_id": "T001",
            "target_distance_m": 25,
            "radial_velocity_m_s": 20,
        },
        False
    ),
    (
        {
            "min_detection_distance_m":50,
            "max_detection_distance_m":100,
        },{
            "target_id": "T001",
            "target_distance_m": 75,
            "radial_velocity_m_s": 20,
        },
        True
    ),
]

@pytest.mark.parametrize("radar, target, detection_response", test_target_detections_list)
def test_target_detections(radar, target, detection_response):
    test_radar = Radar(radar["min_detection_distance_m"], radar["max_detection_distance_m"])
    test_target = Target(target["target_id"],target["target_distance_m"],target["radial_velocity_m_s"])
    assert test_radar.detect_target(test_target) == detection_response
