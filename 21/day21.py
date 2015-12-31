import sys
import itertools
"""
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
"""

weapons = {
  (8, 4, 0),
  (10, 5, 0),
  (25, 6, 0),
  (40, 7, 0),
  (74, 8, 0)
}

armor = {
  (0, 0, 0),
  (13, 0, 1),
  (31, 0, 2),
  (53, 0, 3),
  (75, 0, 4),
  (102, 0, 5),
}

rings = {
  (0, 0, 0),
  (0, 0, 0),
  (25, 1, 0),
  (50, 2, 0),
  (100, 3, 0),
  (20, 0, 1),
  (40, 0, 2),
  (80, 0, 3),
}

boss_hp = 103
boss_damage = 9
boss_armor = 2

def fight(current_hp, current_damage, current_armor):
  current_boss_hp = boss_hp
  current_boss_damage = boss_damage
  current_boss_armor = boss_armor

  while True:
    current_boss_hp -= max(current_damage-current_boss_armor, 1)
    if current_boss_hp <= 0:
      #print "Beat the Boss"
      return True
    current_hp -= max(current_boss_damage-current_armor, 1)
    if current_hp <= 0:
      #print "Died"
      return False
 
def part1():
  result = sys.maxint
  for weapon_cost, weapon_damage, _ in weapons:
    for armor_cost, _, armor_value in armor:
      for r_ring,l_ring in itertools.combinations(rings,2):
        char_damage = weapon_damage + r_ring[1] + l_ring[1]
        char_armor  = armor_value + r_ring[2] + l_ring[2]
        #print char_damage, char_armor
        cost = weapon_cost + armor_cost + r_ring[0] + l_ring[0]
        if fight(100, char_damage, char_armor):
          result = min(cost, result)
  return result

def part2():
  result = 0
  for weapon_cost, weapon_damage, _ in weapons:
    for armor_cost, _, armor_value in armor:
      for r_ring,l_ring in itertools.combinations(rings,2):
        char_damage = weapon_damage + r_ring[1] + l_ring[1]
        char_armor  = armor_value + r_ring[2] + l_ring[2]
        #print char_damage, char_armor
        cost = weapon_cost + armor_cost + r_ring[0] + l_ring[0]
        if not fight(100, char_damage, char_armor):
          result = max(cost, result)
  return result
 

print part1()
print part2()
