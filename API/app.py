from flask import Flask

app = Flask(__name__)

recipie1 = "Recipe Name: Spicy Chicken and Rice Bowl<br>Nutrition (per serving): Calories: 590, Carbs: 75g, Protein: 30g, Fat: 18g<br>Ingredients:<br>- 2 boneless, skinless chicken breasts<br>"
recipie2 = "Recipe Name: Quick Chickpea Salad<br>Nutrition: Calories:  300, Total Fat:  10g, Carbohydrates: 30g, Protein: 10g "

@app.route('/')
def main_homepage_function():
    htmloutvar = ''
    for i in range(7):
        htmloutvar = htmloutvar + "This is line " + str(i) + "<br>"
    return htmloutvar

@app.route('/recipies/<recipieid>')
def recipieshow(recipieid):
    if recipieid == 1:
        return recipie1
    elif recipieid == 2:
        return recipie2
    else:
        return "Not yet input"

@app.route('/toothbrushes')

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)