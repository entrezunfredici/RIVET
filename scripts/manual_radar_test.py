from rivet.radar import is_target_detectable

distances = [0, 0.5, 1, 50, 199.9, 200, 200.1, -10]

for distance in distances:
    try:
        result = is_target_detectable(distance)
        print(f"Distance : {distance} m → {result}")
    except ValueError as error:
        print(f"Distance : {distance} m → Erreur : {error}")
