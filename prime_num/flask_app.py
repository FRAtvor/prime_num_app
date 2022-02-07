from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/prime_num', methods=['GET'])
def get_url():
    args = request.args.get('x')
    return args


if __name__ == '__main__':
   app.run(debug= True)

   print(args)
    # print(type(args.to_dict()))
    # <class 'dict'>