from flask import Flask, redirect, request, render_template, jsonify

from random import randint
from mongoengine import connect

import database

app = Flask(__name__)

with app.app_context():
    db = connect('daneshsayings')

    def select_random():
        start = randint(1, database.Saying.objects().count()) - 1
        return database.Saying.objects().skip(start).limit(1).first().s.strip()

    @app.route('/daneshsayings/')
    def main():
        return render_template("index.html.j2", saying=select_random())

    @app.route('/daneshsayings/saying/')
    def saying():
        database.Saying.objects().count()
        return select_random()
    @app.route('/daneshsayings/slack/')
    def slack():
        return jsonify({
            'response_type': 'in_channel',
            'text': select_random()
            })
if __name__ == "__main__":
    app.run(host="0.0.0.0")
