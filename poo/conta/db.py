import sqlite3
import menu

conn = sqlite3.connect("database-conta.db")
cursor = conn.cursor()
def criar_tabela_conta():
    """criar tabela 'conta' caso não exista""" 
    
    cursor.execute("""
    create table if not exists conta (
        numero_conta integer primary key autoincrement,
        titular text NOT NULL,
        saldo float NOT NULL,
        limite float NOT NULL
    )
    """)
    print("Tabela criada com sucesso.")
    conn.commit()

def get_tables():
    cursor.execute("""
    select name from sqlite_master where type = "table"
    """)
    print(cursor.fetchall())

def get_conta(numero):
    cursor.execute("""
    select * from conta where numero_conta = ?
    """, (numero,))
    return cursor.fetchall()
    
def get_all_conta():
    cursor.execute("""
    select * from conta
    """)
    return cursor.fetchall()


def set_conta(titular, saldo, limite):
    cursor.execute("""
    insert into conta(titular, saldo, limite)
    values (?,?,?)    
    """, (titular, saldo, limite))
    conn.commit()