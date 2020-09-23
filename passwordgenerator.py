import random,string
p_len=int(input('Length of password : '))
p_characters=string.ascii_letters+string.digits#+string.punctuation
password=[]
for x in range(p_len):
    password.append(random.choice(p_characters))
print(''.join(password))
#print(password)