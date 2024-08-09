import mysql.connector

host = "localhost"
user = "root"
password = "mysql"

conexao = None
cursor = None

try:
    conexao = mysql.connector.connect(host = host, user = user, password = password)
    cursor = conexao.cursor()
    print("Mission passed!")

    cursor.execute('''
    CREATE SCHEMA Hospitalvet
''')

    cursor.execute('''
    CREATE TABLE Hospitalvet.Paciente (
    IdPaciente INT NOT NULL PRIMARY KEY,
    nomePaciente VARCHAR(225) NOT NULL,
    Especie VARCHAR(255) NOT NULL,
    Tutor VARCHAR (255) NOT NULL,
    Raça VARCHAR (255) NOT NULL,
    Peso DECIMAL (5,2) NOT NULL
    );
''')
    
    cursor.execute('''
    INSERT INTO Hospitalvet.Paciente (IdPaciente, nomePaciente, Especie, Tutor, Raça, Peso)
    VALUES
    (1, 'Rex', 'Cachorro', 'João', 'Vira-lata', 15.50),
    (2, 'Mia', 'Gato', 'Maria', 'Siamês', 4.20),
    (3, 'Bolt', 'Cachorro', 'Pedro', 'Pastor Alemão', 20.10),
    (4, 'Luna', 'Cachorro', 'Ana', 'Labrador', 18.00),
    (5, 'Oliver', 'Gato', 'Carla', 'Persa', 5.80),
    (6, 'Thor', 'Cachorro', 'Lucas', 'Golden Retriever', 27.30),
    (7, 'Lola', 'Cachorro', 'Mariana', 'Poodle', 7.50),
    (8, 'Simba', 'Gato', 'Fernanda', 'Maine Coon', 6.70),
    (9, 'Zeus', 'Cachorro', 'Gustavo', 'Rottweiler', 32.00),
    (10, 'Nina', 'Cachorro', 'Patrícia', 'Shih Tzu', 5.10),
    (11, 'Lucky', 'Cachorro', 'Roberto', 'Chihuahua', 3.50),
    (12, 'Coco', 'Gato', 'Camila', 'Bengal', 4.00),
    (13, 'Rocky', 'Cachorro', 'Márcio', 'Bulldog Francês', 12.60),
    (14, 'Milo', 'Cachorro', 'Isabela', 'Dálmata', 22.80),
    (15, 'Sophie', 'Gato', 'Renata', 'Ragdoll', 5.40),
    (16, 'Jack', 'Cachorro', 'Diego', 'Jack Russell Terrier', 8.90),
    (17, 'Misty', 'Gato', 'Tatiane', 'Sphynx', 3.20),
    (18, 'Max', 'Cachorro', 'Amanda', 'Bulldog Inglês', 24.50),
    (19, 'Whiskers', 'Gato', 'Eduardo', 'Angorá', 4.50),
    (20, 'Ruby', 'Cachorro', 'Larissa', 'Basset Hound', 19.70),
    (21, 'Chloe', 'Cachorro', 'Rafael', 'Dachshund', 6.20),
    (22, 'Leo', 'Gato', 'Vanessa', 'British Shorthair', 5.00),
    (23, 'Harley', 'Cachorro', 'Juliana', 'Boxer', 29.40),
    (24, 'Ziggy', 'Cachorro', 'Alexandre', 'Husky Siberiano', 26.00),
    (25, 'Oreo', 'Gato', 'Priscila', 'Munchkin', 3.90),
    (26, 'Teddy', 'Cachorro', 'Caroline', 'Shiba Inu', 10.30),
    (27, 'Cleo', 'Gato', 'Marcelo', 'Scottish Fold', 4.30),
    (28, 'Duke', 'Cachorro', 'Fábio', 'Doberman', 31.10),
    (29, 'Penny', 'Cachorro', 'Luiza', 'Yorkshire Terrier', 3.80),
    (30, 'Mochi', 'Gato', 'Daniel', 'Siberian', 5.60)
'''
)
    conexao.commit()

except mysql.connector.Error as e:
    print("Erro SQL:", e)

except Exception as e:
    print("Erro Python:", e)

finally:
    if cursor != None:
        cursor.close()
    if conexao != None and conexao.is_connected():
        conexao.close()