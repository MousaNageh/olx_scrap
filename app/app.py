from flask import Flask, jsonify
from db.db_connection import DatabaseConnection
from driver.chrome_diver import ChromeDriver
from olx_email.olx_ads_email import EmailSender
from scraping.olx_scraping import OlxScraping
app = Flask(__name__)
app.config.from_pyfile('config.py')
db = DatabaseConnection()
driver = ChromeDriver().get_driver()

@app.route('/')
def get_olx_data():
    olx_scraping = OlxScraping(driver=driver)
    data = olx_scraping.get_data(keyword='s')

    email = EmailSender(recipient="200moussa200@gmail.com",app=app)
    email.send_email(data=data[:20])
    return "olx up"

# @app.route('/animals')
# def get_stored_animals():
#     db = get_db()
#     _animals = db.animal_tb.find()
#     animals = [{"id": animal["id"], "name": animal["name"], "type": animal["type"]} for animal in _animals]
#     return jsonify({"animals": animals})

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)