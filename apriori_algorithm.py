import pprint
from itertools import combinations

# author: Walter Vives


def open_file(new_file):
  opened_file = open(new_file, "r",encoding='utf-8')
  read_file = opened_file.read()
  new_line_split = read_file.split("\n")
  opened_file.close()
  index = 0
  total_list = []
  for element in new_line_split:
    new_line_split[index] = element.split(",")
    total_list.append(new_line_split[index])
    index += 1 
  return total_list

def get_products(transactions):
  unique_products = set()
  for ticket in transactions:
    for item in ticket:
      unique_products.add(item)
  return unique_products

def frequency(comb, transactions, size_t):
  freq = []
  for combination in comb:
    aux = 0
    for ticket in transactions:
      if set(combination) & set(ticket) == set(combination):
        aux += 1
    freq.append((combination, aux/size_t))
  return freq 

def get_products_filter(filters):
  unique_products = set()
  for bina in filters:
    for item in bina[0]:
      unique_products.add(item)
  return unique_products


def apriori_algorithm(transactions, min_support=0.5):
  tabla = {}
  products = get_products(transactions)
  size_t = len(transactions)
  idx = 1
  while products:
    data = {}
    data["products"] = products
    comb = list(combinations(products,idx))
    freq = frequency(comb, transactions, size_t)
    filters = list(filter(lambda data: data[1] >= min_support, freq))  
    products = get_products_filter(filters)
    data["frequency"] = freq
    data["filters"] = filters
    tabla[idx] = data
    idx += 1
  return tabla

def main():
  file = open_file("data.txt")
  result = apriori_algorithm(file, 0.43)
  final_products = result[3]["filters"]
  #pprint.pprint(final_products)
  pprint.pprint(final_products)


if __name__ == "__main__":
  main()

