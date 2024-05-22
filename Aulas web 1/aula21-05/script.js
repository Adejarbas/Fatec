

let cep = document.querySelector("input[name='cep']");

let api = "https://viacep.com.br/ws/json/";

let botao = document.getElementById("buscar");

botao.addEventListener ('click', async function buscarCep(){

api = `https://viacep.com.br/ws/${cep.value}/json/`;
let dados = await fetch(api);
let dadosformat = await dados.json();

alert (dadosformat.localidade);

document.getElementById('elemento').setAttribute('src',`https://source.unsplash.com/1600x900/?${dadosformat.localidade}`);

}) //botao.addEventListener("click", buscarCep());