import os

MAIL_SERVER = os.environ.get("MAIL_SERVER")
MAIL_PORT = int(os.environ.get("MAIL_PORT"))
MAIL_USE_SSL = bool(os.environ.get("MAIL_USE_SSL"))
MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER")
MAIL_MAX_EMAILS = None
MAIL_ASCII_ATTACHMENTS = False
