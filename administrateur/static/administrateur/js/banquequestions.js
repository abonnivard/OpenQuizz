window.addEventListener('load', () => {

    let boutonOn = document.querySelector('.bouton1')
    let boutonOff = document.querySelector('.boutoncroix')


    function afficher() {
        document.querySelector('.contact_div').style.display = "flex";
        document.querySelector('.popup_question').style.display = "flex";
        document.querySelector('.all').style.filter = 'blur(3px)'
        document.querySelector('.titleup').style.filter = "blur(4px)"
    }

    function supprimer() {
        document.querySelector('.contact_div').style.display = "none";
        document.querySelector('.popup_question').style.display = "none";
        document.querySelector('.all').style.filter = 'blur(0px)'
        document.querySelector('.titleup').style.filter = "blur(0px)"
    }

    boutonOn.addEventListener('click', afficher)
    boutonOff.addEventListener('click', supprimer)



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

    async function supprimerQuestion (element) {
        let q = document.getElementById(element.id+'question')
        q.style.display = 'none'
        const formData = new FormData()
        formData.append('numero', element.id)
        const response = await fetch("/suppression-question/", {
            method: 'post',
            body: formData,
            headers: {
              "X-CSRFToken": getCookie("csrftoken"),
            },
            credentials: 'same-origin',
        })

        if (response.status === 200){
            return window.location.replace("/banque-question")
        }
    }


    const arr = Array.from(boutonsuppS);
    arr.forEach(element => element.addEventListener('click', function() { supprimerQuestion(element); }))
})

    let checkboxqcm = document.querySelector('.qcmchoice')

    function qcm () {
        if (checkboxqcm.checked) {
            let qcm = document.querySelector('.qcm')
            qcm.style.display = 'flex'
            let q = qcm.querySelectorAll('input[type=text]')
            for (let i = 0;i<2;i++){
                q[i].setAttribute('required', '')
            }

            let reponseqcm = document.querySelector('.reponseqcm')
            let qrep = reponseqcm.querySelector('select')
            qrep.setAttribute('required', '')

            let reponselongue = document.getElementsByName('reponselongue')[0]
            reponselongue.style.display = 'none'
            reponselongue.removeAttribute('required')
        }
        else {
            let qcm = document.querySelector('.qcm')
            qcm.style.display = 'none'
            let q = qcm.querySelectorAll('input[type=text]')
            for (let i = 0;i<2;i++){
                q[i].removeAttribute('required')
            }

            let reponseqcm = document.querySelector('.reponseqcm')
            let qrep = reponseqcm.querySelector('select')
            qrep.removeAttribute('required')

            let reponselongue = document.getElementsByName('reponselongue')[0]
            reponselongue.style.display = 'flex'
            reponselongue.setAttribute('required', '')

        }
    }