# Sistema de Gerenciamento de Clientes com Cálculo de IMC

Este projeto é um sistema simples para gerenciar o cadastro de clientes em um banco de dados SQLite e calcular o Índice de Massa Corporal (IMC) dos clientes cadastrados.

## Funcionalidades

1. **Criação de tabela**: Garante que a tabela de clientes seja criada no banco de dados.
2. **Cadastro de clientes**:
   - Adição em massa de clientes pré-definidos.
   - Adição de um cliente individual via entrada do usuário.
3. **Consulta de clientes**:
   - Verificação de cadastro pelo nome.
   - Cálculo do IMC de um cliente.
4. **Fluxo interativo**:
   - Solicitação de nome do cliente para consulta ou cadastro.
   - Cálculo automático do IMC para clientes já cadastrados.

---

## Como Usar

### 1. Instalação de Dependências

Certifique-se de que o Python e o SQLite estão instalados no seu ambiente.

### 2. Estrutura do Banco de Dados

A tabela `clientes` possui os seguintes campos:

- **id**: Identificador único do cliente (INTEGER, PRIMARY KEY).
- **nome**: Nome do cliente (TEXT, NOT NULL).
- **idade**: Idade do cliente (INTEGER, NOT NULL).
- **altura**: Altura do cliente em metros (REAL, NOT NULL).
- **peso**: Peso do cliente em kg (REAL, NOT NULL).

### 3. Execução do Sistema

1. Execute o arquivo Python. A base de dados será criada automaticamente no arquivo `clinica.db`.
2. O programa adicionará clientes pré-definidos e iniciará a interface interativa:
   - Informe o nome do cliente para consulta:
     - Se o cliente não existir, será solicitado o cadastro.
     - Após o cadastro, o IMC será calculado automaticamente.
   - Se o cliente já existir, o IMC será exibido.

### 4. Exemplo de Uso

#### Entrada:
```
Nome: Ana
```

#### Saída:
```
O usuário Ana tem IMC = 23.44
```

---

## Estrutura do Código

### Funções Principais

- **`criar_tabela_clientes`**: Cria a tabela `clientes` no banco de dados.
- **`adicionar_clientes`**: Insere uma lista de clientes na tabela.
- **`adicionar_cliente`**: Adiciona um cliente individual.
- **`consultar_imc`**: Retorna o IMC de um cliente pelo nome.
- **`usuario_consulta_imc`**: Interface para o usuário calcular o IMC.
- **`consultar_cadastro`**: Verifica se um cliente está cadastrado.
- **`usuario_consulta_cadastro`**: Interface para consultar o cadastro de um cliente.
- **`aplicacao`**: Gerencia o fluxo principal do programa.

---

## Requisitos

- **Python 3.x**
- **SQLite3**


