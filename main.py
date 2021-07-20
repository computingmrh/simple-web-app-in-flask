from flask import *

app = Flask(__name__)

blog1 = {"content":"This is an amazing blog!", "title":"Clickbait","ID":1}
blog2 = {"content":"What? Even more????", "title":"Look at them now","ID":2}
blogList =[blog1, blog2]

@app.route('/')
def homePage():
    return render_template("home.html",name="Betty", age=15)

@app.route('/second')
def secondPage():
    return render_template("secondPage.html")

@app.route("/blog")
def blogPage():
	global blogList
	return render_template("blogSummary.html", blogs = blogList)

@app.route("/viewBlog/<blogid>")
def viewBlog(blogid):
	global blogList
	for b in blogList:
		if b["ID"] == int(blogid):
			return render_template("viewBlog.html", 
			blog = b)

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")











