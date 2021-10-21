from json import dumps
from logging.config import dictConfig
from os import environ
from flask import Flask, Response, request

# https://stackoverflow.com/a/56998012/3333549
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://sys.stdout',
        'formatter': 'default'
    }},
    'root': {
        'level': 'DEBUG',
        'handlers': ['wsgi']
    }
})

HTTP_METHODS = ['GET', 'POST', 'PUT', 'PATCH',
                'DELETE', 'COPY', 'HEAD', 'OPTIONS',
                'LINK', 'UNLINK', 'PURGE', 'LOCK',
                'UNLOCK', 'PROPFIND', 'VIEW', 'CONNECT', 'TRACE']

app = Flask(__name__)


@app.route('/', defaults={'path': ''}, methods=HTTP_METHODS)
@app.route('/<path:path>', methods=HTTP_METHODS)
def catch(path):
    data = {
        'headers': dict(request.headers),
        'data': request.data.decode('utf-8'),
        'args': request.args,
        'form': request.form,
        'endpoint': request.endpoint,
        'method': request.method,
        'remote_addr': request.remote_addr,
        'path': path,
    }

    # pylint: disable=no-member
    app.logger.debug(dumps(data, indent=2, sort_keys=True))
    # pylint: enable=no-member

    status = environ.get('RESPONSE_STATUS')

    return Response(
        dumps(data),
        status=int(status) if status is not None else 200,
        mimetype=environ.get('RESPONSE_MIME') or 'application/json'
    )
