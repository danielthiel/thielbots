m = {   'spawn': [(7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (5, 2), (6, 2), (12, 2), (13, 2), (3, 3), (4, 3), 
                    (14, 3), (15, 3), (3, 4), (15, 4), (2, 5), (16, 5), (2, 6), (16, 6), (1, 7), (17, 7), (1, 8), (17, 8), (1, 9), 
                    (17, 9), (1, 10), (17, 10), (1, 11), (17, 11), (2, 12), (16, 12), (2, 13), (16, 13), (3, 14), (15, 14), (3, 15), 
                    (4, 15), (14, 15), (15, 15), (5, 16), (6, 16), (12, 16), (13, 16), (7, 17), (8, 17), (9, 17), (10, 17), (11, 17)], 
        'obstacle': [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), 
                        (11, 0), (12, 0), (13, 0), (14, 0), (15, 0), (16, 0), (17, 0), (18, 0), (0, 1), (1, 1), (2, 1),
                         (3, 1), (4, 1), (5, 1), (6, 1), (12, 1), (13, 1), (14, 1), (15, 1), (16, 1), (17, 1), (18, 1), 
                         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (14, 2), (15, 2), (16, 2), (17, 2), (18, 2), (0, 3), (1, 3), 
                         (2, 3), (16, 3), (17, 3), (18, 3), (0, 4), (1, 4), (2, 4), (16, 4), (17, 4), (18, 4), (0, 5), (1, 5), 
                         (17, 5), (18, 5), (0, 6), (1, 6), (17, 6), (18, 6), (0, 7), (18, 7), (0, 8), (18, 8), (0, 9), (18, 9), 
                         (0, 10), (18, 10), (0, 11), (18, 11), (0, 12), (1, 12), (17, 12), (18, 12), (0, 13), (1, 13), (17, 13), 
                         (18, 13), (0, 14), (1, 14), (2, 14), (16, 14), (17, 14), (18, 14), (0, 15), (1, 15), (2, 15), (16, 15), 
                         (17, 15), (18, 15), (0, 16), (1, 16), (2, 16), (3, 16), (4, 16), (14, 16), (15, 16), (16, 16), (17, 16), 
                         (18, 16), (0, 17), (1, 17), (2, 17), (3, 17), (4, 17), (5, 17), (6, 17), (12, 17), (13, 17), (14, 17), 
                         (15, 17), (16, 17), (17, 17), (18, 17), (0, 18), (1, 18), (2, 18), (3, 18), (4, 18), (5, 18), (6, 18), 
                         (7, 18), (8, 18), (9, 18), (10, 18), (11, 18), (12, 18), (13, 18), (14, 18), (15, 18), (16, 18), (17, 18), (18, 18)]
}

MOVE_SPAWN_WEIGTH = 10
MOVE_2FSPAWN_WEIGTH = 5
SUICIDE_WEIGHTS = [(5,10),(10,3)] # List of tuples: (hp_trigger, suicide_weigth)

class Robot:
    def act(self, game):
        me_move = [] # of dict: {'position':(x,y), 'value':int}
        me_attack = []
        me_guard = 0 # nur value
        me_suicide = 0 # nur value

        # Abkuerzungen:
        loc = self.location
        hp = self.hp

        # Ueberpruefe ab im Spawnfeld:
        if loc in m['spawn']:
            for v in get_valid_adjacent_locations(loc):
                me_move.append({'position':v, 'value':MOVE_SPAWN_WEIGTH})

        # Ueberpruefe Abstand zum Spawnfeld:


        # Bestimme Suizid-Gewichtung:
        for element in SUICIDE_WEIGHTS:
            if hp <= element[0]:
                me_suicide = max(me_suicide, element[1])

        # Suche Loesungsweg: Guard > Move > Attack > Suicide:
        do_value = me_guard
        do_loc = loc
        do_action = 'guard'
        for pm in me_move:
            if pm['value'] > do_value:
                do_value = pm['value']
                do_loc = pm['position']
                do_action = 'move'
        for pa in me_attack:
            if pa['value'] > do_value:
                do_value = pa['value']
                do_loc = pa['position']
                do_action = 'attack'
        if me_suicide > do_value:
            do_value = me_suicide
            do_loc = loc
            do_action = 'suicide'

        do_this = [do_action, do_loc]
        print do_this, loc
        return do_this


def get_valid_adjacent_locations(current):
    valid = []
    a = tuple((current[0]+1, current[1]))
    b = tuple((current[0]-1, current[1]))
    c = tuple((current[0], current[1]+1))
    d = tuple((current[0], current[1]-1))
    if a not in m['obstacle'] and a not in m['spawn']:
        valid.append(a)
    if b not in m['obstacle'] and b not in m['spawn']:
        valid.append(b)
    if c not in m['obstacle'] and c not in m['spawn']:
        valid.append(c)
    if d not in m['obstacle'] and d not in m['spawn']:
        valid.append(d)
    return valid


