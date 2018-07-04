import os
os.getcwd() # pwd
os.chdir('..')
os.system('cd Python')


import shutil
shutil.copfile('os.py', 'imp.py')
shutil.move('./python.exe', '..')


import glob
print(glob.glob(*.py))


import sys
print(sys.argv)

sys.stderr.write("Writing to stderr")
sys.exit()


import re
re.findall(r'\bf[a-z]*', 'what fell fight had fast')




import math
a = math.sin(math.pi / 2)
b = math.log(1000, 10)
print(a, b)


import random
a = random.choice([7, 39, 15])
b = random.sample(ramge(100), 10)
c = random.random()
d = random.randrange(10)
print(a, b, c, d)


import statistics
m = statistics.mean(b)
n = statistics.median(b)
p = statistics.variance(b)
print(m, n, p)
