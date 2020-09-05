from flask import Flask, render_template
app = Flask(__name__)

@app.route( '/' )
def piWeather():
    temp = 15;
    hmdty = 70;
    return render_template( 'index.html', temperature=temp, humidity=hmdty )
