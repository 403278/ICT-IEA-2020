from flask import Flask, render_template, url_for, request
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('sensors.html')


@app.route('/sensors')
def sensors():
    print("now we are here in the sensors end-point")
    return render_template('sensors.html', title='Sensors')


@app.route('/about')
def about():
    print("now we are here in the about end-point")
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)