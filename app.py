# -*- coding: utf-8 -*- 

from flask import Flask, render_template, request, url_for, redirect, flash
import pylib
import datetime
from geoip import geolite2

app = Flask(__name__)
# Create dummy secrey key so we can use sessions
app.secret_key = pylib.get_random_uuid()

@app.route('/')
def webprint():
    return render_template('index.html') 

@app.route('/req', methods=['POST'])
def customer_request():
    print request.form
    model = request.form.get('model', u'').encode('utf-8')
    vin = request.form.get('vin', u'').encode('utf-8')
    tel = request.form.get('tel', u'').encode('utf-8')
    if not tel:
        flash("Извините но не указан контакт. Заполните пожалуйста.")
        return redirect(url_for('webprint'))   
    message = "Сообщение отослано. С вами свяжутся в ближайшее время {}. Спасибо".format(tel)
    match = geolite2.lookup(request.remote_addr)
    email_message = "Bремя заявки={}\nIPaddress={}; {}\n"\
        "Страна-{}\nВременная зона клиента-{}\nLat/Lon={}\n"\
        "Модель={}\nVIN={}\nТелефон={}\n".format(
        datetime.datetime.now().strftime("%Y-%B-%d %H:%M:%S"),
        request.environ.get('REMOTE_ADDR'),
        request.remote_addr,
        match.country,
        match.timezone,
        match.location,
        model, vin, tel)
    subj = "Заявка с сайта bymotor.ru"
    flash(message)
    pylib.send_email(subj, email_message)
    return redirect(url_for('webprint'))

@app.route('/full_order_reqest', methods=['POST'])
def customer_full_request():
    print request.form
    mark = request.form.get('mark', u'').encode('utf-8')
    model = request.form.get('model', u'').encode('utf-8')
    year = request.form.get('year', u'').encode('utf-8')
    volume = request.form.get('volume', u'').encode('utf-8')
    power = request.form.get('power', u'').encode('utf-8')
    engine = request.form.get('engine', u'').encode('utf-8')
    gearbox = request.form.get('gearbox', u'').encode('utf-8')
    marknotes = request.form.get('marknotes', u'').encode('utf-8')
    addons = request.form.get('addons', u'').encode('utf-8')
    username = request.form.get('username', u'').encode('utf-8')
    userphone = request.form.get('userphone', u'').encode('utf-8')
    useremail = request.form.get('useremail', u'').encode('utf-8')
    match = geolite2.lookup(request.remote_addr)
    
    if not userphone or not useremail or not username:
        flash("Извините но не указан ни один контакт. Заполните пожалуйста.")
        return redirect(url_for('webprint'))

    message = "Подробная заявка отослана. С вами свяжутся в ближайшее время. Спасибо {}".format(username)
    subj = "Подробная Заявка с сайта bymotor.ru"
    email_message = "Bремя заявки={}\nIPaddress={}; {}\n"\
        "Страна={}  Временная зона клиента={}  Lat/Lon={}\n"\
        "Марка={}  Модель={}  Год={}\n"\
        "ОбъемДвиг={}  Мощность={}  ТипДвиг={}\n"\
        "Коробка={}  Маркировка={}  НавесноеОбор={}\n"\
        "Имя={}  Тел={} Email={}\n".format(
        datetime.datetime.now().strftime("%Y-%B-%d %H:%M:%S"),
        request.environ.get('REMOTE_ADDR'), request.remote_addr,
        match.country, match.timezone, match.location,
        mark, model, year, volume, power, engine, gearbox, marknotes, addons,
        username, userphone, useremail)

    flash(message)
    pylib.send_email(subj, email_message)
    return redirect(url_for('webprint'))

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80, debug=True)

