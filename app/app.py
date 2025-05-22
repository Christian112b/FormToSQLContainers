from flask import Flask, render_template, request, url_for, redirect
from controllers.database import *

app = Flask(__name__)

@app.route('/')
def home():

    db = Database()
    estudiantes = db.get_estudiantes()

    return render_template('form.html', estudiantes=estudiantes)

@app.route('/submit', methods=['POST'])
def submit():
    print("Form submitted")
    print(request.form)

    db = Database()
    db.insert_estudiante(
        nombre=request.form['nombre'],
        edad=request.form['edad'],
        sexo=request.form['sexo'],
        carrera=request.form['carrera'],
        semestre=request.form['semestre'],
        matricula=request.form['matricula'],
        fecha=request.form['fecha'],
        fecha_nacimiento=request.form['fecha_nacimiento'],
        lugar_nacimiento=request.form['lugar_nacimiento']
    )

    return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')  


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)