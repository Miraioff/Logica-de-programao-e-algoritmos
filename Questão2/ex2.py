lin = f'-'*66
# cabeçalho e cardápio
print(f'{"Bem-Vindo a loja de marmitas do Fabrício Gonçalves":-^66}')
print(f'{"Cardápio":-^66}')
print(lin)
print(f'-|{"TAMANHO":^10}|{"BIFE ACEBOLADO (BA)":^25}|{"FILÉ DE FRANGO (FF)":^25}|-')
print(f'-|{"P":^10}|{"R$ 16.00":^25}|{"R$ 15.00":^25}|-')
print(f'-|{"M":^10}|{"R$ 18.00":^25}|{"R$ 17.00":^25}|-')
print(f'-|{"G":^10}|{"R$ 22.00":^25}|{"R$ 21.00":^25}|-')
print(lin)
#inicia as variáveis valor_total e valor em zero
valor_total = 0
valor = 0
#laço principal
while True:
  #laço para garantir que o usuário não erre na entrada do sabor
  while True:
    sabor = str(input('Informe o sabor desejado (BA/FF): ')).upper()
    #só permite que o programa continue caso seja  informado um dos sabores disponiveis
    if sabor == 'BA' or sabor == 'FF':
      break
    else:
        print('Sabor inválido.Tente novamente.')
  print()
  while True:
    #laço para garantir que o usuário não erre na entrada do tamnho do pedido
    tam = str(input('Informe o tamanho desejado (P/M/G): ')).upper()
    #só permite que o programa continue caso seja  informado um dos tamanhos disponiveis
    if tam == 'P' or tam == 'M' or tam == 'G':
      break
    else:
        print('Tamanho inválido.Tente novamente.')
  print()
  # verifica o sabor escolhido
  if sabor == 'BA':
    if tam == 'P':
      valor = 16.00
    elif tam == 'M':
      valor = 18.00
    else:
      valor = 22.00
  elif sabor == 'FF':
    if tam == 'P':
      valor = 15.00
    elif tam == 'M':
      valor = 17.00
    else:
      valor = 21.00
  # Soma os valores de cada pedido e guarda na variável valor_total
  valor_total += valor

  print(f'Você pediu {"Bife Acebolado" if sabor == "BA" else "Filé de Frango"} no tamanho {tam}: R$ {valor:.2f}')

  # Verifica se o usuário quer pedir mais alguma coisa
  # Se não quiser o programa se encerra e mostra o valor total a ser pago
  fim = str(input('Deseja mais alguma coisa? (S/N): ')).upper()
  if fim == 'S':
    print()
    continue
  break
print()
print(f'O valor total a ser pago: R$ {valor_total:.2f}')
