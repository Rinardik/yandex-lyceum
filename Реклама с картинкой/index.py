from flask import Flask, url_for
import requests
app = Flask(__name__)


@app.route('/')
def index_0():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index_1():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def index_2():
    return """Человечество вырастает из детства.</br>Человечеству мала одна планета.</br>Мы сделаем обитаемыми безжизненные пока планеты.</br>И начнем с Марса!</br>Присоединяйся!</br>"""


@app.route('/image_mars')
def index_3():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="static/mars.jpg" alt="здесь должна была быть картинка, но не нашлась">
                  </body>
                </html>"""


@app.route('/promotion_image')
def index_4():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <title>Привет, Марс!</title>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
                    <link href="https://getbootstrap.com/docs/5.3/assets/css/docs.css" rel="stylesheet">
                    <link href='{url_for('static', filename='style.css')}', rel="stylesheet">
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
                  </head>
                  <body class="p-3 m-0 border-0 bd-example m-0 border-0 bd-example-row">  
                    <h1>Жди нас, Марс!</h1>
                    <img src="static/mars.jpg" alt="здесь должна была быть картинка, но не нашлась">
                 
                    </br>    
                    <div class="col"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
                    Человечество вырастает из дества.
                    </font></font></div>
                    </br>
                    <div class="col-sm-9 p-3"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
                    Человечеству мала одна планета.
                    </font></font></div>
                    </br>
                    <div class="col-sm-9 p-3"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
                    Мы сделаем обитаемыми безжизненных пока планеты.
                    </font></font></div>
                    </br>
                    <div class="col-sm-9 p-3"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
                    И начем с Марса
                    </font></font></div>
                    </br>
                    <div class="col-sm-9 p-3"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
                    Присоединяйся!
                    </font></font></div>
                    </br>
                </body>
                </html>"""


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if requests.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Форма для регистрации в суперсекретной системе</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
                                    <div class="form-group">
                                        <label for="classSelect">В каком вы классе</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>7</option>
                                          <option>8</option>
                                          <option>9</option>
                                          <option>10</option>
                                          <option>11</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="about">Немного о себе</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif requests.method == 'POST':
        print(requests.form['email'])
        print(requests.form['password'])
        print(requests.form['class'])
        print(requests.form['file'])
        print(requests.form['about'])
        print(requests.form['accept'])
        print(requests.form['sex'])
        return "Форма отправлена"

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')