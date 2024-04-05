from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'junub'

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lokidormoi@1998",
    database="eddydb"
)


@app.route('/')
def home():
    if 'loggedin' in session:
        return render_template('index.html', username=session['username'])
    return render_template('login.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor = db.cursor()
        sql = "SELECT * FROM `user` WHERE `name` = %s AND `password` = %s"
        cursor.execute(sql, (username, password))
        account = cursor.fetchall()
        cursor.close()

        if account:
            session['loggedin'] = True
            session['username'] = account[0][1]
            session['userID'] = account[0][0]
            return redirect(url_for('home'))
        else:
            flash("Incorrect Username & Password")

    return render_template('login.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        password2 = request.form['password2']

        if password != password2:
            flash('Passwords do not match')
            return redirect(url_for('register'))

        cursor = db.cursor()
        sql = "INSERT INTO User (name, email, Password) VALUES (%s, %s, %s)"
        cursor.execute(sql, (username, email, password))
        db.commit()
        cursor.close()
        flash("Account created successfully")
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    session.clear()
    return redirect(url_for('home'))


# @app.route('/Identification')
# def identification():
#     return render_template('identification.html')


@app.route('/certificate', methods=['POST', 'GET'])
def certificate():
    # operations
    if request.method == 'POST':
        surname = request.form['surname']
        certificatetype = request.form['certificatetype']
        indexnumber = request.form['indexnumber']
        givennames = request.form['givennames']
        gender = request.form['gender']
        schoolname = request.form['schoolname']
        centernumber = request.form['centernumber']
        dateofexam = request.form['dateofexam']
        placeofexam = request.form['placeofexam']
        iddocument = request.files['iddocument']
        cursor = db.cursor()
        sql = "INSERT INTO certificateapplication('surname', 'certificatetype', 'indexnumber', 'givennames', 'gender', 'schoolname', 'centernumber', 'dateofexam', 'placeofexam', 'iddocument')"
        cursor.execute(sql(surname, certificatetype, indexnumber, givennames,
                       gender, schoolname, centernumber, dateofexam, placeofexam, iddocument))
        db.commit()
        cursor.close()
        flash("Certificate added Successfully!")
        return redirect(url_for('certificate'))
    return render_template('certificate.html')


@app.route('/birth-certificate', methods=['POST', 'GET'])
def birth_certificate():
    # Operations
    if request.method == 'POST':
        name = request.form['name']
        sex = request.form['sex']
        place_of_birth = request.form['placeOfBirth']
        county = request.form['county']
        state = request.form['state']
        fatherName = request.form['fatherName']
        motherName = request.form['motherName']

        userID = session['userID']

        cursor = db.cursor()
        sql = "INSERT INTO ageassessment (`userID`, `name`, sex, placeOfBirth, county, `state`, fatherName, motherName) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (userID, name, sex, place_of_birth,
                       county, state, fatherName, motherName))
        db.commit()
        cursor.close()
        flash("Birth Certificate created successfully")
        return redirect(url_for('birth_certificate'))
    return render_template('birth-certificate.html')


@app.route('/nationality', methods=['POST', 'GET'])
def nationality():

    # Operations
    if request.method == 'POST':
        surname = request.form['surname']
        givenname = request.form['givenname']
        sex = request.form['sex']
        mothername = request.form['mothername']
        dateofbirth = request.form['dateofbirth']
        PlaceOfBirth = request.form['placeofbirth']
        typeofNC = request.form['typeofNC']
        birthcertificate = request.form['birthcertificate']
        passportphoto = request.form['passportphoto']

        cursor = db.cursor()
        sql = "INSERT INTO nationality ('surname', 'givenname', 'sex', 'mothername', 'dateofbirth', 'placeofbirth', 'typeofNC', 'birthcertificate', 'passportphoto') VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql(surname, givenname, sex, mothername, dateofbirth,
                       PlaceOfBirth, typeofNC, birthcertificate, passportphoto))
        db.commit()
        cursor.close()
        flash('Natinal ID created Succesfully')
        return redirect(url_for('nationality'))
    return render_template('nationality.html')


@app.route('/equivalent', methods=['POST', 'GET'])
def equivalent():
    # operations
    if request.method == 'POST':
        surname = request.form['surname']
        givenname = request.form['givenname']
        nationality = request.form['nationality']
        identificationdocumenttype = request.form['identificationdocumenttype']
        qualificationlevel = request.form['qualificationlevel']
        country = request.form['country']
        issuingschool = request.form['insuingschool']
        yearoflssuance = request.form['yearofissuance']
        notorizedcertificate = request.form['notorizedcertificate']
        passport = request.form['passport']

        cursor = db.cursor()
        sql = "INSERT INTO equivalent ('surname', 'givenname', 'nationality', 'identificationdocumenttype', 'qualificationlevel', 'country', 'insuingschool', 'yearofissuance', 'notorizedcertificate', 'passport') VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql(surname, givenname, nationality, identificationdocumenttype,
                       qualificationlevel, country, issuingschool, yearoflssuance, notorizedcertificate, passport))
        db.commit()
        cursor.close()
        flash('Equivalent created Successfully')
        return redirect(url_for('equivalent'))
    return render_template('equivalent.html')


@app.route('/correction', methods=['POST', 'GET'])
def correction():
    # operations
    if request.method == 'POST':
        surname = request.form['surname']
        givenname = request.form['givenname']
        sex = request.form['sex']
        dateofbirth = request.form['dateofbirth']
        placeofbirth = request.form['placeofbirth']
        natinalidnumber = request.form['nationalidnumber']
        correctionreason = request.form['correctionreason']
        correction = request.form['correction']

        cursor = db.cursor()
        sql = "INSERT INTO corrections('surname', 'givenname', 'sex', 'dateofbirth', 'placeofbirth', 'nationalidnumber', 'correctionreason', 'correction') VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql(surname, givenname, sex, dateofbirth,
                       placeofbirth, natinalidnumber, correctionreason, correction))
        db.commit()
        cursor.close()
        flash('Correction Created Succesfully')
        return redirect(url_for('correction'))
    return render_template('correction.html')


@app.route('/driving_test')
def driving_test():
    # operations
    if request.method == 'POST':
        fullname = request.form["fullname"]
        gender = request.form["gender"]
        dateofbirth = request.form["dateofbirth"]
        address = request.form['address']
        phonenumber = request.form['phonenumber']
        email = request.form['email']
        testtype = request.form['testtype']
        testdate = request.form['testdate']

        cursor = cursor.db()
        sql = "INSERT INTO drivingtestregistration('fullname', 'gender', 'dateofbirth', 'address', 'phonenumber', 'email', 'testtype', 'testdate') VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql(fullname, gender, dateofbirth, address,
                       phonenumber, email, testtype, testdate))
        db.commit()
        cursor.close()
        flash('Driving Test Recorded Successfully!')
        return redirect(url_for("driving_test"))
    return render_template('driving_test.html')


@app.route('/apply-license', methods=['GET', 'POST'])
def apply_license():
    # operations
    if request.method == "POST":
        fullname = request.form['fullname']
        dateofbirth = request.form['dateofbirth']
        placeofbirth = request.form['placeofbirth']
        gender = request.form['gender']
        address = request.form['address']
        county = request.form['county']
        state = request.form['state']
        fathename = request.form['fathername']
        mothername = request.form['mothername']
        drivingtesttype = request.form['drivingtesttype']
        drivingtestresult = request.form['drivingtestresult']
        iddocument = request.form['iddocument']

        cursor = cursor.db()
        sql = "INSERT INTO applylicense('fullname', 'dateofbirth', 'placeofbirth', 'gender', 'address', 'county', 'state', 'fathername', 'mothername', 'drivingtesttype', 'drivingtestresult', 'iddocument')  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql(fullname, dateofbirth, placeofbirth, gender, address, county,
                       state, fathename, mothername, drivingtesttype, drivingtestresult, iddocument))
        db.commit()
        cursor.close()
        flash('Application for license recorded successfully')
        return redirect(url_for("apply-license"))
    return render_template('apply-license.html')


@app.route('/exam_result', methods=["GET", "POST"])
def exam_result():
    # operations
    if request.method == "POST":
        fullnames = request.form['fullnames']
        testtype = request.form['testtype']
        examdate = request.form['examdate']
        iddocument = request.form['iddocument']

        cursor = cursor.db()
        sql = "INSERT INTO examresult('fullnames', 'testtype', 'examdate', 'iddocument') VALUES (%s, %s, %s, %s)"
        cursor.execute(sql(fullnames, testtype, examdate, iddocument))
        db.commit()
        db.close()
        flash('Application for Exam Test Recorded Successfully!')
        return redirect(url_for("examresult"))
    return render_template('exam_result.html')


@app.route('/ongoing')
def opngoing():
    # logic to fetch all applications of user_id ... from database
    sql = "SELECT * FROM `ageassessment` WHERE `userID` = %s"
    userID = session['userID'][0]
    cursor = db.cursor()
    cursor.execute(sql, (userID,))
    apps = cursor.fetchall()
    cursor.close()

    return render_template('testing.html', applications=apps)


if __name__ == '__main__':
    app.run(debug=True, port=5500)
