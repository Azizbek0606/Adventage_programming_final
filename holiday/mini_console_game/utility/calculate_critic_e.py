def calculate_critic_e(entity, weapon):
    e = entity.get_type
    w = weapon.get_type

    if e == w:
        return 50

    if {e, w} == {2, 3}:
        return 50

    if e in (1, 2, 3) and w in (1, 2, 3):
        return 10

    return 0