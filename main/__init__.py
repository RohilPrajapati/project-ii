from flask import Flask
app = Flask(__name__)

app.secret_key = 'KGI;lu[/7ce=^if,e(:Pl`.$Xu8@ni&+L!OcuD?)xy:+E}/4k/K3B86{0eHqp]w'

if __name__ == '__main__':
  app.run(debug=True)

import main.views