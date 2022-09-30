from calendar import c
from itertools import combinations, product
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

def get_pair_wise_coverage(partition_list):
  combs = list(combinations(partition_list, 2))

  for combination in list(combs):
    if combination[0][:-1] == combination[1][:-1]:
      combs.remove(combination)

  return list(combs)

# ACoC

# f = 2, v = 3, c = 4
acoc_partitions = [['f1', 'f2'], ['v1', 'v2', 'v3'], ['c1', 'c2', 'c3', 'c4']]

def capitalize_partitions(partition_list):
  res = []
  for partition in partition_list:
    part = []
    for element in partition:
      part.append(element.upper())
    res.append(part)
  return res

acoc_partitions = (capitalize_partitions(acoc_partitions))

print(str(acoc_partitions))

def get_all_combinations_coverage(partition_list):
  # make combination for a list with any number of partitions
  combs = list(product(*partition_list))
  print(str(combs))

get_all_combinations_coverage(acoc_partitions)

combinations = get_pair_wise_coverage(partitions)

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
