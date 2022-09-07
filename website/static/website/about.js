document.addEventListener('DOMContentLoaded',function(){
    //for the euanlimzx homepage
    document.querySelector('.bi-instagram').addEventListener('click',()=>instagram());
    document.querySelector('.bi-github').addEventListener('click',()=>github());
    document.querySelector('.bi-telegram').addEventListener('click',()=>telegram());

})

function telegram(){
    location.href="https://t.me/euanlim"
}

function instagram(){
    location.href="https://www.instagram.com/euanlim_/"
}

function github(){
    location.href="https://github.com/euanlimzx?tab=repositories"
}