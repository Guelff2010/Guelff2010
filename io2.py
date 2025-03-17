print ('BEM VINDO AO HOTEL GUSTTA')
totalpessoas = int(input('quantas pessoas no quarto'))

opcao1 = 1
opcao2 = 2
opcao3 = 3

if totalpessoas == opcao1 :
 print('insira seus dados')
 nome = input('insira seu nome')
 idade = input('insira sua idade ')
 print ('seja bem vindo', nome)
elif totalpessoas == opcao2 :
 print('insira seus dados')
 nome = input('insira o nome dos hospedes')
 idade = input('digite a idade de vcs ')
 print ('seja bem vindos', nome)
elif totalpessoas == opcao3 :
 print('insira seus dados ')
 nome = input('insira os nomes')
 idade = input('insira as idades')
 print ('!SURUBÃO!')
 print ('seja bem vindo')
 print (f'''OPCAO DE ESTADIA
pobre: R$ 50,00 por dia
medio: R$ 100,00 por dia
!LUXO!: R$ 500,00 por dia
        ''')
pobre = 'pobre'
medio = 'medio' 
luxo = '!LUXO'

pagamento = int (input('qual o meodo de pagamento  1/2/3'))

if pagamento == '1':
      print('gerando QRCODE...')
elif pagamento == '2':
      print('gerando nota')
elif pagamento == '3':
      print('retire o cartão')

print ('pagamento feito nunca mais volte')
