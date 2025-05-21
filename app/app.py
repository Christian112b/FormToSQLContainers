from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    print("Form submitted")
    print(request.form)

    return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')  


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)