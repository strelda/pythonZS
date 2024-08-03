from collections import defaultdict

def norm(x):
    return "".join(sorted(x))

N = int(input())
slovnik = defaultdict(list)
for _ in range(N):
    slovo = input()
    slovnik[norm(slovo)].append(slovo)

M = int(input())
for _ in range(M):
    slovo = input()
    print(" ".join(sorted(slovnik[norm(slovo)])))
