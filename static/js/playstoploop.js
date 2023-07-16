$(document).ready(function () {
    var playstoploopChannel = pusher.subscribe('playstoploop');
    var toAppend = document.createElement('campoplaystoploop')
    playstoploopChannel.bind('send', function(data) {
        document.getElementById('playstoploop').appendChild(toAppend)
        toAppend.innerHTML ='<img src="'+
                                `${data.playstoploop}`+
                            '">'
      });
});