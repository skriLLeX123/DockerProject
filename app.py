import json
from flask import Flask, jsonify, render_template, request


app = Flask(__name__)


with open('Students.json') as json_data:
    d = json.load(json_data)
    student_list = []
    for data in d['Student']:
    	student_list.append(data)
  	    	
@app.route('/', methods =['GET'])
def test():
    return render_template("index.html")

@app.route('/Student', methods =['GET'])
def test1():
    return render_template("index.html",list_data=student_list)

@app.route('/Student/<string:idd>', methods =['GET'])
def test2(idd):
    g1=[]
    for student in student_list:
        if student['id'] == idd:
            g1.append(student)
        else:
            if idd in student['course']:
                g1.append(student)
    
    #g1 = [student for student in student_list if student['id'] == idd]
    #g1 = [student for student in student_list if course in student['course']]
    return render_template("index.html",list_data=g1)
    
"""
@app.route('/Student/<string:course>', methods =['GET'])
def test3(course):
    g2 = [student for student in student_list if course in student['course']]
    return render_template("index.html",list_data=g2)
"""
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
