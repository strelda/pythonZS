import collections

freq = collections.defaultdict(int)

with open('vstup.txt', encoding='utf-8') as f:
    for line in f:
        for i in range(len(line)-1):
            dig = line[i:i+2]
            if dig.isalpha():
                freq[dig.lower()] += 1

with open('vystup.txt', 'w', encoding='utf-8') as g:
    for dig in sorted(freq.keys(), key=lambda k: (-freq[k], k)):
        print(dig, freq[dig], file=g)