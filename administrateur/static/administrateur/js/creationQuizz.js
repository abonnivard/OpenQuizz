

    let timerOn = document.querySelector('.timechoice')

    function displaychangetime (){
        if (timerOn.checked){
            document.querySelector('.selecttime').style.display = 'flex'
        }else{
            document.querySelector('.selecttime').style.display = 'none'
        }

    }


    let listequestionsd = document.getElementsByClassName('questiond')
    let listequestionsg = document.getElementsByClassName('questiong')

    function changerDtoG (element, rang) {
        element.style.display = "none"
        arrg[rang].style.display = 'flex'
    }

    function changerGtoD (element, rang) {
        element.style.display = "none"
        arrd[rang].style.display = 'flex'
    }

    const arrd = Array.from(listequestionsd)
    const arrg = Array.from(listequestionsg)


    for (let i = 0;i<arrd.length;i++){
        arrd[i].addEventListener('click', function() { changerDtoG(arrd[i],i); })
    }

    for (let i = 0;i<arrg.length;i++){
        arrg[i].addEventListener('click', function() { changerGtoD(arrg[i],i); })
    }



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

    let enregistrer = document.querySelector("#submit")

    async function sauvegarder() {
        const formData = new FormData()
        let liste = []
        for(let i = 0;i<arrg.length; i++){
            if (arrg[i].style.display === 'flex'){
                liste.push(i)
            }
        }
        if (timerOn.checked){
            let timer = document.querySelector('.timer')
            formData.append('timer', timer.value.toString())
        }else {
            formData.append('timer', "0")
        }
        let classement = document.querySelector("#classement")
        if (classement.checked){
            formData.append('classementdisplay', "true")
        }else{
            formData.append('classementdisplay', "false")
        }

        let stocker = document.querySelector("#stocker")
        if (stocker.checked){
            formData.append('stocker', "true")
        }else{
            formData.append('stocker', "false")
        }

        let choix = document.querySelector('#choix1')
        if (choix.checked){
            formData.append('mode', 'cours')
        }else {
            formData.append('mode', 'examen')
        }


        let name = document.querySelector("#namequizz").value
        formData.append('name', name)

        formData.append('liste', liste)
        const response = await fetch("/enregistrement/", {
            method: 'post',
            body: formData,
            headers: {
              "X-CSRFToken": getCookie("csrftoken"),
            },
            credentials: 'same-origin',
        })
        if (response.status === 200) {
            return window.location.href = "/dashboard/"
        }
    }


    enregistrer.addEventListener('click', sauvegarder)


