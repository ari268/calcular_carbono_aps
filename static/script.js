document.getElementById('form-carbono').addEventListener('submit', function(event) {
    event.preventDefault();  // Evitar o comportamento padrão de envio de formulário

    // Coletar dados do formulário
    let dados = {
        energia: parseFloat(document.getElementById('energia').value),
        combustivel: parseFloat(document.getElementById('combustivel').value),
        transporte: parseFloat(document.getElementById('transporte').value)
    };

    // Enviar dados para o servidor Flask via POST
    fetch('/calcular', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dados)
    })
    .then(response => response.json())
    .then(data => {
        // Exibir o resultado no HTML
        document.getElementById('resultado-emissoes').innerText = data.total_emissoes.toFixed(2) + ' kg de CO2';
    })
    .catch(error => console.error('Erro:', error));
});
