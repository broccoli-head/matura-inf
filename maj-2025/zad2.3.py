file = open("dane/symbole.txt")
first_line = file.readline().strip()
file.seek(0)

line_length = len(first_line)
biggest_num = first_line
biggest_result_dec = 0

for line in file:
  line = line.strip()
  result = 0
  
  for i in range(line_length):
    if line[i] == 'o': continue
    elif line[i] == '+': value = 1
    elif line[i] == '*': value = 2
    
    result += 3 ** (line_length - i - 1) * value
  
  if result > biggest_result_dec:
    biggest_result_dec = result
    biggest_num = line

print(biggest_result_dec, biggest_num)