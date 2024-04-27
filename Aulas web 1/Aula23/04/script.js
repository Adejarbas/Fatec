let adicionais=0;
let engrega = 0;

function totalpagar(){

    let total=0;
    calcularAdicionais()
    total= adicionais + calcularEntrega;
}

function CalcularAdicionais(){
    adicionais=0;
    let selecionados=document.querySelectorAll("input[name='adicionais']")
    
    let qtd = selecionados.length;
    for (i=0; i<qtd; i++)

    {  
        if (selecionados[i].checked)
        {
            adicionais += Number(selecionados[i].value);
        }
    }
}

function calcularEntrega(){


}