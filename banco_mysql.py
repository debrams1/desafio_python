import mysql
# criar função para inserir contatos banco mysql
import mysql.connector

def inserir_contato(nome, email, cidade):
    try:
        # Conectar ao banco de dados
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="desafio"
        )

        # Criar um cursor
        cursor = conexao.cursor()

        # Construir a consulta SQL
        consulta = "INSERT INTO contato (nome, email, cidade) VALUES (%s, %s, %s)"
        valores = (nome, email, cidade)

        # Executar a consulta
        cursor.execute(consulta, valores)

        # Commitar a transação
        conexao.commit()

        print("Contato inserido com sucesso!")

    except mysql.connector.Error as erro:
        print(f"Erro ao inserir contato: {erro}")

    finally:
        # Fechar a conexão
        if conexao.is_connected():
            cursor.close()
            conexao.close()

# criar função para visualizar contatos banco mysql
def obter_contato():
    try:
        # Conectar ao banco de dados
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="desafio"
        )

        # Criar um cursor
        cursor = conexao.cursor()

        # Construir a consulta SQL
        consulta = "SELECT * FROM contato"

        # Executar a consulta
        cursor.execute(consulta)

        # Obter os resultados
        resultados = cursor.fetchall()

        # Imprimir os resultados
        for contato in resultados:
            print(f"Nome: {contato[1]}, E-mail: {contato[2]}, Cidade: {contato[3]}")

    except mysql.connector.Error as erro:
        print(f"Erro ao visualizar contatos: {erro}")

    finally:
        # Fechar a conexão
        if conexao.is_connected():
            cursor.close()
            conexao.close()



