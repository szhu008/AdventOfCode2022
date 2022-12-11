import numpy as np

objs = []
ops  = []
div_by = []
true_throw  = []
false_throw = []

with open('test.txt', 'r') as fin:
    for line in fin:
        if line.startswith('Monkey'):
            objs.append(eval(f"[ {next(fin).split(':')[1]} ]"))
            ops.append( compile(next(fin).split('= ')[1].strip() , "<string>" , "eval"))
            div_by.append(int( next(fin).split('by ')[1] ))
            true_throw.append( int( next(fin).split('monkey ')[1]))
            false_throw.append( int( next(fin).split('monkey ')[1]))

n_monkey = len(objs)
monkey_count = np.zeros(n_monkey)
mod = np.prod(div_by)

for rnds in range(10000):
    for i in range(n_monkey):
        monkey_count[i] += len(objs[i])
        for old in objs[i]:
            new = eval(ops[i]) % mod # black magic
            if new % div_by[i] == 0:
                objs[true_throw[i]].append(new)
            else:
                objs[false_throw[i]].append(new)
        objs[i] = []

monkey_count.sort()
print(monkey_count[-2] * monkey_count[-1])

