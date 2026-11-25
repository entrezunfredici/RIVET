import pytest

from rivet import Target

test_targets_values_list = [("T001",150.0,20.0),("T002",170.0,50.0),("T003",150.0,0)]

@pytest.mark.parametrize("target_id, distance_m, speed_m_s", test_targets_values_list)
def test_create_target(target_id, distance_m, speed_m_s):
    test_target = Target(target_id, distance_m, speed_m_s)
    assert test_target.target_id == target_id
    assert test_target.distance_m == distance_m
    assert test_target.speed_m_s == speed_m_s
