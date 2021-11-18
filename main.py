from flask import Flask, render_template, request
from models import LVQ

# Create a flask app
app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

# Index page
@app.route('/')
def hello():
  return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
  if request.method=='POST':
    text = request.form['text']
    lvq = LVQ(text)
    return render_template('result.html',lvq=lvq)
  return render_template('index.html')
  


if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )
