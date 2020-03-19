from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
import utils
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("main.html")

@app.route("/c1")
def get_c1_data():
    data = utils.get_cl_data()
    return jsonify({"confirm":data['confirm'],"suspect":data['suspect'],"heal":data['heal'],"dead":data['dead']})


@app.route("/time")
def get_time():
    return utils.get_time()

if __name__ == '__main__':
    app.run()
