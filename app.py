from flask import Flask, request
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    return "Olá, Flask"

@app.route('/item', methods=['POST'])
def post_item():
    data = request.get_json()
    sql = f"INSERT INTO todolist(item, status) VALUES('{data['item']}','{data['status']}')"
    banco(sql)
    return data

def banco(sql):
    resultado = ""
    try:
        # Conexão com o banco de dados PostgreSQL
        conn = psycopg2.connect(
            host = "dpg-cuhulhlds78s73e3eabg-a.oregon-postgres.render.com",
            port = "5432",
            dbname = "senaidb_giju",
            user = "senaidb_giju_user",
            password = "oynUaoIszXotTDt9caTgB5x17bp0etxB"
        )
        cursor = conn.cursor() # cursor vai ser a variável para executar os comandos SQL.
        cursor.execute(sql) # executa o comando sql seja insert, select .. etc
        cursor.close() # finaliza o cursor
        conn.commit() # confirma o comando SQL 
        conn.close() # finaliza a conexão
    except psycopg2.Error as e:
        print("Erro na conexão do baaaaaaanco de dados")


if __name__ == '__main__':
    app.run(debug=True)

    
