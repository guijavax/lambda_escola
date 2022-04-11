import psycopg2


def connect():
    return psycopg2.connect(host="localhost", database="escola", user="postgres", password="root")


def lambda_handler(event, context):
    try:
        print('Connecting')
        # id_aluno = event['id_aluno']
        # nome = event['nome']
        id_aluno = 22
        nome = 'Vicente Araújo'
        con = connect()
        cur = con.cursor()
        cur.execute('insert into aluno values(%s,%s)', (id_aluno, nome))
        con.commit()
        con.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)


lambda_handler(None, None)
