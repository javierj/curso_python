
def buildNumList(seq):
	elements = seq.split(",")
	numList = {}
	for e in elements:
		numList.append(int(e))
	return numList

def palindroma(elems):
	if len(elems) < 2:
	    return False;

	mitad = len(elems) / 2;
	ultimoelemento = len(elems)-1;
	
	for i in range(0, mitad): 
		if elems[i].strip() != elems[ultimoelemento - i].strip():  
			return False 
	return True 

if __name__ == '__main__':
    lista = buildNumList("1, 2, 3, 4, 5, 6")
    result = palindroma(lista)


	
	