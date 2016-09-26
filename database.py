from mongoengine import *
class Saying(Document):
    i = SequenceField()
    s = StringField() #saying
