from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')  # http://127.0.0.1:5000/projects
def projects():
    return render_template('projects.html')

@app.route('/blogs')
def blogs():  # Corrected the function name
    return render_template('articles.html')

@app.route('/myresume')  # http://127.0.0.1:5000/myresume
def resume():  # Renamed function to better match the route's purpose
    return render_template('resume.html')

@app.route('/contactme')  # http://127.0.0.1:5000/contactme
def contactme():
    return render_template('contact.html')

@app.route('/userdata', methods=['GET', 'POST'])
def userdata():
    if request.method == "POST":
        username = request.form['username']
        userid = request.form['userid']
        u_message = request.form['u_message']
        userdata = [username, userid, u_message]
        
        with open('file.txt', 'a+') as f:
            f.write('\n' + ' '.join(userdata) + '\n')  # Write all data in one line with space separation

        return render_template("contact.html")  # Use a template to show a thank you message
    return "Method not allowed", 405  # Handle GET request inappropriately called here

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
