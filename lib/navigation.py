
# value is a list of str(nodes) adjacent to key str(node)
adjacencies = {
  #pickup zone
  'start_zone': ['start_int'],
  'bay1': ['bay1_int'],
  'bay2': ['bay2_int'],
  'bay3': ['bay3_int'],
  'bay4': ['bay4_int'],

  #pickup intersections
  'bay1_int': ['ol6_int', 'bay2_int', 'bay1'],
  'bay2_int': ['start_int', 'bay1_int', 'bay2'],
  'start_int': ['start_zone', 'bay2_int', 'bay3_int'],
  'bay3_int': ['start_int', 'bay4_int', 'bay3'],
  'bay4_int': ['pl1_int', 'bay3_int', 'bay4'],

  #lower orange zone
  'ol6_int': ['bay1_int', 'ol6_port', 'ol5_int'],
  'ol5_int': ['ol6_int', 'ol5_port', 'ol4_int'],
  'ol4_int': ['ol5_int', 'ol4_port', 'ol3_int'],
  'ol3_int': ['ol4_int', 'ol3_port', 'ol2_int'],
  'ol2_int': ['ol3_int', 'ol2_port', 'ol1_int'],
  'ol1_int': ['ol2_int', 'ol1_port', 'ol_cross'],
  'ol_cross': ['ol1_int', 'orange_side_corner'],
  'ol6_port': ['ol6_int'],
  'ol5_port': ['ol5_int'],
  'ol4_port': ['ol4_int'],
  'ol3_port': ['ol3_int'],
  'ol2_port': ['ol2_int'],
  'ol1_port': ['ol1_int'],

  #lower purple zone
  'pl1_int': ['bay4_int', 'pl1_port', 'pl2_int'],
  'pl2_int': ['pl1_int', 'pl2_port', 'pl3_int'],
  'pl3_int': ['pl2_int', 'pl3_port', 'pl4_int'],
  'pl4_int': ['pl3_int', 'pl4_port', 'pl5_int'],
  'pl5_int': ['pl4_int', 'pl5_port', 'pl6_int'],
  'pl6_int': ['pl5_int', 'pl6_port', 'pl_cross'],
  'pl_cross': ['pl6_int', 'purple_side_corner'],
  'pl6_port': ['pl6_int'],
  'pl5_port': ['pl5_int'],
  'pl4_port': ['pl4_int'],
  'pl3_port': ['pl3_int'],
  'pl2_port': ['pl2_int'],
  'pl1_port': ['pl1_int'],

  #far side of map (lower ramp side)
  'orange_side_corner': ['ol_cross', 'rl_int'],
  'purple_side_corner': ['pl_cross', 'rl_int'],
  'rl_int': ['orange_side_corner', 'purple_side_corner', 'ru_centre_int'],

  #upper side of ramp
  'ru_centre_int': ['ru_orange_int', 'ru_purple_int'],
  'ru_orange_int': ['ru_centre_int', 'ou1_int'],
  'ru_purple_int': ['ru_centre_int', 'pu6_int'],

  #upper orange zone 
  'ou1_int': ['ru_orange_int', 'ou1_port', 'ou2_int'],
  'ou2_int': ['ou1_int', 'ou2_port', 'ou3_int'],
  'ou3_int': ['ou2_int', 'ou3_port', 'ou4_int'],
  'ou4_int': ['ou3_int', 'ou4_port', 'ou5_int'],
  'ou5_int': ['ou4_int', 'ou5_port', 'ou6_int'],
  'ou6_int': ['ou5_int', 'ou6_port', 'ou_cross'],
  'ou_cross': ['ou6_int'],
  'ou6_port': ['ou6_int'],
  'ou5_port': ['ou5_int'],
  'ou4_port': ['ou4_int'],
  'ou3_port': ['ou3_int'],
  'ou2_port': ['ou2_int'],
  'ou1_port': ['ou1_int'],

  #upper purple zone 
  'pu1_int': ['pu_cross', 'pu1_port', 'pu2_int'],
  'pu2_int': ['pu1_int', 'pu2_port', 'pu3_int'],
  'pu3_int': ['pu2_int', 'pu3_port', 'pu4_int'],
  'pu4_int': ['pu3_int', 'pu4_port', 'pu5_int'],
  'pu5_int': ['pu4_int', 'pu5_port', 'pu6_int'],
  'pu6_int': ['pu5_int', 'pu6_port', 'ru_purple_int'],
  'pu_cross': ['pu1_int'],
  'pu6_port': ['pu6_int'],
  'pu5_port': ['pu5_int'],
  'pu4_port': ['pu4_int'],
  'pu3_port': ['pu3_int'],
  'pu2_port': ['pu2_int'],
  'pu1_port': ['pu_cross']}

# value is a tuple (x, y) representing coordinates of each key str(node)
coords = {
    # --- Pickup Zone (bottom) ---
    'start_zone': (8, 0),
    'start_int': (8, 3),
    'bay1': (0, 0),
    'bay2': (3, 0),
    'bay3': (13, 0),
    'bay4': (16, 0),
    'bay1_int': (0, 3),
    'bay2_int': (3, 3),
    'bay3_int': (13, 3),
    'bay4_int': (16, 3),

    # --- Lower Orange Zone (left) ---
    'ol6_int': (0, 9),
    'ol5_int': (0, 10),
    'ol4_int': (0, 11),
    'ol3_int': (0, 12),
    'ol2_int': (0, 13),
    'ol1_int': (0, 14),
    'ol6_port': (2, 9),
    'ol5_port': (2, 10),
    'ol4_port': (2, 11),
    'ol3_port': (2, 12),
    'ol2_port': (2, 13),
    'ol1_port': (2, 14),
    'ol_cross': (0, 15),
    'orange_side_corner': (0, 21),

    # --- Lower Purple Zone (right) ---
    'pl1_int': (16, 9),
    'pl2_int': (16, 10),
    'pl3_int': (16, 11),
    'pl4_int': (16, 12),
    'pl5_int': (16, 13),
    'pl6_int': (16, 14),
    'pl1_port': (14, 9),
    'pl2_port': (14, 10),
    'pl3_port': (14, 11),
    'pl4_port': (14, 12),
    'pl5_port': (14, 13),
    'pl6_port': (14, 14),
    'pl_cross': (16, 15),
    'purple_side_corner': (16, 21),

    # --- Ramp Intersections (top) ---
    'rl_int': (8, 21),
    'ru_centre_int': (8, 7),
    'ru_orange_int': (6, 7),
    'ru_purple_int': (10, 7),

    # --- Upper Orange Line (left top) ---
    'ou1_int': (6, 11),
    'ou2_int': (6, 12),
    'ou3_int': (6, 13),
    'ou4_int': (6, 14),
    'ou5_int': (6, 15),
    'ou6_int': (6, 16),
    'ou1_port': (4, 11),
    'ou2_port': (4, 12),
    'ou3_port': (4, 13),
    'ou4_port': (4, 14),
    'ou5_port': (4, 15),
    'ou6_port': (4, 16),
    'ou_cross': (6, 18),

    # --- Upper Purple Line (right top) ---
    'pu6_int': (10, 11),
    'pu5_int': (10, 12),
    'pu4_int': (10, 13),
    'pu3_int': (10, 14),
    'pu2_int': (10, 15),
    'pu1_int': (10, 16),
    'pu6_port': (12, 11),
    'pu5_port': (12, 12),
    'pu4_port': (12, 13),
    'pu3_port': (12, 14),
    'pu2_port': (12, 15),
    'pu1_port': (12, 16),
    'pu_cross': (10, 18),
}

#truth table for line follow decisionmaking
truth_table = {
    "1,1,1,1": "stop",
    "1,1,1,0": "stop",
    "1,1,0,0": "stop",
    "1,0,1,0": "stop",
    "0,1,0,1": "stop",
    "0,0,1,1": "stop",
    "0,1,1,1": "stop",
    "0,1,1,0": "straight",
    "0,0,1,0": "right",
    "0,1,0,0": "left",
    "0,0,0,1": "stop",
    "1,0,0,0": "stop",
    "0,0,0,0": "stop"
}

# args are str(start), str(goal)
# returns list of str(nodes) in path
def Bfs(start, end, graph):
    queue = [[start]]
    visited = {start}
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            print (path)
            return path
        for n in graph.get(node, []):
            if n not in visited:
                visited.add(n)
                queue.append(path + [n])

# returns "left", "right", "straight", or "back"
# args are three tuples representing coordinates (x, y)
def Turn_Direction(p1, p2, p3):
    v1 = (p2[0]-p1[0], p2[1]-p1[1])
    v2 = (p3[0]-p2[0], p3[1]-p2[1])
    cross = v1[0]*v2[1] - v1[1]*v2[0]
    dot = v1[0]*v2[0] + v1[1]*v2[1]
    if cross > 0:
        return "left"
    elif cross < 0:
        return "right"
    else:
      return "straight" if dot > 0 else "back"

#args are list of str(nodes) in path, and coords dict
#returns list of "left", "right", "straight", or "back" instructions
def Directions(path, coords):
    turns = []
    for i in range(1, len(path)-1):
        turns.append(Turn_Direction(coords[path[i-1]], coords[path[i]], coords[path[i+1]]))
    print(turns)
    return turns

# args are str(qr_string)
# returns str(node)
#use string manip, output of form "xxN_port"
#input of form "Rack X, Upper/Lower, N" STRING NOT LIST OF STRINGS
def Translate_QR(qr_string):
    # extract letters from input string, MAKE SURE TO LOWERCASE
    rack = qr_string[5].lower()  # 'a' or 'b'
    if rack == 'a':
        colour = 'o'  # orange
    else:
        colour = 'p'  # purple

    level = qr_string[8].lower()  # 'u' or 'l'
    number = qr_string[15]  # '1' to '6'

    node = f"{colour}{level}{number}_port"
    print (node)
    return node

# args are str(start), str(end)
# returns list of "left", "right", "straight", or "back" instructions
# CALL THIS FROM MAIN PROGRAM, IT DOES EVERYTHING
def Turns(start, end):
    print(end)
    node_sequence = Bfs(start, end, adjacencies)
    turn_sequence = Directions(node_sequence, coords)
    print(turn_sequence)
    return turn_sequence