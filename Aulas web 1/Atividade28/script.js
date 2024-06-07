document.getElementById("pesquisaCep").addEventListener ('click', async function PesquisarCEP(){
let cep = document.getElementById('CEP').value

const apiViaCep = `https://viacep.com.br/ws/'+CEP+/json/`

const resCep = await fetch(apiViaCep)

const data = await resCep.json()

if (data.erro == true)
    alert("CEP Invalido")
else

document.getElementById("Rua").value = `${data.logradouro} ${data.bairro} ${data.localidade} ${data.uf}`
})
