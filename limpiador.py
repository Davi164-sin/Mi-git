
from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
<title>Eliminar archivo</title>
</head>
<body>
<h1>Eliminar archivo</h1>
<form action="/eliminar_archivo" method="post">
<input type="text" name="archivo" placeholder="Ingrese el nombre del archivo">
<input type="submit" value="Eliminar archivo">
</form>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html)

@app.route('/eliminar_archivo', methods=['POST'])
def eliminar_archivo():
    archivo_eliminar = request.form['archivo']
    if os.path.exists(archivo_eliminar):
        os.remove(archivo_eliminar)
        return "Archivo eliminado"
    else:
        return "El archivo no existe"

if __name__ == '__main__':
    app.run(port=5003)

