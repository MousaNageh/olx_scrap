from flask import Flask, jsonify
from db.db_connection import DatabaseConnection
from driver.chrome_diver import ChromeDriver
from scraping_executor.olx_scraping_executor import olx_scraping_executor
from validations.validate_olx_request import validate_olx_request
from flask import request
import multiprocessing

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = DatabaseConnection().get_db()
driver = ChromeDriver().get_driver()

@app.route('/',methods=['POST'])
def get_olx_data():
    errors,valid_data = validate_olx_request(request)
    if errors :
        return jsonify({'errors': errors}), 400
    args = (
        valid_data,
        db,
        driver,
        app
    )
    process = multiprocessing.Process(target=olx_scraping_executor,args=args)
    process.start()

    return jsonify({'success':"email will send after awhile"}), 200


if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)