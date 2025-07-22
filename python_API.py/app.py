from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/saludo', methods=['GET'])
def saludo():
    """
    Saludo API
    ---
    parameters:
      - name: cadenadeentrada
        in: query
        type: string
        required: false
        description: Nombre para el saludo
    responses:
      200:
        description: Mensaje de saludo
        schema:
          type: object
          properties:
            mensaje:
              type: string
    """
    nombre = request.args.get('cadenadeentrada', '')
    mensaje = f'Hola {nombre} desde la API de Python'
    return jsonify({'mensaje': mensaje})

if __name__ == '__main__':
    app.run(debug=True)