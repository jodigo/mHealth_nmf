from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
  return "STAT"

@app.route('/number/<int:some_int>', methods=['PUT'])
def plus100(some_int):
  return "%d" % (some_int + 100)

if __name__ == "__main__":
  app.run(debug=True)