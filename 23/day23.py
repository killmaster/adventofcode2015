input_list = []

with open('input.txt') as f:
  for line in f:
    input_list.append(line.rstrip().replace(',','').split())

def interpreter(instructions, starting_registers):
  registers = starting_registers
  i = 0
  while i < len(instructions) and i >= 0:
    instruction = instructions[i]
    if    instruction[0] == 'hlf':
      registers[instruction[1]] /= 2
      i += 1
    elif  instruction[0] == 'tpl':
      registers[instruction[1]] *= 3
      i += 1
    elif  instruction[0] == 'inc':
      registers[instruction[1]] += 1
      i += 1
    elif  instruction[0] == 'jmp':
      i += int(instruction[1])
    elif  instruction[0] == 'jie':
      if registers[instruction[1]] % 2 == 0:
        i += int(instruction[2])
      else:
        i += 1
    elif  instruction[0] == 'jio':
      if registers[instruction[1]] == 1:
        i += int(instruction[2])
      else:
        i += 1
  return registers

registers = {
      'a': 0,
      'b': 0
      }

print 'part1:', interpreter(input_list, registers)['b']
registers['a'] = 1
registers['b'] = 0
print 'part2:', interpreter(input_list, registers)['b']
