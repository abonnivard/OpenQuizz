window.addEventListener('load', () => {

})

    let checkboxqcm = document.querySelector('.qcmchoice')

    function qcm () {
        if (checkboxqcm.checked) {
            let qcm = document.querySelector('.qcm')
            qcm.style.display = 'flex'
            let q = qcm.querySelectorAll('input[type=text]')
            for (let i = 0;i<2;i++){
            }

            let reponseqcm = document.querySelector('.reponseqcm')
            let qrep = reponseqcm.querySelector('select')

            let reponselongue = document.getElementsByName('reponselongue')[0]
            reponselongue.style.display = 'none'
        }
        else {
            let qcm = document.querySelector('.qcm')
            qcm.style.display = 'none'
            let q = qcm.querySelectorAll('input[type=text]')
            for (let i = 0;i<2;i++){
            }

            let reponseqcm = document.querySelector('.reponseqcm')
            let qrep = reponseqcm.querySelector('select')

            let reponselongue = document.getElementsByName('reponselongue')[0]
            reponselongue.style.display = 'flex'

        }
    }