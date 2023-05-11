from flask import Flask, request

app = Flask(__name__)

recipiedb = [
    "Recipe Name: Spicy Chicken and Rice Bowl<br>Nutrition (per serving): Calories: 590, Carbs: 75g, Protein: 30g, Fat: 18g<br>Ingredients:<br>- 2 boneless, skinless chicken breasts<br>",
    "Recipe Name: Quick Chickpea Salad<br>Nutrition: Calories:  300, Total Fat:  10g, Carbohydrates: 30g, Protein: 10g "    
    ]

@app.route('/')
def main_homepage_function():
    htmloutvar = ''
    for i in range(7):
        htmloutvar = htmloutvar + "This is line " + str(i) + "<br>"
    return htmloutvar

@app.route('/name/<inputname>')
def prtname(inputname):
    return "Hello " + inputname 


@app.route('/recipies/<recipieid>')
def recipieshow(recipieid):
    if len(recipiedb) <= int(recipieid):
        return "No Recipie"
    else:
        return recipiedb[int(recipieid)]

@app.route('/delrecipie/<recipieid>', methods=['GET','DELETE'])
def recipiedel(recipieid):
    if request.method == 'DELETE':
        recipiedb.pop(int(recipieid))
    else:
        return "You need to use a DELETE http method<br>"



@app.route('/toothbrushes')
def toothbrushes():
    pass

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)