from itertools import combinations, product
import pyperclip

# Partitions

# a = 2
# b = 2
# c = 2
partitions = [['a1', 'a2'], ['b1', 'b2'], ['c1', 'c2']]


def get_pair_wise_coverage(partition_list):
  combs = list(combinations(partition_list, 2))
  result = []
  for i in combs:
    list_buffer = []
    list_buffer = [(x, y) for x in i[0] for y in i[1]]
    for j in list_buffer:
      result.append(j)
  return result

def capitalize_partitions(partition_list):
  res = []
  for partition in partition_list:
    part = []
    for element in partition:
      part.append(element.upper())
    res.append(part)
  return res

partitions = (capitalize_partitions(partitions))


def get_all_combinations_coverage(partition_list):
  # make combination for a list with any number of partitions
  combs = list(product(*partition_list))
  return combs


def remove_quot(myStr):
  outputString = ''
  for character in myStr:
    if character == "'":
      continue
    outputString += character
  return outputString

def convert_partition_to_string(part_input):
  string = ''
  string = str(part_input)
  string = remove_quot(string)
  string = string[1:-1]
  return string

def get_combinations(part_input):
  print('\n (1) Pair-wise coverage \n (2) All combinations coverage \n')
  choice = input("Insira o número do tipo de cobertura desejado: ")
  print()
  if choice == '1':
    print("< Pair-wise coverage >")
    pw = get_pair_wise_coverage(part_input)
    result = convert_partition_to_string(pw)
    print(result)
    pyperclip.copy(result)

  elif choice == '2':
    print("< All combinations coverage >")
    result = convert_partition_to_string(get_all_combinations_coverage(part_input))
    print(result)
    pyperclip.copy(result)

get_combinations(partitions)
