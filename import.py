import codecs
import database
from mongoengine import connect

db = connect("daneshsayings")

with codecs.open('import.txt', 'r', 'utf-8') as f:
    for line in f:
        database.Saying(s=line).save()
