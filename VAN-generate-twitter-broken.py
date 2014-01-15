# Requires twitter libraries and I couldn't get it to work. Oh well.
# Generates a random combination of a verb, adjective, and noun

from twitter.api import Twitter
from random import randint

v_f = open("verb.txt")
a_f = open("adj.txt")
n_f = open("noun.txt")

def file_line_count(f):
    lines = f.readlines()
    i = 0
    for l in lines:
            i += 1
    return i

def roll_van():
	v_rand = randint(0, v_n-1)
	a_rand = randint(0, a_n-1)
	n_rand = randint(0, n_n-1)

	v_f.seek(0)
	a_f.seek(0)
	n_f.seek(0)
	
	v = v_f.readlines()[v_rand].strip("\n")
	a = a_f.readlines()[a_rand].strip("\n")
	n = n_f.readlines()[n_rand].strip("\n")

	print(v_rand, a_rand, n_rand)
	van = v + " " + a + " " + n

	return van

v_n = file_line_count(v_f)
a_n = file_line_count(a_f)
n_n = file_line_count(n_f)

van = roll_van()
print(van)

while True:
	var = input("[y/n]?").lower()
	if var == "y":
		break
	elif var == "n":
		van = roll_van()
		print(van)

v_f.close()
a_f.close()
n_f.close()

post = van + ", go! #vangetgoing"
print(post)

twitter = Twitter("json", "intd_VANgo","INTD450SweatSocks")
twitter.statuses.update(status=post)