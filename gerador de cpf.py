print('BEM VINDO AO GERADOR DE CPF PRIMEIRO DIGITE 9 NÚMEROS')
n1 = int(input('PRIMEIRO NÚMERO: ')) 
n2 = int(input('SEGUNDO NÚMERO: ')) 
n3 = int(input('TERCEIRO NÚMERO: ')) 
n4 = int(input('QUARTO NÚMERO: ')) 
n5 = int(input('QUINTO NÚMERO: ')) 
n6 = int(input('SEXTO NÚMERO: ')) 
n7 = int(input('SÉTIMO NÚMERO: ')) 
n8 = int(input('OITAVO NÚMERO: ')) 
n9 = int(input('NONO NÚMERO: ')) 

print('PROCESSANDO... ') 

r1 = n1 * 10
r2 = n2 * 9
r3 = n3 * 8
r4 = n4 * 7
r5 = n5 * 6
r6 = n6 * 5
r7 = n7 * 4
r8 = n8 * 3
r9 = n9 * 2

s = r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8 + r9

print('AGUARDE...') 

s2 = s * 10
s3 = s2 % 11

p1 = n1 * 11
p2 = n2 * 10
p3 = n3 * 9
p4 = n4 * 8
p5 = n5 * 7
p6 = n6 * 6
p7 = n7 * 5
p8 = n8 * 4
p9 = n9 * 3
p10 = s3 * 2
g2 = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10

g1 = g2 * 10
g3 = g1 % 11
print('O SEU CPF É: {}{}{}{}{}{}{}{}{}-{}{}'.format(n1, n2, n3, n4, n5, n6, n7, n8, n9, s3, g3))
