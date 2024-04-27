let lampada = document.getElementById("lampada");

function Ligar(){
    lampada.setAttribute("src", "luzLigada.gif")


}

function Desligar(){
    lampada.setAttribute("src", "luzDesligada.gif")

    
}

function Sumir (){
    //lampada.style.display = "none";
    lampada.hidden = true;

}

function Aparecer(){
//lampada.style.display = "block";
lampada.hidden = false;


}

function Piscar(){
    if (lampada.getAttribute("src") ==  "luzLigada.gif")
          lampada.setAttribute("src", "luzDesligada.gif");
          
    else  if (lampada.getAttribute("src") == "luzDesligada.gif")
          lampada.setAttribute("src", "luzLigada.gif");
          
}

function Magica(){
   setInterval(Piscar, 1000)

}