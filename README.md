# Hospital Veterinário

## Descrição do Projeto

HospitalVet é um sistema simples de gerenciamento de pacientes para um hospital veterinário, desenvolvido em Python utilizando MySQL para armazenamento de dados. O programa permite visualizar, cadastrar, alterar e remover pacientes, oferecendo uma solução prática para o controle de informações de animais em atendimento.

## Funcionalidades

- **Ver Pacientes**: Exibe uma lista de todos os pacientes cadastrados no sistema.
- **Cadastrar Paciente**: Adiciona um novo paciente ao banco de dados.
- **Alterar Cadastro de Paciente**: Modifica as informações de um paciente existente.
- **Remover Paciente**: Exclui um paciente do banco de dados.
- **Sair**: Encerra o programa.

## Estrutura do Projeto

- **`setup.py`**: Script para configuração inicial do banco de dados MySQL, criando a estrutura necessária e inserindo dados de exemplo.
- **`main.py`**: Programa principal contendo a lógica para interação com o usuário e gerenciamento dos dados dos pacientes.

## Requisitos

- Python 3.6 ou superior
- MySQL Connector

## Como Executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/PabloCarnauba/hospitalvet.git
   ```
2. **Instale as dependências:**
   ```bash
   pip install mysql-connector-python
   ```
3. **Configure o banco de dados:**
   Execute o arquivo `setup.py` para criar a base de dados e tabelas necessárias:
   ```bash
   python setup.py
   ```
4. **Execute a aplicação:**
   ```bash
   python main.py
   ```

## Estrutura da Interface

A interface do HospitalVet é baseada em texto e opera por meio de um menu interativo, permitindo fácil navegação e gerenciamento das informações dos pacientes.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests. Para grandes mudanças, por favor, abra uma issue primeiro para discutir o que você gostaria de mudar.