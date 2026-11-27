import pytest

from rivet import Target

test_targets_values_list = [
    ("T001",150.0,20.0),
    ("T002",170.0,50.0),
    ("T003",50.0,0),
    ("T004",70.0,-10)
]

@pytest.mark.parametrize("target_id, target_distance_m, radial_velocity_m_s", test_targets_values_list)
def test_create_target_with_possible_values(target_id, target_distance_m, radial_velocity_m_s):
    test_target = Target(target_id, target_distance_m, radial_velocity_m_s)
    assert test_target.target_id == target_id
    assert test_target.target_distance_m == target_distance_m
    assert test_target.radial_velocity_m_s == radial_velocity_m_s

test_targets_impossible_values = [
    ("",150.0,20.0,"l'id ne peut pas être vide"),
    ("T002",-170.0,50.0, "une distance ne peut pas être négative"),
    ("T003","test",0, "la distance doit être un flottant ou un int"),
    ("T004",70.0,{"radial velocity":-10}, "la vélocitée radiale doit être un flottant ou un int")
]

@pytest.mark.parametrize("target_id, target_distance_m, radial_velocity_m_s, error", test_targets_impossible_values)
def test_create_target_with_impossible_values(target_id, target_distance_m, radial_velocity_m_s, error):
    with pytest.raises(ValueError, match=error):
        Target(target_id, target_distance_m, radial_velocity_m_s)

test_moving_target_list = [
    ("T001",100.0,-10.0,3,70),
]

@pytest.mark.parametrize("target_id, target_distance_m, radial_velocity_m_s, duration_s, destination_m", test_moving_target_list)
def test_moving_target(target_id, target_distance_m, radial_velocity_m_s, duration_s, destination_m):
    moving_target = Target(target_id, target_distance_m, radial_velocity_m_s)
    moving_target.advance_time(duration_s)
    assert moving_target.target_distance_m == destination_m
