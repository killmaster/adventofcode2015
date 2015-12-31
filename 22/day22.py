import sys
import itertools
import random

spell_names = set("missiles", "drain", "shield", "poison", "recharge")

spells = {
    "missiles": (53, 4, 0),
    "drain": (73, 2, 2),
    "shield": (113, 6, 7),
    "poison": (173, 6, 3),
    "recharge": (229, 5, 101)
    }

effects = [
    (0,0),  # shield
    (0,0),  # poison
    (0,0)   # recharge
    ]

boss_hp = 71 
boss_damage = 10

def fight(move_set):
  cost = 0
  while True:
    current_move = move_set.pop()
    if current_move == "missiles":
      
    current_boss_hp -= max(current_damage-current_boss_armor, 1)
    if current_boss_hp <= 0:
      #print "Beat the Boss"
      return True
    current_hp -= max(current_boss_damage-current_armor, 1)
    if current_hp <= 0:
      #print "Died"
      return False
 
def part1():
  result = 0 
  move_sets = set()
  for i in range(100000):
    move_sets.add(random.sample(spell_names),20)
  for move_set in move_sets:
    resulting_cost, did_i_win = fight(move_set)
    if did_i_win:
      results.add(resulting_cost)
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
