# sumTwoNumbers

from behave import *

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

#
@given('una lista vacia')
def impl(context):
	context.elements = []

@given('la lista {seq}')
def impl(context, seq):
	elements = seq.split(",")
	context.elements = elements

@when('compruebo si es palindroma')
def impl(context):
	context.result = palindroma(context.elements)

@then('el resultado es {res}')
def impl(context, res):
	expected = res == "True"
	assert (context.result == expected)
	
	
	