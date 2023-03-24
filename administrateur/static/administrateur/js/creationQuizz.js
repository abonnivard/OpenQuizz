

    let timerOn = document.querySelector('.timechoice')

    function displaychangetime (){
        if (timerOn.checked){
            document.querySelector('.selecttime').style.display = 'flex'
        }else{
            document.querySelector('.selecttime').style.display = 'none'
        }

    }

