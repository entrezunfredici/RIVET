from rivet.radar import is_target_detectable, analyze_targets
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
]

@pytest.mark.parametrize("target_distance_list, response", test_targets_list)
def test_analyze_targets(target_distance_list, response):
    if isinstance(response, str):
        with pytest.raises(ValueError, match=response):
            analyze_targets(target_distance_list)
    else:
        assert analyze_targets(target_distance_list)==response
