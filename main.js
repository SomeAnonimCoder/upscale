function send() {

    form = document.getElementById("input_img")
    res = document.getElementById("result")

    file = form.files[0]
    var data = new FormData();
    data.append('file', file);

    var request = new XMLHttpRequest();
    request.open('post', '/cgi-bin/upscale.py');

    request.addEventListener('load', function(e) {
        res.src="data/"+request.response+"_res.png"
    });

    request.send(data);
    res.hidden=0
}

