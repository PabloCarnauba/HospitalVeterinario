import mysql.connector

import os

host = "localhost"
user = "root"
password = "mysql"
database  = "hospitalvet"

def getConexao():
    return mysql.connector.connect(host = host, user = user, password = password, database = database)

while True:
    print('''
          1) - Ver pacientes.
          2) - Cadastrar paciente.
          3) - Alterar cadastro paciente.
          4) - Remover paciente.
          5) - Sair.
          ''')
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == '1':
        conexao = getConexao()
        cursor = conexao.cursor()
        cursor.execute('''
            SELECT * FROM Paciente
            ''')
        resultado = cursor.fetchall()
        
        for paciente in resultado:
            print(f"ID: {paciente[0]} | Nome: {paciente[1]} | Especie: {paciente[2]} | Tutor: {paciente[3]} | Raça: {paciente[4]} | Peso: {paciente[5]}")
            
        cursor.close()
        conexao.close()
        print("")
        os.system('pause')
        
    elif escolha == '2':
        IdPaciente = int(input("ID do paciente a ser cadastrado: "))
        nomePaciente = input("Nome do paciente: ")
        Especie = input("Especie do paciente: ")
        Tutor = input("Tutor do paciente: ")
        Raça = input("Raca do paciente: ")
        Peso = float(input("Peso do paciente: "))
        
        conexao = getConexao()
        cursor = conexao.cursor()
        
        cursor.execute(''' 
            INSERT INTO Paciente (IdPaciente, nomePaciente, Especie, Tutor, Raça, Peso)
            VALUES (%s, %s, %s, %s, %s, %s)
            ''', (IdPaciente,nomePaciente, Especie, Tutor, Raça, Peso))
        
        conexao.commit()
        cursor.close()
        conexao.close()
        print("")
        print('-' * 30)
        print("Paciente cadastrado com sucesso!")
        print('-' * 30)
        print("")
        os.system('pause')
        
    elif escolha == '3':
        IdPaciente = int(input("ID do paciente a ser alterado: "))
        novoNome = input("Novo nome do paciente: ")
        novaEspecie = input("Nova especie do paciente: ")
        novoTutor = input("Novo tutor do paciente: ")
        novaRaca = input("Nova raca do paciente: ")
        novoPeso = float(input("Novo peso do paciente: "))
        
        conexao = getConexao()
        cursor = conexao.cursor()
        
        cursor.execute('''
            UPDATE Paciente
            SET nomePaciente = %s, Especie = %s, Tutor = %s, Raça = %s, Peso = %s
            WHERE IdPaciente = %s
            ''', (novoNome, novaEspecie, novoTutor, novaRaca, novoPeso, IdPaciente))
        
        conexao.commit()
        cursor.close()
        conexao.close()
        print("")
        print('-' * 30)
        print("Paciente alterado com sucesso!")
        print('-' * 30)
        print("")
        os.system('pause')
        
    elif escolha == '4':
        IdPaciente = int(input("ID do paciente a ser excluído: "))
        
        conexao = getConexao()
        cursor = conexao.cursor()
        
        cursor.execute('''
            DELETE FROM Paciente
            WHERE IdPaciente = %s
            ''', (IdPaciente,))
        
        conexao.commit()
        cursor.close()
        conexao.close()
        print("")
        print('-' * 30)
        print("Paciente excluído com sucesso!")
        print('-' * 30)
        print("")
        os.system('pause')
        
    elif escolha == '5':
        print("Saindo...")
        break
    
    else:
        print("Opção inválida, tente novamente!")
        os.system('pause')