from flask import Flask, render_template, send_file
app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html')
@app.route('/')
def loader():
    return render_template('loader.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/blogs')
def blogs():
    return render_template('blogs.html')

@app.route('/singleblog')
def singleblog():
    return render_template('singleblog.html')

@app.route('/resume')
def resume():
    return send_file('static/resume.pdf')

if __name__ == '__main__':
    app.run(debug=True)
