from flask import Flask, request, url_for
from prime_num import prime_num_test, find_nearest_pn
import math

app = Flask(__name__)


@app.route('/prime_test', methods=['GET'])
def get_test_num():
    args = request.args.get('x', default=0, type=int)
    if prime_num_test(args):
        return "bingo"
    else:
        return f"{args} is not a prime number. The nearest prime number is: {find_nearest_pn(args)}"
   


if __name__ == '__main__':
   app.run(debug=True)

  

    # print(type(args.to_dict()))
    # <class 'dict'>
