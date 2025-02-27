from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1> Миссия Колонизация Марса </h1>'


@app.route('/index')
def about():
    return '<h1> И на Марсе будут яблони цвести! </h1>'


@app.route('/promotion')
def promotion():
    return '''<h1>Человечество вырастает из детства. <br>
Человечеству мала одна планета. <br>
Мы сделаем обитаемыми безжизненные пока планеты. <br>
И начнем с Марса! <br>
Присоединяйся!</h1>'''

@app.route('/image_mars')
def image_mars():
    return render_template('image_mars.html')

@app.route('/promotion_image')
def promotion_image():
    return render_template('promotion_image.html')

@app.route('/astronaut_selection' , methods=['GET', 'POST'])
def astronaut_selection():
    if request.method == 'GET':
        return render_template('astronaut_selection.html')
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['education'])
        print(request.form['profession'])
        print(request.form['motivation'])
        print(request.form['gender'])
        print(request.form['ready'])
        print(request.form['email'])
        return '<h1> Анкета отправлена </h1>'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
    
