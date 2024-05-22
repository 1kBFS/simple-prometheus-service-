from flask import Flask, Response
from prometheus_client import make_wsgi_app, generate_latest, Enum
from werkzeug.middleware.dispatcher import DispatcherMiddleware

import host_type

app = Flask(__name__)

STATE = Enum('host_type', 'Type of the host',
             states=['virtual machine', 'container', 'physical server', 'undefined'])
STATE.state(host_type.determine_host_type())


@app.route('/')
def hello_world():
    return Response(generate_latest(STATE), mimetype="text/plain")


if __name__ == '__main__':
    app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
        '/': make_wsgi_app()
    })
    # host_type.determine_host_type(STATE)
    app.run(host="0.0.0.0", port=8080)
