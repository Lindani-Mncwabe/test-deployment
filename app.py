from flask import Flask, request
from flasgger import Swagger
import json

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/')
def hello_world():
    """
    Example endpoint returning a simple greeting
    ---
    responses:
      200:
        description: A simple greeting message
        examples:
          text: Hello, World!
    """
    return 'Hello, World!'

@app.route('/multiply', methods=['GET'])
def multiply():
    """
    Multiply two numbers
    ---
    parameters:
      - name: num1
        in: query
        type: integer
        required: true
        description: The first number
      - name: num2
        in: query
        type: integer
        required: true
        description: The second number
    responses:
      200:
        description: The product of the two numbers
        schema:
          type: object
          properties:
            product:
              type: integer
              description: The product of num1 and num2
              example: 6
    """
    try:
        num1 = int(request.args.get('num1'))
        num2 = int(request.args.get('num2'))
        product = num1 * num2
        response = app.response_class(
            response=json.dumps({"product": product}),
            status=200,
            mimetype='application/json'
        )
        return response
    except (TypeError, ValueError) as e:
        response = app.response_class(
            response=json.dumps({"error": str(e)}),
            status=400,
            mimetype='application/json'
        )
        return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5008)