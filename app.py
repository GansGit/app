import bottle
from bottle import route, run, template, redirect, request, get, auth_basic, abort, response
import MySQLdb as db


@route('/list')
def view_list():
        ip = request.get('REMOTE_ADDR')
        return template ('list.html', ip=ip, rows = GetAllAuthors())
@route('/')
def default():
        redirect('/login')
@route ('/login')
def view_login():
        return template('login.html')

#########BALANCER TESTING########
#@route('/my_ip')
#def show_ip():
   # ip = request.environ.get('REMOTE_ADDR')
   # ip = request.get('REMOTE_ADDR')
   # or ip = request['REMOTE_ADDR']
   #return template("Your IP is: {{ip}}", ip=ip)

def GetAllAuthors():
    connect = db.connect('localhost', 'root', 'pass', 'test')
    with connect:
        curs = connect.cursor()
        curs.execute("select books.Title, authors.name_first, authors.name_last, authors.country from  books inner join  authors on books.AuthorID = authors.AuthorID")
        rows = curs.fetchall()
        desc = curs.description
        #print desc
        #print "%s %s %s %s" % (desc[0][0], desc[1][0], desc[2][0], desc[3][0])
        #for row in rows:
           #print "%d %s %s %s" % row
        return rows
    curs.close()
GetAllAuthors()

run (host='0.0.0.0', port=80, debug=True, reloader=True)

