import os
from bottle import *

@route('/')
def index():
  return "halló Þröstur!"
  
return(host='0.0.0.0', port=os.envrion.get('PORT'))
