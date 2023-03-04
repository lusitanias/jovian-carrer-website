from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [{
  'id': 1,
  'titel': 'Datenanalyst',
  'ort': 'Bangalore, Indien',
  'gehalt': '20000 EUR'
}, {
  'id': 2,
  'titel': 'Programmierer',
  'ort': 'Hamburg, Deutschland',
  'gehalt': '50000 EUR'
}, {
  'id': 3,
  'titel': 'Python-Entwickler',
  'ort': 'Rom, Italien',
  'gehalt': '35000 EUR'
}]


@app.route('/')
def index():
  return render_template('test.html', jobs=JOBS, company_name='Jovian')

@app.route('/jobs')
def list_jobs():
  return jsonify(JOBS)

app.run(host='0.0.0.0', port=82)
