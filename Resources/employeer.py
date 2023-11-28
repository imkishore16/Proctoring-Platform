from flask import Flask ,request , render_template,url_for,redirect,flash,session
from flask_smorest import Blueprint,abort
from flask_jwt_extended import jwt_required, get_jwt
from db import db
from sqlalchemy.exc import SQLAlchemyError
from BetaFiles.Objective import ObjectiveTest

blp = Blueprint("Employeer", "employeer", description="Operations on authentication")
@blp.route("/employeer_index")
# @user_role_employeer
def employeer_index():
    return render_template('employeer_index.html')

@blp.route("/generate_test")
# @user_role_employeer
def generate_test():
    return render_template('generatetest.html')


@blp.route('/test_generate', methods=["GET", "POST"])
# @user_role_professor
def test_generate():
    if request.method == "POST":
        inputText = request.form["itext"]
        testType = request.form["test_type"]
        noOfQues = request.form["noq"]
        if testType == "objective":
            print(1)
            objective_generator = ObjectiveTest(inputText, noOfQues)
            print(2)
            question_list, answer_list = objective_generator.generate_test()
            print(question_list)
            testgenerate = zip(question_list, answer_list)
            return render_template('generatedtestdata.html', cresults=testgenerate)
        # elif testType == "subjective":
        #     subjective_generator = SubjectiveTest(inputText, noOfQues)
        #     question_list, answer_list = subjective_generator.generate_test()
        #     testgenerate = zip(question_list, answer_list)
        #     return render_template('generatedtestdata.html', cresults=testgenerate)
        else:
            return None


@blp.route('/viewquestions', methods=['GET'])
# @user_role_professor
def viewquestions():
    # cur = mysql.connection.cursor()
    # results = cur.execute(
    #     'SELECT test_id from teachers where email = %s and uid = %s', (session['email'], session['uid']))
    # if results > 0:
    #     cresults = cur.fetchall()
    #     cur.close()
    #     return render_template("viewquestions.html", cresults=cresults)
    # else:
        return render_template("viewquestions.html", cresults=None)


@blp.route('/updatetidlist', methods=['GET'])
# @user_role_professor
def updatetidlist():
    # cur = mysql.connection.cursor()
    # results = cur.execute(
    #     'SELECT * from teachers where email = %s and uid = %s', (session['email'], session['uid']))
    # if results > 0:
    #     cresults = cur.fetchall()
    #     now = datetime.now()
    #     now = now.strftime("%Y-%m-%d %H:%M:%S")
    #     now = datetime.strptime(now, "%Y-%m-%d %H:%M:%S")
    #     testids = []
    #     for a in cresults:
    #         if datetime.strptime(str(a['start']), "%Y-%m-%d %H:%M:%S") > now:
    #             testids.append(a['test_id'])
    #     cur.close()
    #     return render_template("updatetidlist.html", cresults=testids)
    # else:
        return render_template("updatetidlist.html", cresults=None)









# @blp.route('/changepassword_professor')
# # @user_role_professor
# def changepassword_professor():
#     return render_template('changepassword_professor.html')