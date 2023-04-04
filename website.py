

from flask import Flask, render_template,request
from finalgui import Weight_Loss, Weight_Gain, Healthy
app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/", methods=['GET','POST'])
def abc():
	if request.method == "POST":
		weight = float(request.form['name'])
		height = float(request.form['n1'])
		age = int(request.form['n2'])
		meal = int(request.form['n3'])
		recommendation_type = int(request.form['n4'])
		if recommendation_type == 1:
			recommendation = Weight_Loss(weight, height, age, meal)
		elif recommendation_type == 2:
			recommendation = Weight_Gain(weight, height, age, meal)
		else:
			recommendation = Healthy(weight, height, age, meal)
		return render_template('result_page.html',result=enumerate(recommendation))
	return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
    