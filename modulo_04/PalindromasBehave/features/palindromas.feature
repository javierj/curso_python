Feature: Deteccion de listas palindromas
  In order to detectar si una lista es palindroma
  As usuario
  I want indicar una lista y saber si es palindroma o no

  Scenario: lista vacia
     Given una lista vacia 
      when compruebo si es palindroma
      then el resultado es False
  
  Scenario Outline: varias listas
     Given la lista <lista>
      when compruebo si es palindroma
      then el resultado es <resultado>
	  
  Examples: Listas 
   | lista   | resultado |
   | 1       | False     |
   | 1, 2    | False     |
   | 1, 1    | True      |   
   | 1, 3, 1 | True      |
   