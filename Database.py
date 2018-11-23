# Importa o modulo de conexão SQLite3 + Python
import sqlite3

# Gera a string de conexão
db = sqlite3.connect("Database.db")

# Posiciona o cursor.
cursor = db.cursor()


# Cria a tabela cursos.
def createTablecursos():
    cursor.execute("CREATE TABLE IF NOT EXISTS cursos(\n"
        "codigo_do_curso INTEGER PRIMARY KEY,\n"
        "nome_do_curso TEXT NOT NULL,\n"
        "carga_horaria TEXT NOT NULL,\n"
        "data_de_cadastro TEXT NOT NULL);\n")

# Cria a tabela alunos.
def createTablealunos():
    cursor.execute("CREATE TABLE IF NOT EXISTS alunos(\n"
        "cpd INTEGER PRIMARY KEY NOT NULL,\n"
        "nome_do_aluno TEXT DEFAULT NULL,\n"
        "telefone INTEGER DEFAULT NULL,\n"
        "endereco TEXT DEFAULT NULL,\n"
        "cep INTEGER DEFAULT NULL,\n"
        "email TEXT DEFAULT NULL,\n"
        "codigo_do_curso INTEGER DEFAULT NULL,\n"
        "FOREIGN KEY (codigo_do_curso)REFERENCES cursos(codigo_do_curso));")

# Insere os cursos na tabela de cursos.
def insertTablecursos():
    cursor.execute("INSERT OR IGNORE INTO cursos VALUES(\n"
                   "100,'Medicina','2000 Horas','12/01/2018'),\n"
                   "(200,'Direito','1000 Horas','25/01/2018'),"
                   "(300,'Administração','700 Horas','13/02/2018');")

# Insere os alunos na tabela de alunos.
def insertTablealunos():
    cursor.execute("INSERT OR IGNORE INTO alunos VALUES ("
                   "12345,'Jose Maria',981231232,'R. Alternada',65032123,'zemaria@hotmail.com',100),"
                   "(21231,'João Tadeu',981113312,'Av. Alternada',65000000,'jaotadeu@hotmail.com',200),"
                   "(23421,'João Maria',999112391,'Al. Alternada',65111111,'jaomaria@hotmail.com',200),"
                   "(32154,'Jose Tadeu',981235432,'R. Projetada',65012321,'zetadeu@hotmail.com',100),"
                   "(53421,'José José',988119933,'Av. Projetada',65060600,'zeze@hotmail.com',100),"
                   "(65000,'Maria do Socorro',988121232,'Al. Principal',65033333,'mariahelp@hotmail.com',300),"
                   "(65233,'Maria do Carmo',988331233,'Al. Projetada',65222222,'mariadanovela@hotmail.com',300);")

# Cria uma tabela de usuários.
def createTableusers():
    cursor.execute("CREATE TABLE IF NOT EXISTS USERS(USERNAME TEXT NOT NULL,EMAIL TEXT,PASSWORD TEXT)")

# Insere um usuário na tabela.
def insertTableusers():
    cursor.execute("INSERT OR IGNORE INTO USERS VALUES(?,?,?)",('admin','admin@gmail.com','admin'))

# Execução das funções pré-estabelecidas.
createTablealunos()
createTablecursos()
createTableusers()
insertTablealunos()
insertTablecursos()
insertTableusers()

# Salva os dados no banco
db.commit()

# Fecha a conexão com o banco.
cursor.close()

