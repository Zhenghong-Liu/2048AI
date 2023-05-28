from flask import Flask, render_template
from flask_socketio import SocketIO, send
from GameEnv import Game2048
from mcts import MCTS
from mcts import select_one_dir_with_model

import time

app = Flask(__name__)
socketio = SocketIO(app)


@socketio.on('message')
def handle_message(data):
    global game
    global mcts

    # print("len of mcts.node_dict:",len(mcts.node_dict))
    if data['data'] == "START":
        print("Connect")
    if len(data['data']) == 16:
        start = time.time()
        #将1x16的list数组转换为4x4的矩阵
        matrix = []
        for i in range(4):
            matrix.append(data['data'][i * 4:i * 4 + 4])
        game.reset(matrix)
        # game.display()

        action = select_one_dir_with_model(mcts,game,False)
        print("AI推荐的action:",action)
        print("推荐用时：",time.time()-start)
        send(action)
    if data['restart'] == "True":
        # print("Restart")
        game = Game2048()
        mcts.reset()



@app.route("/")
def main_page():
    return render_template('index.html')


if __name__ == '__main__':
    game = Game2048()
    mcts = MCTS()
    mcts.ucb_debug = False
    mcts.predict_debug = False
    mcts.search_debug = False
    mcts.search_n = 100
    socketio.run(app, "0.0.0.0", 8000, allow_unsafe_werkzeug=True)
