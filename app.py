from flask import Flask , render_template
app = Flask(__name__)
import random 


@app.route("/intro")
def quote():
	return render_template ("spair.html")


if __name__=="__main__":
	app.run(port=3000, debug=True)
	