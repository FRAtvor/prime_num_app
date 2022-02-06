from flask import Flask, request

app = Flask(__name__)


@app.route('/prime_test', methods=['GET'])
def search():
    args = request.args.get('x')
    return args


if __name__ == '__main__':
   app.run()

   print(args)
    # print(type(args.to_dict()))
    # <class 'dict'>