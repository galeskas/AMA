import sqlite3
from datetime import datetime

def create_tables():
    # Conecta-se ao banco de dados (criará o arquivo se ele não existir)
    conn = sqlite3.connect('amadata.db')
    cursor = conn.cursor()

    # Verifica se a tabela Tipo já existe
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Tipo'")
    cursor.execute("DROP TABLE IF EXISTS Tipo")
    if not cursor.fetchone():
        cursor.execute('''
        CREATE TABLE Tipo (
            tipoID INTEGER PRIMARY KEY AUTOINCREMENT,
            Tipo TEXT
        );
        ''')
        print("Tabela 'Tipo' criada com sucesso.")

    # Verifica se a tabela Status já existe
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Status'")
    cursor.execute("DROP TABLE IF EXISTS Status")
    if not cursor.fetchone():
        cursor.execute('''
        CREATE TABLE Status (
            statusID INTEGER PRIMARY KEY AUTOINCREMENT,
            Status TEXT
        );
        ''')
        print("Tabela 'Status' criada com sucesso.")

      # Verifica se a tabela Mamadas já existe
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Mamadas'")
    cursor.execute("DROP TABLE IF EXISTS Mamadas")
    if not cursor.fetchone():
        cursor.execute('''
            CREATE TABLE Mamadas (
                MamadaID INTEGER PRIMARY KEY AUTOINCREMENT,
                Data_Hora TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                tipoID INTEGER,
                statusID INTEGER,
                Quantidade INTEGER,
                FOREIGN KEY (tipoID) REFERENCES Tipo(tipoID),
                FOREIGN KEY (statusID) REFERENCES Status(statusID)
            );
            ''')
        print("Tabela 'Mamadas' criada com sucesso.")
            # Salva as alterações
    conn.commit()
    # Fecha a conexão
    conn.close()

def insert_values():
    # Conecta-se ao banco de dados
    conn = sqlite3.connect('amadata.db')
    cursor = conn.cursor()

    # Simulação de dados
    status = [
        ('Vazia',),
        ('Metade',),
        ('Cheia',),
    ]

        # Simulação de dados
    tipo = [
        ('Mamadeira',),
        ('Natural',),
        ('Colher',),
    ]

    simulado = [
        ('2026-08-01 03:15:00', 2, 1, 'NULL'),
        ('2026-08-01 07:30:00', 2, 1, 'NULL'),
        ('2026-08-01 11:45:00', 1, 3, 150),
        ('2026-08-02 04:00:00', 2, 1, 'NULL'),
        ('2026-08-02 08:20:00', 2, 1, 'NULL'),
        ('2026-08-03 14:10:00', 2, 1, 'NULL'),
        ('2026-08-03 18:00:00', 1, 2, 90),
        ('2026-08-04 02:30:00', 2, 1, 'NULL'),
        ('2026-08-05 10:00:00', 2, 1, 'NULL'),
        ('2026-08-05 15:30:00', 3, 1, 30),
        ('2026-08-06 06:15:00', 2, 1, 'NULL'),
        ('2026-08-07 12:00:00', 2, 1, 'NULL'),
        ('2026-08-08 09:45:00', 1, 3, 160),
        ('2026-08-09 01:20:00', 2, 1, 'NULL'),
        ('2026-08-10 16:50:00', 2, 1, 'NULL'),
        ('2026-08-12 05:10:00', 2, 1, 'NULL'),
        ('2026-08-14 11:30:00', 2, 1, 'NULL'),
        ('2026-08-15 20:15:00', 1, 2, 100),
        ('2026-08-18 08:00:00', 2, 1, 'NULL'),
        ('2026-08-20 13:40:00', 2, 1, 'NULL'),
        ('2026-08-22 04:45:00', 2, 1, 'NULL'),
        ('2026-08-25 10:20:00', 2, 1, 'NULL'),
        ('2026-08-28 17:00:00', 1, 3, 180),
        ('2026-08-30 07:10:00', 2, 1, 'NULL'),
        ('2026-08-31 22:30:00', 2, 1, 'NULL'),
    ]
    # Insere os dados na tabela Mamadas
    for row in status:
        cursor.execute('''
        INSERT INTO status (Status)
        VALUES (?)
        ''', row)

        # Insere os dados na tabela Mamadas
    for row in tipo:
        cursor.execute('''
        INSERT INTO tipo (Tipo)
        VALUES (?)
        ''', row)

    for row in simulado:
        cursor.execute('''
        INSERT INTO Mamadas (Data_Hora, tipoID, statusID, Quantidade)
        VALUES (?,?,?,?)
        ''', row)


    # Salva as alterações
    conn.commit()

    # Fecha a conexão
    conn.close()
