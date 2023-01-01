from flask import Blueprint, render_template , request, redirect, url_for, flash
from models.ModelUsuarios import Users
from utils.conexion import db
from flask_login import  current_user, login_required
import random

operations = Blueprint('operations', __name__)

@operations.route('/welcomeUser')
@login_required
def welcomeUser():
    return render_template('home.html')

@operations.route('/exercise4')
@login_required
def exercise4():
    greetWM = []
    greetWW = []
    greetMW = []
    greetMM = []

    candidatesWoman = []
    candidatesMan = []

    mens = ['fernando', 'jose', 'martin', 'angel', 'jorge', 'tomas', 'francisco', 'omar','rodolfo', 'agustin', 'mario', 'ricardo', 'leonardo', 'vicente', 'luis', 'miguel', 'guillermo', 'javier', 'euduardo', 'alejandro', 'pedro', 'cesar', 'pablo', 'julian', 'jesus']
    womens = ['laura', 'edith', 'jimena', 'alejandra', 'barbara', 'arely', 'martha', 'teresa', 'maria', 'marina', 'miriam', 'samanta', 'lucia', 'leticia', 'linda', 'ana', 'liliana', 'elena','juliana', 'elisa', 'yolanada', 'raquel', 'gloria', 'selena', 'estefania']
    
    print('**Candidatos:')
    for i in range(1,7):
        woman = random.randint(0,24)
        man = random.randint(0,24)
        candidate = [womens[woman].capitalize(), mens[man].capitalize()]
        gender = random.randint(0,1)
        if gender == 0:  
            candidatesWoman.append(candidate[gender])
        else:
            candidatesMan.append(candidate[gender])
  
    print(' ')
    print('**Saludo: ')
    for i in candidatesWoman:

        for h in mens:
            greetWM.append(f'Estimado: {h.capitalize()}, soy la candidata: {i}')

        for m in womens:
            greetWW.append(f'Estimada: {m.capitalize()}, soy la candidata: {i}')

    for i in candidatesMan:
        for h in mens:
            greetMM.append(f'Estimado: {h.capitalize()}, soy el candidato: {i}')
        for m in womens:
            greetMW.append(f'Estimada: {m.capitalize()}, soy el candidato: {i}')

    return render_template('exercise4.html', name=current_user.name, 
    candidatesWoman = candidatesWoman, candidatesMan=candidatesMan,greetWM=greetWM, greetWW = greetWW,
    greetMM=greetMM, greetMW=greetMW )

@operations.route('/exercise5')
@login_required
def exercise5():
    mylist = []
    numMinors = []
    numGreater = []
    numSame = []
    numMultiples = []
    
    #My list
    for i in range(1,200):
        mynumber = random.randint(1,100)
        mylist.append(mynumber)
    mylist.sort()
  
    #Miniors
    for i in mylist:
        if mynumber <= i:
            break
        else:
            numMinors.append(i)
    long = len(numMinors)
    if long == 0:
        flash(f'No hay numero menores a {mynumber}')
    else:
        numMinors

    #Greater
    for i in mylist:
        if mynumber >= i:
            continue
        else:
            numGreater.append(i)
    long = len(numGreater)
    if long == 0:
        flash(f'No hay números mayores a {mynumber}')
    else:
        numGreater
    #Same
    for i in mylist:
        if mynumber == i:
            numSame.append(i)
        else:
            continue
    long = len(numSame)
    if long == 0:
        flash(f'No hay números iguales a{mynumber}')
        i = 'No hay números iguales'
        numSame.append(i)
    else:
        numSame
    #multiplos
    for i in mylist:
        if mynumber % i == 0:
            numMultiples.append(i)
        else:
            continue
    long = len(numMultiples)
    if long == 0:
        flash('No hay números iguales')
        i = 'No hay números iguales'
        numMultiples.append(i)
    else:
        numMultiples

    return render_template('exercise5.html', 
    name=current_user.name, mylist = mylist, mynumber=mynumber, numMinors=numMinors,
    numGreater=numGreater, numSame=numSame, numMultiples=numMultiples)


@operations.route('/register_user', methods=['POST'])
def register_user():
    try:
        name =request.form['name']
        name = name.capitalize()
        lastname = request.form['lastname']
        lastname =lastname.capitalize()
        nickname = request.form['nickname']
        len(nickname)
        while nickname.islower() == True  or nickname.isupper == True:
            flash("Nickname invalido, debe contener al menos una letra mayuscula y minuscula")
            return render_template('register_user.html')
        while nickname.isalpha() == True or nickname.isdigit() == True:
            flash("Nu nickname invalido, debe contener numeros y letras")
            return render_template('register_user.html')
        while len(nickname) < 6:
            flash("Nickname invalido, debe contener al menos 6 caracteres")
            return render_template('register_user.html')
        while nickname.isalpha() == True:
            flash("Nickname invalido, solo debe tener letras y numeros")
            return render_template('register_user.html')
        while nickname.isalnum() == False:
            flash("Nickname invalido, solo debe tener letras y numeros")
            return render_template('register_user.html')
        while nickname.find(" ") >= 1:
            return render_template('register_user.html')
        password = request.form['password']
        len(password)
        while password.islower() == True  or password.isupper == True:
            flash('su contraseña invalida, debe contener al menos una letra mayuscula y minuscula')
            return render_template('register_user.html')
        while password.isalpha() == True or password.isdigit() == True:
            flash("su contraseña invalida, debe contener numeros y letras")
            return render_template('register_user.html')
        while len(password) < 8:
            flash("su contraseña invalida, debe contener al menos 8 caracteres")
            return render_template('register_user.html')
        while password.isalpha() == True:
            flash("su contraseña invalida, debe tener letras y numeros")
            return render_template('register_user.html')
        while password.isalnum() == True:
            flash("su contraseña invalida, debe tener al menos un caracter no alfanumerico")
            return render_template('register_user.html')
        while password.find(" ") >= 1:
            flash("su contraseña invalida, no debe contener espacios")
            return render_template('register_user.html')        
        password2 = request.form['password2']
        while password != password2:
            flash("las contraseñas deben de ser iguales")
            return render_template('register_user.html')    
        user = Users.query.filter_by(nickname=nickname).first()
        if user:
            flash('usuario ya existe')
            return redirect(url_for('login.index'))
        new_user = Users(name =name, lastname=lastname, nickname=nickname, password=password)
        new_user.create_pw(password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login.index'))
    except Exception as e:
        db.session.rollback()
        db.session.close()
        print(f'error: {e}')
        return redirect(url_for('login.index'))


