def letter_occ(searched, word):
  counter = 0
  for letter in word:
    if letter is searched:
      counter += 1
  
  return counter

def common_letter_occ(letter, word1, word2):
  return min(letter_occ(letter, word1), letter_occ(letter, word2))


def main():
  maxSum = 0
  result = ""

  with open("dane/pary.txt") as file:
    for line in file:
      currSum = 0
      letter_set = set()
      words = line.split()
      
      for word in words:
        for letter in word:
          letter_set.add(letter)
      
      for letter in letter_set:
        currSum += common_letter_occ(letter, words[0], words[1])
      
      if currSum > maxSum:
        maxSum = currSum
        result = words[0] + " " + words[1]
  
  print(maxSum, result)

main()