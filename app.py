from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/status')
def get_status():
    return jsonify({"service": "status-checker", "status": "running"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
