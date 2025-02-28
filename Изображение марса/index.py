from flask import Flask, url_for

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

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')