from flask import Flask

app = Flask(__name__)

@app.route('/')
def main_homepage_function():
    htmloutvar = ''
    for i in range(7):
        htmloutvar = htmloutvar + "This is line " + str(i) + "\n"
    return htmloutvar

    return 

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)