with open('experiments/codex_k_surprise_threshold.py', 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('Status: OPEN.\n10\n', 'Status: OPEN.\n\n')
c = c.replace('print(\'CF address space climbed by repetition; K caps exceptions.\')\n20\n"""', 'print(\'small orbits K~hundreds bits << K(codex)\')\n"""')
c = c.replace('print("CF address space climbed by repetition; K caps exceptions.")\n20\n"""', 'print(\'small orbits K~hundreds bits << K(codex)\')\n"""')
with open('experiments/codex_k_surprise_threshold.py', 'w', encoding='utf-8') as f:
    f.write(c)
print('Cleaned.')
print(repr(open('experiments/codex_k_surprise_threshold.py', 'r', encoding='utf-8').read().split('"""')[1][:800]))