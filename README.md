# Lógica de Programação e Algoritmos

Este repositório contém as resoluções dos exercícios propostos na disciplina de **Lógica de Programação e Algoritmos**. Cada questão aborda diferentes conceitos fundamentais de programação, como estruturas condicionais, laços de repetição, funções, manipulação de listas e dicionários.

---

## 🚀 Tecnologias Utilizadas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

---

## Questão 1: Cálculo de Juros por Parcela

Este programa simula o cálculo de juros para uma venda parcelada no cartão de crédito, aplicando taxas diferentes com base no número de parcelas escolhido pelo cliente.

### 📋 Enunciado

Uma empresa de vendas precisa de um aplicativo que calcule o valor total de uma compra e o valor de cada parcela, aplicando juros compostos de acordo com a quantidade de parcelas:

- **Até 3 parcelas:** 0% de juros
- **De 4 a 5 parcelas:** 4% de juros
- **De 6 a 8 parcelas:** 8% de juros
- **De 9 a 12 parcelas:** 16% de juros
- **A partir de 13 parcelas:** 32% de juros

### ✅ Requisitos do Código

- **A.** Exibir uma mensagem de boas-vindas com o nome completo do autor.
- **B.** Solicitar ao usuário o `valor do pedido` e a `quantidade de parcelas`.
- **C.** Implementar a lógica de cálculo de juros conforme a tabela.
- **D.** Calcular e exibir o `valor final de cada parcela` e o `valor total` da compra.
- **E.** Utilizar as estruturas `if`, `elif` e `else`.
- **F.** Adicionar comentários para explicar o código.

### 🧪 Cenários de Teste

- **G.** A saída deve mostrar a mensagem de boas-vindas.
- **H.** A saída deve apresentar um exemplo de parcelamento com juros (4 parcelas ou mais), exibindo o valor da parcela e o total.

---

## Questão 2: Pedido em uma Loja de Marmitas

Este programa simula um sistema de pedidos para uma loja de marmitas, permitindo que o cliente escolha o sabor e o tamanho, acumule o valor total e faça múltiplos pedidos em uma única execução.

### 📋 Enunciado

Desenvolver a interface de um cliente para uma loja que vende marmitas de **Bife Acebolado (BA)** e **Filé de Frango (FF)** nos seguintes tamanhos e preços:

| Tamanho | Bife Acebolado (BA) | Filé de Frango (FF) |
| :---: | :---: | :---: |
| **P** | R$ 16,00 | R$ 15,00 |
| **M** | R$ 18,00 | R$ 17,00 |
| **G** | R$ 22,00 | R$ 21,00 |

### ✅ Requisitos do Código

- **A.** Exibir uma mensagem de boas-vindas com o nome do autor e um cardápio.
- **B.** Solicitar o sabor (`BA` ou `FF`) e validar a entrada.
- **C.** Solicitar o tamanho (`P`, `M` ou `G`) e validar a entrada.
- **D.** Utilizar `if/elif/else` aninhados para calcular o preço.
- **E.** Usar um acumulador para somar o valor total dos pedidos.
- **F.** Perguntar se o cliente deseja adicionar mais itens. Se sim, repetir o processo; senão, encerrar e exibir o total.
- **G.** Utilizar as estruturas `while`, `break` e `continue`.
- **H.** Adicionar comentários explicativos no código.

### 🧪 Cenários de Teste

- **I.** A saída deve mostrar a mensagem de boas-vindas e o cardápio.
- **J.** Testar um pedido onde o usuário insere um sabor inválido.
- **K.** Testar um pedido onde o usuário insere um tamanho inválido.
- **L.** Simular um pedido com dois itens diferentes (sabor e tamanho) e exibir o valor total.

---

## Questão 3: Sistema de Vendas de Camisetas

Este programa calcula o custo total de um pedido de camisetas em atacado, aplicando descontos por volume e adicionando custos de frete.

### 📋 Enunciado

Desenvolver um sistema de cobrança para uma fábrica de camisetas com os seguintes produtos e regras de negócio:

**Modelos e Preços:**
- **MCS** (Manga Curta Simples): R$ 1,80
- **MLS** (Manga Longa Simples): R$ 2,10
- **MCE** (Manga Curta com Estampa): R$ 2,90
- **MLE** (Manga Longa com Estampa): R$ 3,20

**Descontos por Volume:**
- **Menos de 20 camisetas:** Sem desconto
- **20 a 199 camisetas:** 5% de desconto
- **200 a 1.999 camisetas:** 7% de desconto
- **2.000 a 20.000 camisetas:** 12% de desconto
- **Acima de 20.000 camisetas:** Pedido não aceito

**Opções de Frete:**
- **Retirar na fábrica (0):** R$ 0,00
- **Transportadora (1):** R$ 100,00
- **Sedex (2):** R$ 200,00

### ✅ Requisitos do Código

- **A.** Exibir uma mensagem de boas-vindas com o nome do autor.
- **B.** Criar uma função `escolha_modelo()` que retorna o valor do modelo escolhido e valida a entrada.
- **C.** Criar uma função `num_camisetas()` que retorna a quantidade de camisetas com o desconto aplicado e valida a quantidade máxima e entradas não numéricas (`try/except`).
- **D.** Criar uma função `frete()` que retorna o valor do frete e valida a opção escolhida.
- **E.** Calcular o total a pagar no escopo principal do programa (`main`).
- **F.** Implementar tratamento de exceções com `try/except`.
- **G.** Adicionar comentários relevantes.

### 🧪 Cenários de Teste

- **H.** A saída deve mostrar a mensagem de boas-vindas.
- **I.** Testar um pedido onde o usuário insere um modelo inválido.
- **J.** Testar um pedido onde o usuário excede o número máximo de camisetas.
- **K.** Simular um pedido completo com entradas válidas para modelo, quantidade e frete.

---

## Questão 4: Gerenciamento de Funcionários

Este programa implementa um sistema CRUD (Criar, Ler, Atualizar, Deletar) para gerenciar os registros de funcionários de uma empresa, utilizando listas e dicionários.

### 📋 Enunciado

Desenvolver um software de gerenciamento de funcionários com o seguinte menu:

  1.  **Cadastrar Funcionário**
  2.  **Consultar Funcionário**
      1.  Consultar Todos
      2.  Consultar por ID
      3.  Consultar por Setor
      4.  Retornar ao menu
  3.  **Remover Funcionário**
  4.  **Encerrar Programa**

### ✅ Requisitos do Código

- **A.** Exibir uma mensagem de boas-vindas com o nome do autor.
- **B.** Utilizar uma lista global `lista_funcionarios` e uma variável `id_global`.
- **C.** Criar a função `cadastrar_funcionario(id)` para adicionar um novo funcionário (em um dicionário) à lista.
- **D.** Criar a função `consultar_funcionarios()` com um submenu para as diferentes opções de consulta.
- **E.** Criar a função `remover_funcionario()` que remove um funcionário da lista pelo ID.
- **F.** Implementar o menu principal no escopo do programa, que chama as funções correspondentes.
- **G.** Utilizar uma lista de dicionários para armazenar os dados.
- **H.** Adicionar comentários explicativos.

### 🧪 Cenários de Teste

- **I.** A saída deve mostrar a mensagem de boas-vindas.
- **J.** Cadastrar 3 funcionários, sendo 2 do mesmo setor.
- **K.** Realizar uma consulta de "todos os funcionários".
- **L.** Realizar uma consulta por ID.
- **M.** Realizar uma consulta por setor que retorne os 2 funcionários cadastrados.
- **N.** Remover um funcionário e, em seguida, consultar todos novamente para verificar a remoção.
