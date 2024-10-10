from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Fatores de emissão (exemplo simples e expandidos)
EMISSION_FACTORS = {
    'energia': 0.233,  # CO2 por kWh
    'combustivel': 2.31,  # CO2 por litro de gasolina
    'transporte': 0.21,  # CO2 por km rodado
    'transporte_publico': 0.05  # CO2 por km de transporte público (exemplo)
}

# Função para calcular o crédito de carbono para indivíduos, empresas ou cidades
def calcular_pegada_carbono(dados, tipo_usuario):
    if tipo_usuario == 'individuo':
        # Cálculo para indivíduos
        consumo_energia = dados.get('energia', 0) * EMISSION_FACTORS['energia']
        consumo_combustivel = dados.get('combustivel', 0) * EMISSION_FACTORS['combustivel']
        distancia_transporte = dados.get('transporte', 0) * EMISSION_FACTORS['transporte']
        total_emissoes = consumo_energia + consumo_combustivel + distancia_transporte

    elif tipo_usuario == 'empresa':
        # Cálculo para empresas (escala maior)
        consumo_energia = dados.get('energia', 0) * 1000 * EMISSION_FACTORS['energia']  # Conversão para kWh
        consumo_combustivel = dados.get('combustivel', 0) * EMISSION_FACTORS['combustivel']
        total_emissoes = consumo_energia + consumo_combustivel

    elif tipo_usuario == 'cidade':
        # Cálculo para cidades
        consumo_energia = dados.get('energia', 0) * 1000 * EMISSION_FACTORS['energia']  # Conversão para kWh
        distancia_transporte_publico = dados.get('transporte_publico', 0) * EMISSION_FACTORS['transporte_publico']
        distancia_transporte_carro = dados.get('transporte_carro', 0) * EMISSION_FACTORS['transporte']
        total_emissoes = consumo_energia + distancia_transporte_publico + distancia_transporte_carro

    else:
        total_emissoes = 0  # Caso não seja um tipo válido

    return total_emissoes

# Rota principal para exibir o HTML
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/como-funciona')
def como_funciona():
    return render_template('como-funciona.html')

# Rota para processar o cálculo de carbono
@app.route('/calcular', methods=['POST'])
def calcular():
    dados = request.json
    tipo_usuario = dados.get('tipo_usuario', 'individuo')  # Assume 'individuo' se não informado
    total_emissoes = calcular_pegada_carbono(dados, tipo_usuario)
    return jsonify({'total_emissoes': total_emissoes})

if __name__ == '__main__':
    app.run(debug=True)

