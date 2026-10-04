import math

file = open("dane/symbole.txt")
first_line = file.readline().strip()
file.seek(0)

line_length = len(first_line)
final_sum = 0

for line in file:
  line = line.strip()
  
  for i in range(line_length):
    if line[i] == 'o': continue
    elif line[i] == '+': value = 1
    elif line[i] == '*': value = 2
    
    final_sum += 3 ** (line_length - i - 1) * value


sum_3 = ""
converted_sum_3 = ""
curr_num = final_sum

while curr_num > 0:
  sum_3 += str(curr_num % 3)
  curr_num = math.floor(curr_num / 3)

sum_length = len(sum_3)

for i in range(sum_length):
  curr_digit = sum_3[sum_length - i - 1]

  if curr_digit == '0':
    converted_sum_3 += "o"
  elif curr_digit == '1':
    converted_sum_3 += "+"
  elif curr_digit == '2':
    converted_sum_3 += "*"

print(final_sum, converted_sum_3)