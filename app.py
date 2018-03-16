# from cork import Cork
import bottle
from bottle import route, run, template, redirect, request, get, auth_basic, abort, response
# import MySQLdb as db
import socket
#print (socket.gethostbyname(socket.gethostname()))


# @route('/list')
# def view_list():
#         return template ('list.html', ip = socket.gethostbyname(socket.gethostname()), rows = GetAllAuthors())
@route('/')
def default():
        redirect('/login')

@get('/login') # or @route('/login')
def login():
        # return '''
        # <form action="/login" method="post">
        #         Username: <input name="username" type="text" />
        #         Password: <input name="password" type="password" />
        #         <input value="Login" type="submit" />
        # </form>
        # '''
        return template ('login.html')

@route('/login', method=['POST']) # or @route('/login', method='POST')
def do_login():
        username = request.forms.get('username')
        password = request.forms.get('password')
        if username== 'maks' and password=='pass':
                #return "<p>Your login information was correct.</p>"
                return template ('list.html', ip = socket.gethostbyname(socket.gethostname()), rows = GetAllAuthors())

        else:
                return "<p>Login failed.</p>"

# @route ('/login')
# def view_login():
#         return template('login.html')

#########BALANCER TESTING########
#@route('/my_ip')
#def show_ip():
   # ip = request.environ.get('REMOTE_ADDR')
   # ip = request.get('REMOTE_ADDR')
   # or ip = request['REMOTE_ADDR']
   #return template("Your IP is: {{ip}}", ip=ip)

#########Acces to DB##########
# def GetAllAuthors():
#     connect = db.connect('localhost', 'root', 'pass', 'test')
#     with connect:
#         curs = connect.cursor()
#         curs.execute("select books.Title, authors.name_first, authors.name_last, authors.country from  books inner join  authors on books.AuthorID = authors.AuthorID")
#         rows = curs.fetchall()
#         desc = curs.description
#         #print desc
#         #print "%s %s %s %s" % (desc[0][0], desc[1][0], desc[2][0], desc[3][0])
#         #for row in rows:
#            #print "%d %s %s %s" % row
#         return rows
#     curs.close()
#GetAllAuthors()

run (host='0.0.0.0', port=80, debug=True, reloader=True)

