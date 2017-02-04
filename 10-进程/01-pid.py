import os

pid = os.fork()
pid2 = os.fork()
print('pid = %d pid2 = %d'%(pid, pid2))
