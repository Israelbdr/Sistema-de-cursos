
from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

'''db = sqlite3.connect('Database.db')
cursor = db.cursor()
cursor.execute("SELECT * FROM alunos")
return render_template('index.html', data=data)
'''

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)