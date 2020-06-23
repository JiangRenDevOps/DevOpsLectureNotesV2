from flask import Flask, Response

from WK4_Python_WebApp.hands_on.src.utils.logger import Logger


app = Flask(__name__)

logger = Logger(severity="DEBUG", name="app_run").get_logger()

Customers = {}


@app.route('/health_check', methods=['GET'])
def health_check():
    logger.info("Health check invoked successfully")
    return Response(response="Health check invoked successfully", status=200)


# Add more APIs here


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True)
