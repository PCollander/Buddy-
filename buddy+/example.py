from flask import Flask
app = Flask(__name__)

students = ['harri', 'lisa', 'pyry', 'pera', 'maria']

@app.route('/hello/<int:name_id>')
def hello(name_id):
    if name_id < 4:
        student = students[name_id]
    else:
        student = 'quest'
    return f'Hello {student}'

if __name__ == '__main__':
    app.run(debug=True)