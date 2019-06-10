from flask import Flask, render_template, request, jsonify
from pusher import Pusher
from util.database.querys import DBQuerys
import json

app = Flask(__name__)

pusher = Pusher(
  app_id='619047',
  key='9eaefb7dfbd60539d7dc',
  secret='931dacc8a112a6aa14f5',
  cluster='us2',
  ssl=True
)


@app.route('/')
def index():

    __querys = DBQuerys()

    return render_template('index.html',
                           count=__querys.contar_tipo_repositorios(),
                           total_repos=__querys.contar_all_repos())


if __name__ == '__main__':
    app.run(debug=True)