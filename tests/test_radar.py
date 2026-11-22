from rivet.radar import is_target_detectable
import pytest

test_distance_dict = {-1:"La distance ne peut pas être négative", 0:False, 1:True, 20:True, 50:True, 70:True, 500:False, 0.5:False, 199.9:True, 200:True, 200.1:False}

@pytest.mark.parametrize("target_distance, response", test_distance_dict.items())
def test_target_distance_detection(target_distance, response):
    if isinstance(response, str):
        with pytest.raises(ValueError, match=response):
            is_target_detectable(target_distance)
    else:
        assert is_target_detectable(target_distance)==response
