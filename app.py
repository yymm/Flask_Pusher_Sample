# -*- encoding: utf-8 -*-

from flask import Flask, render_template, redirect, url_for, request
import pusher

app = Flask(__name__)

#app.config.from_pyfile("app.cfg")

#p = pusher.Pusher(
    #app_id = app.config["ID"],
    #key = app.config["KEY"],
    #secret = app.config["SECRET"]
#)
p = pusher.pusher_from_url()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pusher', methods=["POST"])
def pusher():
    if request.method == 'POST':
        p['channel1'].trigger('event1', {'message': "((((((((((っ･ωΣ[柱]ｶﾞｺｯ!"})
    return 'ok'

if __name__ == '__main__':
    app.debug = True
    app.run(host='192.168.5.7', port=8080)
