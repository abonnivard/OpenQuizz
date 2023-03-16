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