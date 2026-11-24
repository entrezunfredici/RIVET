from rivet.radar import is_target_detectable, analyze_targets
from rivet import Radar
import pytest

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


@pytest.mark.parametrize("target_distance, response", test_distance_dict.items())
def test_is_target_detectable(target_distance, response):
    if isinstance(response, str):
        with pytest.raises(ValueError, match=response):
            is_target_detectable(target_distance)
    else:
        assert is_target_detectable(target_distance)==response

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

@pytest.mark.parametrize("target_distance_list, response", test_targets_list)
def test_analyze_targets(target_distance_list, response):
    if isinstance(response, str):
        with pytest.raises(ValueError, match=response):
            analyze_targets(target_distance_list)
    else:
        assert analyze_targets(target_distance_list) == response

test_targets_safe_list = [[0, 0.5, 0.5, 1, 1, 50, 50, 199.9, 200, 200.1]]

@pytest.mark.parametrize("target_distance_list", test_targets_safe_list)
def test_safe_list(target_distance_list):
    target_distance_copy_list=target_distance_list.copy()
    analyze_targets(target_distance_list)
    assert target_distance_list == target_distance_copy_list


def test_radar_class_with_default_values():
    test_radar = Radar()
    assert test_radar.min_detection_distance == 1.0
    assert test_radar.max_detection_distance == 200.0

test_radar_list = [
    (5,100),
    (10,500),
    (0.5,50),
]

@pytest.mark.parametrize("min_detection_distance, max_detection_distance", test_radar_list)
def test_radar_class(min_detection_distance,max_detection_distance):
    test_radar = Radar(min_detection_distance, max_detection_distance)
    assert test_radar.min_detection_distance == min_detection_distance
    assert test_radar.max_detection_distance == max_detection_distance

