# Dicionario para adicionar cores a saida do terminal
cor = {'roxo' : '\033[1;35m',
       'vermelho' : '\033[1;31m',
       'amarelo' : '\033[1;33m',
       'limpa' : '\033[m'}

lin = f'{cor['amarelo']}=={cor['limpa']}'*25
print(lin)
print(f'{cor['roxo']}{"BEM VINDO A LOJA DO FABRÍCIO GONÇALVES":^50}{cor['limpa']}')
print(lin)

# inputs do valor do pedido e da quantidade de parcelas
valor_pedido = float(input(f'{cor['roxo']}Informe o valor do pedido: R$ '))
qtd_parcelas = int(input('Informe a quantidade de parcelas: '))
print(lin)

juros = 0
if qtd_parcelas <= 0:
  # se a quantidade de parcelas for <= 0, sera pedido para adicionar uma quantidade maior que 0.
  # O programa ira encerrar
  print(f'{cor['vermelho']} Informe uma quantia de parcelas maior que zero')
  print(lin)
  exit()
else:
  if qtd_parcelas >= 13:
    # se as quantidades de parcelas for >= 13, sera cobrado juros de 32%
    juros = valor_pedido * 0.32

  elif qtd_parcelas >= 9:
    # se as quantidades de parcelas for >= 9 e < 13, os juros será de 16%
    juros = valor_pedido * 0.16

  elif qtd_parcelas >= 6:
    # se as quantidades de parcelas for >= 6 e < 9, os juros será de 8%
    juros = valor_pedido * 0.08

  elif qtd_parcelas >= 4:
    # se a quantidade de parcelas for >= 4 e < 6, terá juros de 4%
    juros = valor_pedido * 0.04
  elif qtd_parcelas < 4:
    juros = 0

  #calculo do valor de cada parcela.
  valor_parcelas = (valor_pedido + juros) / qtd_parcelas
  #calculo do valor total.
  valor_total = valor_parcelas * qtd_parcelas

  print(f'{cor['roxo']}O valor das parcelas é de: R$ {valor_parcelas:.2f}')
  print(f'O valor total parcelado é R$ {valor_total:.2f}{cor['limpa']}')
  print(lin)
