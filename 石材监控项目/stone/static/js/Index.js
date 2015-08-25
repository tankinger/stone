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
			   +":" + window.location.port + "/websocket1");

    socket.onmessage = function(event) {
	str_temp = event.data;
	//temp = str_temp.split(' ')
	temp = eval(str_temp)
	//设备数据
	
	for (var i=0;i<temp[0].length;i++)
        {
            for (var j=0;j<temp[0][i]['data'].length;j++)
            {

                document.getElementById(temp[0][i]['data'][j][0]).innerHTML=temp[1][i][j]['name'];
                document.getElementById(temp[0][i]['data'][j][1]).innerHTML=temp[1][i][j]['value'];
                document.getElementById(temp[0][i]['data'][j][2]).innerHTML=temp[1][i][j]['unit'];

            }

	    document.getElementById(temp[0][i]['dev_name']).innerHTML=temp[3][i];

	    //报警数据
            if (temp[2][i]['value']=="报警")
            {
		document.getElementById(temp[0][i]['dev_id']).style.border = "2px solid #FF0000";
            }
            else if(temp[2][i]['value']=="运行")
            {
		document.getElementById(temp[0][i]['dev_id']).style.border = "2px solid #00CD00";
            }
            else if(temp[2][i]['value']=="停机")
            {
		document.getElementById(temp[0][i]['dev_id']).style.border = "2px solid #5B5B5B";
            }
            else if(temp[2][i]['value']=="通信异常")
            {
		document.getElementById(temp[0][i]['dev_id']).style.border = "2px solid #FFD306";
            }
        }
			
	

	/*//报警数据
	if (temp[2]['state']['value']=="报警")
	{
	    document.getElementById("bjx0001b").style.border = "2px solid #FF0000";
	}
	else if(temp[2]['state']['value']=="运行")
	{
	    document.getElementById("bjx0001b").style.border = "2px solid #00CD00";
	}
	else if(temp[2]['state']['value']=="停机")
	{
	    document.getElementById("bjx0001b").style.border = "2px solid #5B5B5B";
	}
	else if(temp[2]['state']['value']=="通信异常")
	{
	    document.getElementById("bjx0001b").style.border = "2px solid #FFD306";
	}*/
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
