file = open("dane/symbole.txt")
lines = file.readlines()
line_count = len(lines)
square_count = 0

for i in range(line_count - 2):
  line = lines[i].strip()

  for j in range(len(line) - 2):
    if line[j] == line[j + 1] == line[j + 2]:
      sign = line[j]
      isSquare = True

      for a in range(3):
        if lines[i + 1][j + a] != sign or lines[i + 2][j + a] != sign:
          isSquare = False
          break
      
      if isSquare:
        square_count += 1
        print(square_count, i + 2, j + 2)
      


file.close()