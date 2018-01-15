## HW 1
## SI 364 W18
## 1000 points

#################################

## List below here, in a comment/comments, the people you worked with on this assignment AND any resources you used to find code (50 point deduction for not doing so). If none, write "None".
#Kyle E.
# https://developers.google.com/maps/documentation/static-maps/intro

## [PROBLEM 1] - 150 points
## Below is code for one of the simplest possible Flask applications. Edit the code so that once you run this application locally and go to the URL 'http://localhost:5000/class', you see a page that says "Welcome to SI 364!"

from flask import Flask, request
from string import Template
import requests
import json
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_to_you():
    return 'Welcome to SI 364!'



## [PROBLEM 2] - 250 points
## Edit the code chunk above again so that if you go to the URL 'http://localhost:5000/movie/<name-of-movie-here-one-word>' you see a big dictionary of data on the page. For example, if you go to the URL 'http://localhost:5000/movie/ratatouille', you should see something like the data shown in the included file sample_ratatouille_data.txt, which contains data about the animated movie Ratatouille. However, if you go to the url http://localhost:5000/movie/titanic, you should get different data, and if you go to the url 'http://localhost:5000/movie/dsagdsgskfsl' for example, you should see data on the page that looks like this:

# {
#  "resultCount":0,
#  "results": []
# }


## You should use the iTunes Search API to get that data.
## Docs for that API are here: https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/
## Of course, you'll also need the requests library and knowledge of how to make a request to a REST API for data.

## Run the app locally (repeatedly) and try these URLs out!

@app.route('/movie/<movie>')
def get_itunes_data(movie):
	baseurl = 'https://itunes.apple.com/search?'
	search_term = 'term=' + movie
	resp = requests.get(baseurl+search_term)
	text = resp.text
	python_obj = json.dumps(text)
	#python_obj = python_obj.replace('\n', '')
	x = json.loads(python_obj)
	return x

## [PROBLEM 3] - 250 points

## Edit the above Flask application code so that if you run the application locally and got to the URL http://localhost:5000/question, you see a form that asks you to enter your favorite number.
## Once you enter a number and submit it to the form, you should then see a web page that says "Double your favorite number is <number>". For example, if you enter 2 into the form, you should then see a page that says "Double your favorite number is 4". Careful about types in your Python code!
## You can assume a user will always enter a number only.
@app.route('/question')
def fav_number():
	s = """<!DOCTYPE html>
<html>
<body>
<form action ="/result" method = "POST">
  Enter your favorite number:<br>
  <input type="text" name="favorite_number">
  <br>
  <input type="submit" value="Submit">
</form>
</body>
</html>"""
	return s

@app.route('/result', methods=['GET', 'POST'])
def double_number():
    if request.method == 'POST':
    	double = request.form['favorite_number']
    	double = int(double)
    	return 'Double your favorite number is ' + str(double*2)

## [PROBLEM 4] - 350 points

## Come up with your own interactive data exchange that you want to see happen dynamically in the Flask application, and build it into the above code for a Flask application, following a few requirements.

## You should create a form that appears at the route: http://localhost:5000/problem4form

## Submitting the form should result in your seeing the results of the form on the same page.

## What you do for this problem should:
# - not be an exact repeat of something you did in class
# - must include an HTML form with checkboxes and text entry
# - should, on submission of data to the HTML form, show new data that depends upon the data entered into the submission form and is readable by humans (more readable than e.g. the data you got in Problem 2 of this HW). The new data should be gathered via API request or BeautifulSoup.

#https://www.google.com/maps/search/?api=1&parameters

#my code was working and displaying everything on the same page, but now my view function is not returning a response
@app.route('/problem4form', methods = ['GET'])
def problem_4():
	x = """<!DOCTYPE html>
<html>
<body>
<form action ="/problem4form" method = "GET">
  <h2>Hello There!</h2>
  Please enter your name<br>
  <input type="text" name="name">
  <br>
</form>
</body>
</html>
<br>
<form action="/problem4form" method="GET">
	Where should you travel to next? Pick 1 city.<br>
  <input type="checkbox" name="city1" value="detroit"> City 1 <br>
  <input type="checkbox" name="city2" value="chicago"> City 2 <br>
  <input type="checkbox" name="city3" value="san francisco"> City 3 <br>
  <input type="checkbox" name="city4" value="new york"> City 4 <br>
  <input type="checkbox" name="city5" value="seattle"> City 5 <br>
  <input type="checkbox" name="city6" value="austin"> City 6 <br>
  <input type="submit" value="Submit">
</form>"""
	# return x

# @app.route('/results', methods = ['GET', 'POST'])
# def results():
	if request.method == "GET":
		for city in request.args:
			if city == 'city1':
				return x + '<h1>Welcome to Detroit!</h1><img src="https://maps.googleapis.com/maps/api/staticmap?size=700x300&markers=detroit">'
			elif city == 'city2':
				return x + '<h1>Welcome to Chicago!</h1><img src="https://maps.googleapis.com/maps/api/staticmap?size=700x300&markers=chicago">'
			elif city == 'city3':
				return x + '<h1>Welcome to San Francisco!</h1><img src="https://maps.googleapis.com/maps/api/staticmap?size=700x300&markers=san+francisco">'
			elif city == 'city4':
				return x + '<h1>Welcome to New York!</h1><img src="https://maps.googleapis.com/maps/api/staticmap?size=700x300&markers=new+york">'
			elif city == 'city5':
				return x + '<h1>Welcome to Seattle!</h1><img src="https://maps.googleapis.com/maps/api/staticmap?size=700x300&markers=seattle">'
			elif city == 'city6':
				return x + '<h1>Welcome to Austin!</h1><img src="https://maps.googleapis.com/maps/api/staticmap?size=700x300&markers=austin">'

	
# @app.route('/questions', methods = ['GET','POST'])
# def problem_4_questions():
# 	return """ <form action="http://localhost:5000/results" method='GET'>
# 	Where should you travel to next? Pick 1 city.<br>
#   <input type="checkbox" name="city1" value="detroit"> City 1 <br>
#   <input type="checkbox" name="city2" value="chicago"> City 2 <br>
#   <input type="checkbox" name="city3" value="san francisco"> City 3 <br>
#   <input type="checkbox" name="city4" value="new york"> City 4 <br>
#   <input type="checkbox" name="city5" value="seattle"> City 5 <br>
#   <input type="checkbox" name="city6" value="austin"> City 6 <br>
#   <input type="submit" value="Submit">
# </form>"""

# @app.route('/problem4form', methods = ['GET'])
# def problem_4_results():
    



# You should feel free to be creative and do something fun for you --
# And use this opportunity to make sure you understand these steps: if you think going slowly and carefully writing out steps for a simpler data transaction, like Problem 1, will help build your understanding, you should definitely try that!

# You can assume that a user will give you the type of input/response you expect in your form; you do not need to handle errors or user confusion. (e.g. if your form asks for a name, you can assume a user will type a reasonable name; if your form asks for a number, you can assume a user will type a reasonable number; if your form asks the user to select a checkbox, you can assume they will do that.)

# Points will be assigned for each specification in the problem.
if __name__ == '__main__':
    app.run()