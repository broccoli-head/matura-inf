def main():
  with open("dane/pary.txt") as file:
    for line in file:
      [word1, word2] = line.split()

      if len(word1) < 5 or len(word2) < 5:
        continue

      prefixsuffix(word1, word2)
      prefixsuffix(word2, word1)


def prefixsuffix(word1, word2):
  count = 5
  seqCount = 0

  while(count < len(word1) and count < len(word2)):
    prefix = word1[:count]
    if (word2.endswith(prefix)):
      seqCount = count
    count += 1

  if seqCount >= 5:
    print(word1 + " " + word2 + " " + str(seqCount))

main()