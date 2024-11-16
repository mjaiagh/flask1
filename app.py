from flask import Flask, request

app = Flask(__name__)


@app.route('/calculate')
def hello_world():  # put app
    op = request.args.get('op', type=str)
    arg1 = request.args.get('arg1', type=int)
    arg2 = request.args.get('arg1', type=int)
    if op == 'add':
        result = arg1 + arg2
    elif op == 'subtract':
        result = arg1 - arg2
    elif op == 'multiply':
        result = arg1 * arg2
    elif op == 'divide':
        if arg2 != 0:
            result = arg1 / arg2
        else:
            return "Division by zero", 400
    else:
        return "Invalid operation", 400
    return str(result)


if __name__ == '__main__':
    app.run()
