const hamburger = document.querySelector(".hamburger");

const menu = document.querySelector(".menu-navegacion");

hamburger.addEventListener("click", ()=>{
    menu.classList.toggle("spread");
});

window.addEventListener("click", (event)=>{
    if(menu.classList.contains("spread") 
        && event.target !== menu 
        && event.target !== hamburger)
    {
       menu.classList.toggle("spread");
    } 
})