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

@app.route('/route_avail')
def route_avail():
    route_id = request.args.get('route')
    timeslot = request.args.get('timeslot')
    date_requested = request.args.get('date')
    route_avail = minion.update_route_info(timeslot, route_id, date_requested)
    return json.dumps(route_avail)

@app.route('/health')
def healthcheck():
    with app.app_context():
        print("All is well in port 8080")
        return jsonify(
            status="running"
        )


if __name__ == '__main__':
    app.run(port=8080)