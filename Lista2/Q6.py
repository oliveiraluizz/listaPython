A, D, P= input().split()

a=int(A)
d=int(D)
p=int(P)

F = a + d + p

F1 = (F*100)/110

if F < 110:
    
  if (F1 >= 0) and (F <= 50):
      print("Seu pokemon nao fara progresso em batalhas")
  elif (F1 >= 51) and (F <= 66):   
      print("Seu pokemon esta acima da media")
  elif (F1 >= 67) and (F <= 79):   
      print("Seu pokemon certamente me chamou atencao")    
  elif (F1 >= 80) and (F <= 100):   
      print("Seu pokemon e uma maravilha")   
  
else:
    print("Hum, parece que houve um erro")   

