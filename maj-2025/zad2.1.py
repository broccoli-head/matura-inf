file = open("dane/symbole.txt")

for line in file:
  line = line.strip()
  reversed_line = ""
  line_length = len(line)

  for i in range(line_length):
    reversed_line += line[line_length - i - 1]

  if line == reversed_line:
    print(line)
  
file.close()