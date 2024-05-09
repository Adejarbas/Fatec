//1//

function calculo1(){
    x = Number(document.getElementById("valor1").value);
    y = Number(document.getElementById("valor2").value);

    calculo = (x + y)/2;

    document.getElementById("calculo").innerHTML = calculo;
}


//2//

function calculo2(){
    x = prompt("Insira o valor de X: ");
    y = prompt("Insira o valor de Y: ");
    
    resultado = Math.pow(x,y);


    console.log(`Resultado: ${resultado}`);
    alert(`Resultado: ${resultado}`);
}


//3//

function calcularMenorValor() {
    
    const valor1 = parseFloat(document.getElementById("valor1").value);
    const valor2 = parseFloat(document.getElementById("valor2").value);
    const valor3 = parseFloat(document.getElementById("valor3").value);

    
    const valores = [valor1, valor2, valor3];

    
    const menorValor = Math.min(...valores);

    
    document.getElementById("resultado").innerText = menorValor;
}


//4//
const X = [15, 25];


const Y = [12, 15, 23, 43];


console.log("Multiplicando cada elemento do array X por 5:");
for (let i = 0; i < X.length; i++) {
    const resultado = X[i] * 5;
    console.log(`${X[i]} * 5 = ${resultado}`);
}


//5//
function calcularMedia() {
    // Obtendo os valores das notas
    const nota1 = parseFloat(document.getElementById("nota1").value);
    const nota2 = parseFloat(document.getElementById("nota2").value);

    // Calculando a média ponderada
    const mediaPonderada = (nota1 * 0.3) + (nota2 * 0.7);

    // Exibindo o resultado da média ponderada na página HTML
    document.getElementById("resultado").innerText = mediaPonderada.toFixed(2);
}


//6//
function calcularSalario() {
    const horasTrabalhadas = parseFloat(document.getElementById("horasTrabalhadas").value); // Total de horas trabalhadas
    const valorHoraNormal = 10; // Valor da hora normal
    const horasNormais = 40; // Limite de horas normais
    const valorHoraExtra = 3 * valorHoraNormal; // Valor da hora extra (três vezes o valor da hora normal)
    const valorRefeicao = 1.5; // Valor do desconto por refeição

    let salarioBruto;
    let descontoRefeicao = 0;

    if (horasTrabalhadas <= horasNormais) {
        salarioBruto = horasTrabalhadas * valorHoraNormal;
    } else {
        const horasExtras = horasTrabalhadas - horasNormais;
        salarioBruto = (horasNormais * valorHoraNormal) + (horasExtras * valorHoraExtra);
    }

    // Calculando o desconto da refeição
    descontoRefeicao = valorRefeicao * Math.ceil(horasTrabalhadas / 8); // Uma refeição a cada 8 horas trabalhadas

    // Calculando o salário líquido
    const salarioLiquido = salarioBruto - descontoRefeicao;

    // Exibindo os resultados na página HTML
    document.getElementById("salarioBruto").textContent = salarioBruto.toFixed(2);
    document.getElementById("descontoRefeicao").textContent = descontoRefeicao.toFixed(2);
    document.getElementById("salarioLiquido").textContent = salarioLiquido.toFixed(2);
}


//7//
function gerarNumero() {
    // Gerando um número aleatório entre 1 e 100
    const numero = Math.floor(Math.random() * 100) + 1;

    // Exibindo o número gerado na página HTML
    document.getElementById("numeroGerado").textContent = numero;

    // Verificando se o número é par ou ímpar
    if (numero % 2 === 0) {
        document.getElementById("parOuImpar").textContent = "Par";
    } else {
        document.getElementById("parOuImpar").textContent = "Ímpar";
    }
}


//8//
function calcularTotal() {
    const valorProduto = parseFloat(document.getElementById("valorProduto").value);
    const quantidade = parseInt(document.getElementById("quantidade").value);
    const formaPagamento = document.querySelector('input[name="pagamento"]:checked').value;

    let totalPagar = valorProduto * quantidade;
    let desconto = 0;

    // Verificando a forma de pagamento e aplicando os descontos, se aplicável
    switch (formaPagamento) {
        case "debito":
            desconto = totalPagar * 0.05;
            break;
        case "pix":
            desconto = totalPagar * 0.10;
            break;
        case "credito":
            // Nenhum desconto para pagamento com cartão de crédito
            break;
    }

    // Aplicando desconto adicional se o total a pagar for igual ou superior a R$ 1000,00
    if (totalPagar >= 1000) {
        desconto += totalPagar * 0.10;
    }

    // Aplicando os descontos ao total a pagar
    totalPagar -= desconto;

    // Exibindo os resultados na página HTML
    document.getElementById("totalPagar").textContent = totalPagar.toFixed(2);
    document.getElementById("desconto").textContent = desconto.toFixed(2);
    document.getElementById("formaPagamento").textContent = formaPagamento;
}