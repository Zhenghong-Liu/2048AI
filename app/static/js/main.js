on(window, 'load', function () {

    //构建io对象
//    var socket = io();

    var view = new View();
    var game = new Game();
    game.init(view);
    event(game);


    var key2dir = {
        "a": 0,
        "w": 1,
        "d": 2,
        "s": 3,
    }

    var AIdir = null;

    //获取AIplayer的移动方向
    game.socket.on('message', function (message) {
        if (typeof message === 'string') {
            console.log("收到AIplayer的移动方向：" + message);
            AIdir = key2dir[message];
            if(game.AIplayer){
                game.move(AIdir);
            }
        }
    });


});