from mongoengine import Document

class CustomUser(Document):
    meta = {'collection': 'users'}
