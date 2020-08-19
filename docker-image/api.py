import flask
import scraper
import logging
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/trails', methods=['GET'])
def home():
    return json.dumps(scraper.main(), indent=2)

if __name__ == '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    app.run(host="0.0.0.0", port=5000, debug=True)
