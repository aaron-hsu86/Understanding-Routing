from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/dojo')
def dojo():
    return 'dojo'

@app.route('/say/<name>')
def hello_name(name):
    if name.isnumeric() == True:
        return "Please don't use numbers"
    else:
        return f'Hi {name.capitalize()}!' # seen in solution. Capitalizes name if they put in lowercase

@app.route('/repeat/<num>/<result>') # in solution: /<int:num>/<string:word>
def repeat_result_num(num, result):
    if num.isnumeric(): # solution basically confirms value put into address is a num
        return f'<p>{result}</p>'*int(num)
    else:
        return f'{num} is not a valid number. Please provide a valid number.'
    
@app.route('/<other>')
def other_pages(other):
    return 'Sorry! No response. Try again.'
    

# app.run(debug=True) should be the very last statement! 
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.