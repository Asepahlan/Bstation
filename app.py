from flask import Flask, render_template, request
from main import play_video_in_incognito

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        duration = int(request.form['duration'])
        repeat = int(request.form['repeat'])
        
        # Memutar video menggunakan Selenium
        play_video_in_incognito(url, duration, repeat)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
