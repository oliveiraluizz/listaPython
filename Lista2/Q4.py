N = int(input())

c = 0
v = 0
l = 0

while N != 0:
    
  c +=1
  N -=1
  if N == 0:
    break
  
  v += 1
  N -=1
  if N == 0:
    break
  
  l += 1
  N -=1
  if N == 0:
    break

print("Chapeuzinho Vermelho ", c)
print("Vovozinha ", v)
print("Lobo Mau ", l)