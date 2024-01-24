from flask import Flask,render_template,request
import os

app = Flask(__name__)

app.config['UPLOAD_PATH'] = 'static/images'#uploading path

# @app.route('/') #'/' - to refer homepage
# def home():
#     return "Home " 

# @app.route('/<name>') #'/' - to give dynamic url 
# def home(name):
#     return "Home " + name

# eg: http://127.0.0.1:5000/athisruth -example url to run

# @app.route('/<int:num1>') #'/' - to give dynamic url 
# def home(num1):
#     return f"Home {num1}" 

# eg: http://127.0.0.1:5000/5 -example url to run


# @app.route('/<int:age>') #'/' - to give dynamic url 
# def home(age):
#     if age < 18 :
#         return 'Age Restriction: Not Allowed'
#     else:
#         return 'You are allowed'


@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/product')
def product():
    return render_template('product.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['text'] == 'user' and request.form['password'] == 'hello':
            return render_template('dashboard.html')
        else:
            error = "Wrong username or password"
            return render_template('login.html', error=error)
    else:
        return render_template('login.html')

        




# @app.route('/laptop')
# def laptop():
#     return "laptop page"


# @app.route('/') #'/' - to give dynamic url 
# def home():
#         return render_template('index.html')


# @app.route('/<name>') #'/' - to give dynamic url 
# def home(name):
#         return render_template('index.html',variable_for_homepage=name)#this name is used in our html page,this variable 'name' is added to the html page. 


# @app.route('/<int:num1>') #'/' - to give dynamic url 
# def integ(num1):
#     return render_template('index.html',variable_for_homepage = num1)#this name is used in our html page,this variable 'name' is added to the html page. 


# @app.route('/about') #'/' - to give dynamic url 
# def about():
#     return render_template('about.html')#this name is used in our html page,this variable 'name' is added to the html page. 


# to map our url with a function
# app.add_url_rule('/home','home',home) #'home' -end point name ,home -function name


# @app.route('/') #'/' - to give dynamic url 
# def form():
#     return render_template('form_post_method.html')

# register get method
# @app.route('/register_get_method',methods=['GET'])
# def register():  #how to store the values that we enter in the form to a variable. 
#     name = request.args.get('name')#we need to add the 'name' that we given inside the html tag. 
#     number = request.args.get('number')
#     email = request.args.get('email')
#     return render_template('register_get_method.html',name=name,number=number,email=email)


# register post method

# @app.route('/register',methods=['POST'])#using post method we cannot see the input details inside the url
# def register():  #how to store the values that we enter in the form to a variable. 
#     name = request.form['name'] #we need to add the 'name' that we given inside the html tag. 
#     number = request.form['number']
#     email = request.form['email']
#     return render_template('register.html', name = name, number = number, email = email)


#In form actions we give the link used to move to new page after clicking the submit button. 

# @app.route('/') #'/' - to give dynamic url 
# def form():
#     return render_template('file_upload.html')

@app.route('/') #'/' - to give dynamic url 
def homepage():
    return render_template('homepage.html')


@app.route('/upload', methods = ['POST'])
def upload():
    file =request.files['file']
    file.save(os.path.join(app.config['UPLOAD_PATH'], file.filename))
    return "Uploaded successfully"


if __name__ == "__main__":
    app.run(debug=True)#debug=True adding this feature to get result in the browser directly without rerunning the server. 


# App Routing
    
    # Mapping specific URL with associated function

    # eg:www.website.com -> ('/')
    #    www.website.com -> ('/product')


#add_url_rule() function
    

# Dynamic url
    

# we can add style to our html by giving  link to our css file 
#never add comas in html files

# eg:<link rel="stylesheet" href="./static/css/style.css"> 
    

    # or

# <link rel="stylesheet" href="{{ url_for('static',filename='css/style.css')}}"> 

# To improve the formatting of your HTML source code, you can use the Format Document command Ctrl+Shift+I to format the entire file or Format Selection Ctrl+K Ctrl+F to just format the selected text.


    


    
