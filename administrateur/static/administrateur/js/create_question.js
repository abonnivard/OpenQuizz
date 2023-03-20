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

    function supprimerQuestion (element) {
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
})

    let checkboxqcm = document.querySelector('.qcmchoice')

    function qcm () {
        if (checkboxqcm.checked) {
            document.querySelector('.qcm').style.display = 'flex'
            document.getElementsByName('reponselongue')[0].style.display = 'none'
        }
        else {
            document.querySelector('.qcm').style.display = 'none'
            document.getElementsByName('reponselongue')[0].style.display = 'flex'

        }
    }

