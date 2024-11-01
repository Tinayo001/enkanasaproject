from flask import Flask, render_template, jsonify

app = Flask(__name__, static_folder= 'static')

JOBS = [
                {
            'id': 1,
            'title': 'Data Analyst',
            'location': "Nairobi, Kenya",
            'Salary': 'Ksh, 400000'
            },
        {
            'id': 2,
            'title': 'Data scientist',
            'location': "MOmbasa, Kenya",
            'Salary': 'Ksh, 600000'
            },
        {
            'id': 3,
            'title': 'Front-end engineer',
            'location': "Remote",
            'Salary': 'Ksh, 500000'
            },
        {
            'id': 4,
            'title': 'Backend Engineer',
            'location': "San Fransisco, USA",
            'Salary': '$5000'
            },
        
        ]
@app.route("/")
def hello_world():
    return render_template("home.html",
                           jobs=JOBS,
                           company_name='Tinayo Devops')
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__=="__main":
    app.run(host='0.0.0.0', debug=True)
