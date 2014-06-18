import random

# Main
if __name__ == "__main__":
    bag = [0 for i in range(0, 19)]

    num_tiradas = 10000
    for j in range(1, num_tiradas):
	    resultado = 0
	    for dados in range(0, 3):
		    tirada = random.randint(1, 6)
		    resultado += tirada
	    tmp = bag[resultado]
	    tmp += 1
	    bag[resultado] = tmp

    print("Tiradas: ", num_tiradas)

    for i in range(3, 19):
	    print(i, ", ", bag[i])
    #print(str(bag))

