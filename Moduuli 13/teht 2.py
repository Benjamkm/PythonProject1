from flask import Flask, jsonify

app = Flask(__name__)

airport_data = {
    "EFHK": {
        "Name": "Helsinki Vantaa Airport",
        "Municipality": "Helsinki"
    }
}

@app.route('/kenttä/<icao>', methods=['GET'])
def airport(icao):
    icao = icao.upper()

    if icao in airport_data:
        return jsonify({
            "ICAO": icao,
            "Name": airport_data[icao]["Name"],
            "Municipality": airport_data[icao]["Municipality"]
        })

    return jsonify({
        "error": "Airport not found"
    })


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)