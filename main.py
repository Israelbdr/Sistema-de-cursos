from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/alunos")
def showAlunos():
    db = sqlite3.connect('Database.db')
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute("SELECT alunos.*, cursos.nome_do_curso "
                   "FROM alunos INNER JOIN cursos ON alunos.codigo_do_curso = cursos.codigo_do_curso")
    rows = cursor.fetchall()
    return render_template('listAluno.html', rows=rows)

@app.route("/cursos")
def showCursos():
    db = sqlite3.connect('Database.db')
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute("SELECT * FROM cursos")
    rows = cursor.fetchall()
    return render_template('listCurso.html', rows=rows)

@app.route("/adicionarcurso", methods=['POST', 'GET'])
def addCurso():
    if request.method == 'POST':
        codigo = request.form['codigo']
        nome = request.form['nome']
        horas = request.form['horas']
        data = request.form['data']

        with sqlite3.connect("database.db") as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO cursos (codigo_do_curso,nome_do_curso,carga_horaria,data_de_cadastro)"
                           "VALUES(?, ?, ?, ?)", (codigo, nome, horas, data))

            db.commit
            msg = "Curso Inserido!"

        return render_template("resultado.html", msg=msg)
        db.close
    return render_template('newCurso.html')

@app.route("/adicionaraluno", methods=['POST', 'GET'])
def addAluno():
    if request.method == 'POST':
        cpd = request.form['cpd']
        nome_do_aluno = request.form['nome']
        telefone = request.form['telefone']
        endereco = request.form['endereco']
        cep = request.form['cep']
        email = request.form['email']
        codigo = request.form['codigo']

        with sqlite3.connect("database.db") as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO alunos (cpd,nome_do_aluno,telefone,endereco,cep,email,codigo_do_curso)"
                           "VALUES(?, ?, ?, ?, ?, ?, ?)", (cpd,nome_do_aluno,telefone,endereco,cep,email,codigo))

            db.commit
            msg = "Aluno Inserido!"

        return render_template("resultado.html", msg=msg)
        db.close
    return render_template('newAluno.html')

@app.route("/editarcurso/<int:codigo>", methods=['PUT', 'GET'])
def editCurso():
    if request.method == 'PUT':
        # request.form[]

        with sqlite3.connect("database.db") as db:
            cursor = db.cursor()
            cursor.execute("UPDATE INTO cursos (codigo_do_curso,nome_do_curso,carga_horaria,data_de_cadastro)"
                           "VALUES(?, ?, ?, ?)", (codigo, nome, horas, data))

            db.commit
            msg = "Curso Alterado!"

        return render_template("resultado.html", msg=msg)
        db.close
    return render_template('editarCurso.html')

@app.route("/removeraluno/<int:cpd>", methods=['GET', 'DELETE'])
def deleteAluno(cpd):
    if request.method == 'DELETE':
        with sqlite3.connect("database.db") as db:
            cursor = db.cursor()
            cursor.execute("DELETE FROM alunos WHERE cpd = ?", cpd)
            db.commit
            msg = "Aluno Removido!"
        return render_template("resultado.html", msg=msg)
        db.close
    return render_template("removeAluno.html")

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)