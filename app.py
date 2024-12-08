from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS=[
{  'id': 1,
  'title': 'Data Analyst',
  'location': 'Bengaluru, India',
  'Salary': "Rs. 10,00,000"
},
{
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Mumbai, India',
  'Salary': "Rs. 10,20,000"
},
{
  'id': 3,
  'title': 'AI Engineeer',
  'location': 'Remote',
  # 'Salary': "Rs. 10,80,000"
},]
@app.route("/")
def hello_world():
  return render_template('Home.html',jobs=JOBS)

@app.route("/api/jobs")
def listjobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host = "0.0.0.0",debug = True)