import random

#сначала попробовал вот так реализлвать. понял что лишка.
#while True:
#    try:
 #       parol = random.randint(0,9999)
  #      if  parol >= 1000:
   #         break
    #except:
     #   pass

password = random.randint(1000, 9999)

print("вот ваш пароль из 4 символов")
print(password)
#print(parol)

input()# вот такую штуку узнал как делать.
