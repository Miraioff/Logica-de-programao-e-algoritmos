# função para a escolha de modelo da camisa
def escolha_modelo():
  while True:
    print('''
MCS - Manga Curta Simples R$ 1,80
MLS - Manga Longa Simples R$ 2,10
MCE - Manga Curta com Estampa R$ 2,90
MLE - Manga longa com Estampa R$ 3,20
''')
    modelo = str(input('Escolha o modelo desejado: ')).upper()
    if modelo not in ('MCS', 'MLS', 'MCE', 'MLE'):
      print('Modelo Invalido!Tente novamente.')
      continue
    elif modelo == 'MCS':
      return 1.80
    elif modelo == 'MLS':
      return 2.10
    elif modelo == 'MCE':
      return 2.90
    elif modelo == 'MLE':
      return 3.20

# Função para a escolha de quantidade de camisetas
def num_camisa():
  while True:
    try:
      num = int(input('Informe a quantidade de camisetas: '))
    except:
      print(f'O valor informado deve ser númerico')
      print()
      continue
    #Se número de camisetas for menor que 20 não há desconto na venda
    if num < 20:
      return num
    #Se número de camisetas for igual ou maior que 20 e menor que 200, o desconto será de 5%
    elif num >= 20 and num < 200:
      qtd = num - (num * (5/100))
      return qtd
    #Se número de camisetas for igual ou maior que 200 e menor que 2000, o desconto será de 7%
    elif num >= 200 and num < 2000:
      qtd = num - (num * (7/100))
      return qtd
    #Se número de camisetas for igual ou maior que 2000 e menor ou igual que 20000, o desconto será de 12%
    elif num >= 2000 and num <= 20000:
      qtd = num - (num * (12/100))
      return qtd
    #Se número de camisetas for maior que 20000, não é aceito pedidos nessa quantidade de camisetas
    else:
      print(f'Não é aceito pedidos com mais de 20000 camisetas')
      continue
def frete():
  while True:
    print('''
1 - Transportadora R$ 100,00
2 - Sedex R$ 200,00
3 - Retirar na fábrica sem custo extra''')
    print()

    frete = str(input('Escolha uma opção de frete: '))
    if frete not in ('1', '2', '3'):
      print('Opção invalida! escolha uma das três acima.')
      continue
    #Para o adicional de frete por transportadora (1) é cobrado um valor extra de 100 reais
    elif frete == '1':
      return 100.00
    #Para o adicional de frete por Sedex (2) é cobrado um valor extra de 200 reais
    elif frete == '2':
      return 200.00
    #Para o adicional de retirar o pedido na fábrica (0) é cobrado um valor extra de 0 reais
    elif frete == '3':
      return 00.00



print(f'BEM-VINDO A FÁBRICA DE CAMISETA DO FABRÍCIO GONÇALVES')
print()
#chamando as funções
valor_modelo = escolha_modelo()
print()
quantidade_desconto = num_camisa()
print()
valor_frete = frete()
print()
#calculo do total com desconto e frete
total = (valor_modelo * quantidade_desconto) + valor_frete

print(f'O valor total a ser pago é:R$ {total:.2f}')
