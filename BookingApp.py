from flask import Flask
from flask import jsonify
from flask import request
import Minion as minion
import json

app = Flask(__name__)

@app.route('/route_list')
def route_list():
    source = request.args.get('source')
    destination = request.args.get('destination')
    route_list = minion.get_route_list(source, destination)
    return json.dumps(route_list)

@app.route('/health')
def healthcheck():
    with app.app_context():
        print("All is well in port 8080")
        return jsonify(
            status="running"
        )


if __name__ == '__main__':
    app.run(port=8080)