from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route("/about")
def about():
    return render_template('about.html')


# 200 API Status
@app.route("/health/200")
def health_ok():
    return {"status": 200}


# 400 API Status
@app.route("/health/400")
def health_error():
    return {"status": 400}


# 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


# 500 error handler
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500
