print(f'BEM-VINDO AO SISTEMA DE RH DO FABRÍCIO GONÇALVES')
print()
print()
lista_funcionario = []
id_global = 4139583
#função para cadastrar um funcionário
def cadastrar_funcionario(id:int):
  print(f'{"MENU CADASTRAR FUNCIONÁRIO":-^55}')
  print(f'Id do Funcionário: {id_global}')
  nome = input('Informe o nome do funcionário: ')
  setor = input('Informe o setor do funcionário: ')
  salario = float(input('Informe o salário do funcionário: '))

  funcionario = {'id': id, 'nome': nome, 'setor': setor, 'salario': salario }
  lista_funcionario.append(funcionario.copy())

def consutar_funcionarios():
  #Enquanto o usuário não escolher a opção 4, o menu consultar funcionários deve se repetir.
  while True:
    print(f'{"MENU CONSUTAR FUNCIONÁRIO":-^55}')
    print('''
  1 - Consutar todos funcionários
  2 - Consutar funcionário por Id
  3 - Consutar funcionários por Setor
  4 - Retornar ao menu
  ''')
    opc = input('>>>')
    #Se Consultar Todos, apresentar todos os funcionários com todos os seus dados cadastrados
    if opc == '1':
      for funcionario in lista_funcionario:
        for chave in funcionario:
          print(f'{chave}: {funcionario[chave]}')
    #Se Consultar por Id, solicitar ao usuário que informe um id, e apresentar o funcionário específico com todos os seus dados cadastrados
    elif opc == '2':
      id_informado = int(input('Informe o id a ser buscado: '))
      for funcionario in lista_funcionario:
        if funcionario['id'] == id_informado:
          for chave in funcionario:
            print(f'{chave}: {funcionario[chave]}')
    #Se Consultar por Setor, solicitar ao usuário que informe o setor, e apresentar o(s) funcionário(s) do setor com todos os seus dados cadastrados
    elif opc == '3':
      setor_informado = input('Informe o setor: ')
      for funcionario in lista_funcionario:
        if funcionario['setor'] == setor_informado:
          for chave in funcionario:
            print(f'{chave}: {funcionario[chave]}')
    #Se Retornar ao menu, deve-se retornar ao menu principal (return)
    elif opc == '4':
      return
    #Se Entrar com um valor diferente de 1, 2, 3 ou 4, printar “Opção inválida" e repetir a pergunta
    else:
      print('Opção Invalida!')
      continue
    print()

def remover_funcionario():
  while True:
    print(f'{"MENU REMOVER FUNCIONÁRIO":-^55}')
    try:
      id_informado = int(input('Informe o id a ser removido: '))
      funcionario_encontrado = False

      for funcionario in lista_funcionario:
        if funcionario['id'] == id_informado:
          lista_funcionario.remove(funcionario)
          print('Funcionário removido com sucesso!')
          funcionario_encontrado = True
          break
      if funcionario_encontrado:
        return
      else:
        print('Id Invalido!Tente Novamente')
    except ValueError:
      print('Entrada Invalida! Digite um número para o id.')

while True:
  print(f'{"MENU PRINCIPAL":-^55}')
  print('''
1 - Cadastra funcionário
2 - Consutar funcionário(s)
3 - Remover funcionário
4 - Sair
''')
  opc = input('>>>')
  #Se Cadastrar Funcionário, chamar a função cadastrar_funcionario(id_ global) e em seguida, incrementar em um id_ global (no menu principal)
  if opc == '1':
    cadastrar_funcionario(id_global)
    id_global += 1
    print()
  #Se Consultar Funcionário, chamar função consultar_funcionario ()
  elif opc == '2':
    consutar_funcionarios()
    print()
  #Se Remover Funcionário, chamar função remover_funcionario()
  elif opc == '3':
    remover_funcionario()
    print()
  #Se Encerrar Programa, sair do menu (e com isso acabar a execução do código
  elif opc == '4':
    break
  #Se Entrar com um valor diferente de 1, 2, 3 ou 4, printar “Opção inválida" e repetir a pergunta
  else:
    print('Opção Invalida!')
