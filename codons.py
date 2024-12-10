def create_codon_dict(file_path):
  file = open(file_path)
  rows = file.readlines()
  file.close()
  file_path = "data/codons.txt"

  shaked_dict= {}
  for row in rows:
    row= row.strip().split()
    shaked_dict [row[0]]= row[2]
  print(shaked_dict)

  return shaked_dict


