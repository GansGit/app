import bottle
from bottle import route, run, template, redirect, request, get, auth_basic, abort, response, post
import base64

# сюда по дуфолту йде запит.
@route ('/')

# сюди, як я поняв має передатись юзернаме та пароль 
def check(u,p):
    
  #вертаю завжди ТРУ
  return True  
    
# методи чи функція яка викликає auth_basic. Приймає результат функ. чек. якщо нічого не передавати - інтерпрітатор скаже шо ерора
# TypeError: auth_basic() missing 1 required positional argument: 'check'
@auth_basic(check)

def home():
    return 'coll'
run (host='0.0.0.0', port=80, debug=True, reloader=True)
