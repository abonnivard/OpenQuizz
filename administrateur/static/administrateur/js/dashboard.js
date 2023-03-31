window.addEventListener('load', () => {

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }


    const boutonsuppS = document.getElementsByClassName('supp')

    function supprimerQuestion (element) {
        let q = document.getElementsByClassName('question')[element.id]
        q.style.display = 'none'
        const formData = new FormData()
        formData.append('numero', element.id)
        fetch("/suppression/", {
            method: 'post',
            body: formData,
            headers: {
              "X-CSRFToken": getCookie("csrftoken"),
            },
            credentials: 'same-origin',
        })
    }


    const arr = Array.from(boutonsuppS);
    arr.forEach(element => element.addEventListener('click', function() { supprimerQuestion(element); }))

    let bouttondown = document.getElementsByClassName('downarrow')
    let buttonup = document.getElementsByClassName("uparrow")
    function deploy(element) {
        document.getElementsByClassName('downarrow')[element.id].style.display = "none"
        document.getElementsByClassName('uparrow')[element.id].style.display = "flex"
        document.getElementsByClassName('partieinf')[element.id].style.display = "flex"
        document.getElementById(element.id+'quizz').style.height = "300px"
    }

    function deployoff(element) {
        document.getElementsByClassName('downarrow')[element.id].style.display = "flex"
        document.getElementsByClassName('uparrow')[element.id].style.display = "none"
        document.getElementsByClassName('partieinf')[element.id].style.display = "none"
        document.getElementById(element.id+'quizz').style.height = "70px"
    }

    const arrdeploy = Array.from(bouttondown)
    arrdeploy.forEach(element => element.addEventListener('click', function(){deploy(element); }))
    const arrdeployoff = Array.from(buttonup)
    arrdeployoff.forEach(element => element.addEventListener('click', function(){deployoff(element); }))





})


