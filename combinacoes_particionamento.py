from itertools import combinations
import pyperclip

# Particionamento para rp = 3, rs = 3, rpq = 3, rsq = 3
partitions = [ 'rp1', 'rpq1', 'rs2', 'rsq1']

#pair-wise combination of partitions
partitions = [element.upper() for element in partitions]

#solucao alternativa
#combs = [(partition1, partition2) for idx, partition1 in enumerate(partitions) for partition2 in partitions[idx + 1:]]
#print(combs)

def pretty_print_matrix(matrix):
  print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))

def get_requirements(partition_list):
  combs = list(combinations(partition_list, 2))

  for combination in list(combs):
    if combination[0][:-1] == combination[1][:-1]:
      combs.remove(combination)

  return list(combs)


combinations = get_requirements(partitions)


def remove_quot(myStr):
  outputString = ''
  for character in myStr:
    if character == "'":
        continue
    outputString += character
  return outputString


res = remove_quot(str(combinations))
res = res[1:-1]

print(res)
pyperclip.copy(res)
