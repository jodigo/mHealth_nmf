from flask import Flask, request, render_template
import q1

app = Flask(__name__)

@app.route('/')
def index():
  return "STAT"

@app.route('/number/<int:some_int>', methods=['PUT'])
def plus100(some_int):
  return "%d" % (some_int + 100)

@app.route('/NMF')
def nmf():
  messages = q1.run_nmf()
  return render_template('q3.html', messages = messages)

if __name__ == "__main__":
  app.run(debug=True)