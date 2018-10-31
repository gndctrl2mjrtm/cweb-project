import time
import math

from cweb.pbs.qsession import QSession

test_arg = 1e5

def job(arg):
	a,b = 1,1
	for _ in range(int(arg)):
		a,b = b,a+b
	return a 

def main():

    sess = QSession()

    sess.load(job,1)
    sess.load(job,2)
    sess.load(job,3)
    sess.load(job,4)
    sess.load(job,5)

    sess.push()
    sess.pull()

    while not sess.all_complete:
        time.sleep(1)
        print("Waiting...")

    print(sess.results)

if __name__ == "__main__":
	main()