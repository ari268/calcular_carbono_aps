document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('form-carbono');
    const tipoUsuarioSelect = document.getElementById('tipo_usuario');
    const campoCombustivel = document.getElementById('campo-combustivel');
    const campoTransporte = document.getElementById('campo-transporte');
    const campoTransportePublico = document.getElementById('campo-transporte-publico');
    const campoTransporteCarro = document.getElementById('campo-transporte-carro');
    const resultadoEmissoes = document.getElementById('resultado-emissoes');

    // Função para ajustar os campos visíveis com base no tipo de usuário
    function ajustarCampos() {
        const tipoUsuario = tipoUsuarioSelect.value;

        if (tipoUsuario === 'individuo') {
            campoCombustivel.style.display = 'block';
            campoTransporte.style.display = 'block';
            campoTransportePublico.style.display = 'none';
            campoTransporteCarro.style.display = 'none';
        } else if (tipoUsuario === 'empresa') {
            campoCombustivel.style.display = 'block';
            campoTransporte.style.display = 'none';
            campoTransportePublico.style.display = 'none';
            campoTransporteCarro.style.display = 'none';
        } else if (tipoUsuario === 'cidade') {
            campoCombustivel.style.display = 'none';
            campoTransporte.style.display = 'none';
            campoTransportePublico.style.display = 'block';
            campoTransporteCarro.style.display = 'block';
        }
    }

    // Chama ajustarCampos quando o tipo de usuário é alterado
    tipoUsuarioSelect.addEventListener('change', ajustarCampos);

    // Submissão do formulário via AJAX
    form.addEventListener('submit', function (e) {
        e.preventDefault();

        const dados = {
            tipo_usuario: tipoUsuarioSelect.value,
            energia: parseFloat(document.getElementById('energia').value) || 0,
            combustivel: parseFloat(document.getElementById('combustivel').value) || 0,
            transporte: parseFloat(document.getElementById('transporte').value) || 0,
            transporte_publico: parseFloat(document.getElementById('transporte_publico').value) || 0,
            transporte_carro: parseFloat(document.getElementById('transporte_carro').value) || 0
        };

        fetch('/calcular', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(dados)
        })
        .then(response => response.json())
        .then(data => {
            resultadoEmissoes.textContent = `${data.total_emissoes.toFixed(2)} kg de CO₂`;
        })
        .catch(error => {
            console.error('Erro ao calcular as emissões:', error);
            resultadoEmissoes.textContent = 'Erro ao calcular as emissões.';
        });
    });

    // Chama a função para definir o estado inicial dos campos
    ajustarCampos();
});
