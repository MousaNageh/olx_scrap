from db.olx_db import OlxCollections
from olx_email.olx_ads_email import EmailSender
from scraping.olx_scraping import OlxScraping


def send_email(data,email,app):
    email_sender = EmailSender(recipient=email,app=app)
    email_sender.send_email(data)


def olx_scraping_executor(valid_data,db,driver,app):
    olx_collection = OlxCollections(db=db)
    document = olx_collection.get_if_exists(keyword=valid_data.get('keyword'))
    if not  document:
        olx_scraping = OlxScraping(driver=driver)
        data = olx_scraping.get_data(keyword=valid_data.get('keyword'))
        document = olx_collection.create_doc(keyword=valid_data.get('keyword'),data=data)

    document = dict(document)
    size = max(20,valid_data.get('size',0))
    send_email(data=document["data"][:size], email=valid_data.get('email'), app=app)