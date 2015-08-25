var socket;
var id;
var str_temp;
var temp;

if (!window.WebSocket) {
    window.WebSocket = window.MozWebSocket;
}

// Javascript Websocket Client
if (window.WebSocket) {
    socket = new WebSocket("ws://"+window.location.hostname
			   +":" + window.location.port + "/websocket2");

    socket.onmessage = function(event) {
	str_temp = event.data;
	temp = eval(str_temp)
	for (var i=0;i<temp[1].length;i++)
	{
	    document.getElementById(temp[0][i][0]).innerHTML=temp[1][i]['name'];
	    document.getElementById(temp[0][i][1]).innerHTML=temp[1][i]['value'];
	    document.getElementById(temp[0][i][2]).innerHTML=temp[1][i]['unit'];
	}
	document.getElementById('state_name').innerHTML=temp[2]['name'];
	document.getElementById('state_value').innerHTML=temp[2]['value'];
	document.getElementById('alarms_name').innerHTML=temp[3]['name'];
        document.getElementById('alarms_value').innerHTML=temp[3]['value'];
    };

    socket.onopen = function(event) {
	tip();
	id=window.setInterval(tip,5000);
    };

    socket.onclose = function(event) {
	        //取消定时
	window.clearInterval(id);
    };

}
else {
    alert("Your browser does not support Web Socket.");
}
//dingshi hanshu
function tip(){
    send('lai, gei wo shu ju !')
}
// Send Websocket data
function send(message) {
    if (!window.WebSocket) { return; }
    if (socket.readyState == WebSocket.OPEN) {
	socket.send(message);
    } else {
	alert("The socket is not open.");
    }
}
