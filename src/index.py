import psycopg2


def connect():
    return psycopg2.connect(host="localhost", database="escola", user="postgres", password="root")


def execute():
    try:
        print('Connecting')
        con = connect()
        cur = con.cursor()
        cur.execute('select * from aluno')
        result = cur.fetchall()
        dados = []
        for dado in result:
            dados.append(dado)

        con.close()
        print(dados)
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)


execute()
