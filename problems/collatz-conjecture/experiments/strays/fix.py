with open('experiments/codex_k_surprise_threshold.py', 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('OPEN.\n10\n\n12-line pure Python', 'OPEN.\n\n12-line pure Python')
c = c.replace("\n20\n\"\"\"", "\n\"\"\"")
with open('experiments/codex_k_surprise_threshold.py', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed.')
print('---DOC---')
print(open('experiments/codex_k_surprise_threshold.py', 'r', encoding='utf-8').read().split('"""', 2)[1][:650])