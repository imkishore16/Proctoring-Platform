from flask import Flask ,request , render_template,url_for,redirect,flash,session
from flask_smorest import Blueprint,abort
from flask_jwt_extended import jwt_required, get_jwt
from db import db
from sqlalchemy.exc import SQLAlchemyError
from BetaFiles.Objective import ObjectiveTest

from coolname import generate_slug
from werkzeug.utils import secure_filename
import pandas as pd
from helper_funcs import UploadForm



blp = Blueprint("Employer", "employer", description="Operations on authentication")
@blp.route("/employer_index")
# @user_role_employer
def employer_index():
    return render_template('employer_index.html')

@blp.route("/generate_test")
# @user_role_employer
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
            # print(1)
            # objective_generator = ObjectiveTest(inputText, noOfQues)
            # print(2)
            # question_list, answer_list = objective_generator.generate_test()
            # print(question_list)
            # testgenerate = zip(question_list, answer_list)
            testgenerate=zip(["what is your name","How are you"],["a","c"])
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
    

@blp.route('/updatedispques', methods=['GET', 'POST'])
# @user_role_professor
def updatedispques():
    # if request.method == 'POST':
    #     tidoption = request.form['choosetid']
    #     et = examtypecheck(tidoption)
    #     if et['test_type'] == "objective":
    #         cur = mysql.connection.cursor()
    #         cur.execute('SELECT * from questions where test_id = %s and uid = %s',
    #                     (tidoption, session['uid']))
    #         callresults = cur.fetchall()
    #         cur.close()
    #         return render_template("updatedispques.html", callresults=callresults)
    #     elif et['test_type'] == "subjective":
    #         cur = mysql.connection.cursor()
    #         cur.execute('SELECT * from longqa where test_id = %s and uid = %s',
    #                     (tidoption, session['uid']))
    #         callresults = cur.fetchall()
    #         cur.close()
    #         return render_template("updatedispquesLQA.html", callresults=callresults)
    #     elif et['test_type'] == "practical":
    #         cur = mysql.connection.cursor()
    #         cur.execute('SELECT * from practicalqa where test_id = %s and uid = %s',
    #                     (tidoption, session['uid']))
    #         callresults = cur.fetchall()
    #         cur.close()
    #         return render_template("updatedispquesPQA.html", callresults=callresults)
    #     else:
    #         flash('Error Occured!')
    #         return redirect(url_for('updatetidlist'))
    pass

        # DELETE
# @blp.route('/delete_questions/<testid>', methods=['GET', 'POST'])
# # @user_role_professor
# def delete_questions(testid):
#     et = examtypecheck(testid)
#     if et['test_type'] == "objective":
#         cur = mysql.connection.cursor()
#         msg = ''
#         if request.method == 'POST':
#             testqdel = request.json['qids']
#             if testqdel:
#                 if ',' in testqdel:
#                     testqdel = testqdel.split(',')
#                     for getid in testqdel:
#                         cur.execute('DELETE FROM questions WHERE test_id = %s and qid =%s and uid = %s', (
#                             testid, getid, session['uid']))
#                         mysql.connection.commit()
#                     resp = jsonify(
#                         '<span style=\'color:green;\'>Questions deleted successfully</span>')
#                     resp.status_code = 200
#                     return resp
#                 else:
#                     cur.execute('DELETE FROM questions WHERE test_id = %s and qid =%s and uid = %s', (
#                         testid, testqdel, session['uid']))
#                     mysql.connection.commit()
#                     resp = jsonify(
#                         '<span style=\'color:green;\'>Questions deleted successfully</span>')
#                     resp.status_code = 200
#                     return resp
#     elif et['test_type'] == "subjective":
#         cur = mysql.connection.cursor()
#         msg = ''
#         if request.method == 'POST':
#             testqdel = request.json['qids']
#             if testqdel:
#                 if ',' in testqdel:
#                     testqdel = testqdel.split(',')
#                     for getid in testqdel:
#                         cur.execute('DELETE FROM longqa WHERE test_id = %s and qid =%s and uid = %s', (
#                             testid, getid, session['uid']))
#                         mysql.connection.commit()
#                     resp = jsonify(
#                         '<span style=\'color:green;\'>Questions deleted successfully</span>')
#                     resp.status_code = 200
#                     return resp
#                 else:
#                     cur.execute('DELETE FROM longqa WHERE test_id = %s and qid =%s and uid = %s', (
#                         testid, testqdel, session['uid']))
#                     mysql.connection.commit()
#                     resp = jsonify(
#                         '<span style=\'color:green;\'>Questions deleted successfully</span>')
#                     resp.status_code = 200
#                     return resp
#     elif et['test_type'] == "practical":
#         cur = mysql.connection.cursor()
#         msg = ''
#         if request.method == 'POST':
#             testqdel = request.json['qids']
#             if testqdel:
#                 if ',' in testqdel:
#                     testqdel = testqdel.split(',')
#                     for getid in testqdel:
#                         cur.execute('DELETE FROM practicalqa WHERE test_id = %s and qid =%s and uid = %s', (
#                             testid, getid, session['uid']))
#                         mysql.connection.commit()
#                     resp = jsonify(
#                         '<span style=\'color:green;\'>Questions deleted successfully</span>')
#                     resp.status_code = 200
#                     return resp
#             else:
#                 cur.execute('DELETE FROM questions WHERE test_id = %s and qid =%s and uid = %s',
#                             (testid, testqdel, session['uid']))
#                 mysql.connection.commit()
#                 resp = jsonify(
#                     '<span style=\'color:green;\'>Questions deleted successfully</span>')
#                 resp.status_code = 200
#                 return resp
#     else:
#         flash("Some Error Occured!")
#         return redirect(url_for('/deltidlist'))

## many helper funtions inbetween

@blp.route("/livemonitoringtid")
# @user_role_professor
def livemonitoringtid():
    # cur = mysql.connection.cursor()
    # results = cur.execute(
    #     'SELECT * from teachers where email = %s and uid = %s and proctoring_type = 1', (session['email'], session['uid']))
    # if results > 0:
    #     cresults = cur.fetchall()
    #     now = datetime.now()
    #     now = now.strftime("%Y-%m-%d %H:%M:%S")
    #     now = datetime.strptime(now, "%Y-%m-%d %H:%M:%S")
    #     testids = []
    #     for a in cresults:
    #         if datetime.strptime(str(a['start']), "%Y-%m-%d %H:%M:%S") <= now and datetime.strptime(str(a['end']), "%Y-%m-%d %H:%M:%S") >= now:
    #             testids.append(a['test_id'])
    #     cur.close()
    #     return render_template("livemonitoringtid.html", cresults=testids)
    # else:
    #     return render_template("livemonitoringtid.html", cresults=None)
    return render_template("livemonitoringtid.html", cresults=None)

@blp.route('/create-test', methods=['GET', 'POST'])
# @user_role_professor
def create_test():
    form = UploadForm()
    if request.method == 'POST' and form.validate_on_submit():
        test_id = generate_slug(2)
        filename = secure_filename(form.doc.data.filename)
        filestream = form.doc.data
        filestream.seek(0)
        ef = pd.read_csv(filestream)
        fields = ['qid', 'q', 'a', 'b', 'c', 'd', 'ans', 'marks']
        df = pd.DataFrame(ef, columns=fields)
        # cur = mysql.connection.cursor()
        # ecc = examcreditscheck()
        # if ecc:
        if 1:
            # for row in df.index:
            #     cur.execute('INSERT INTO questions(test_id,qid,q,a,b,c,d,ans,marks,uid) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (test_id,
            #                 df['qid'][row], df['q'][row], df['a'][row], df['b'][row], df['c'][row], df['d'][row], df['ans'][row], df['marks'][row], session['uid']))
            #     cur.connection.commit()

            start_date = form.start_date.data
            end_date = form.end_date.data
            start_time = form.start_time.data
            end_time = form.end_time.data
            start_date_time = str(start_date) + " " + str(start_time)
            end_date_time = str(end_date) + " " + str(end_time)
            neg_mark = int(form.neg_mark.data)
            calc = int(form.calc.data)
            duration = int(form.duration.data)*60
            password = form.password.data
            subject = form.subject.data
            topic = form.topic.data
            proctor_type = form.proctor_type.data
            cur.execute('INSERT INTO teachers (email, test_id, test_type, start, end, duration, show_ans, password, subject, topic, neg_marks, calc,proctoring_type, uid) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                        (dict(session)['email'], test_id, "objective", start_date_time, end_date_time, duration, 1, password, subject, topic, neg_mark, calc, proctor_type, session['uid']))
            mysql.connection.commit()
            cur.execute('UPDATE users SET examcredits = examcredits-1 where email = %s and uid = %s',
                        (session['email'], session['uid']))
            mysql.connection.commit()
            cur.close()
            flash(f'Exam ID: {test_id}', 'success')
            return redirect(url_for('professor_index'))
        else:
            flash("No exam credits points are found! Please pay it!")
            return redirect(url_for('professor_index'))
    return render_template('create_test.html', form=form)


@blp.route('/live_monitoring', methods=['GET', 'POST'])
# @user_role_professor
def live_monitoring():
    if request.method == 'POST':
        testid = request.form['choosetid']
        return render_template('live_monitoring.html', testid=testid)
    else:
        return render_template('live_monitoring.html', testid=None)








# @blp.route('/changepassword_professor')
# # @user_role_professor
# def changepassword_professor():
#     return render_template('changepassword_professor.html')