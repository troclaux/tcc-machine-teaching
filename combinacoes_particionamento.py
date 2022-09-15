from itertools import combinations

partitions = ['n1', 'n2', 'n3', 'm1', 'm2', 'm3', 'mt1', 'mt2', 'mt3']

#pair-wise combination of partitions
partitions = [element.upper() for element in partitions]

#solucao alternativa
#combs = [(partition1, partition2) for idx, partition1 in enumerate(partitions) for partition2 in partitions[idx + 1:]]
#print(combs)


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
