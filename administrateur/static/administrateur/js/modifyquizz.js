


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




