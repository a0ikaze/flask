from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/getresult', methods=['POST'])
def getresult_post():
    data = request.json['data']
    print(data)

    if data <= 5000:
        res = 0
    else:
        res = (data-5000)*0.1

    result = {'result': res}

    return jsonify(result)


@app.route('/getresult/<int:data>', methods=['GET'])
def getresult_get(data):
    print(data)

    if data <= 5000:
        res = 0
    else:
        res = (data-5000)*0.1

    result = {'result': res}

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
