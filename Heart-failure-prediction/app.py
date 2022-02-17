from flask import Flask, render_template, request
import pickle
import pandas as pd
import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully") ;

# conn.execute("""CREATE TABLE IF NOT EXISTS tasks (
#                                     Name text,
#                                     Age real,
#                                     Sex real,
#                                     cp real,
#                                     trestbps real,
#                                     chol real,
#                                     fbs real,
#                                     restecg real,
#                                     thalach real,
#                                     exang real,
#                                     Oldpeak real,
#                                     ST_Slope real,
#                                     ca real,
# 				                    thal real
#                                 );""")
#
#
#
# print ("Table created successfully");
# conn.close()


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('original.html')


@app.route("/predict", methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        fname = str(request.form['fname'])
        age = float(request.form['age'])
        sex = float(request.form['sex'])
        cp = float(request.form['cp'])
        trestbps = float(request.form['trestbps'])
        chol = float(request.form['chol'])
        fbs= float(request.form['fbs'])
        restecg = float(request.form['restecg'])
        thalach = float(request.form['thalach'])
        exang = float(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        slope = float(request.form['slope'])
        ca = float(request.form['ca'])
        thal = float(request.form['thal'])
        # con = sqlite3.connect("database.db")
        # cur = con.cursor()
        # cur.execute(
        #     "INSERT INTO tasks (Name,Age,Sex,cp,trestbps,chol,fbs,restecg,thalach,exang,Oldpeak,ST_Slope,ca,thal )VALUES(?, ?, ?, ?,?,?,?,?,?,?,?,?,?,?)",
        #     (fname, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal))
        #
        # con.commit()
        # print("Record successfully added")

        pred_args = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        files = ['Decision_Tree (2).pkl', 'random_forest (1).pkl', 'knn.pkl', 'Naive_Bayes.pkl']
        res=[]
        for model_file in files:

            mul_reg = open(model_file, 'rb')
            ml_model = pickle.load(mul_reg)
            model_predcition = ml_model.predict([pred_args])
            if model_predcition == 1:
                res = 'Affected'
            else:
                res = 'Not affected'


        #return res
    return render_template('predict.html', prediction = res, fname = fname, age = age, sex = sex, cp = cp, trestbps = trestbps, chol = chol, fbs = fbs, restecg = restecg, thalach =thalach, exang = exang, oldpeak = oldpeak, slope =slope, ca = ca, thal = thal )





if __name__ == '__main__':
    app.run()
