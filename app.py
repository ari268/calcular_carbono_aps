from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Fatores de emissão (exemplo simples)
EMISSION_FACTORS = {
    'energia': 0.233,  # CO2 por kWh
    'combustivel': 2.31,  # CO2 por litro de gasolina
    'transporte': 0.21  # CO2 por km rodado
}

# Função para calcular o crédito de carbono
def calcular_pegada_carbono(dados):
    consumo_energia = dados['energia'] * EMISSION_FACTORS['energia']
    consumo_combustivel = dados['combustivel'] * EMISSION_FACTORS['combustivel']
    distancia_transporte = dados['transporte'] * EMISSION_FACTORS['transporte']

    total_emissoes = consumo_energia + consumo_combustivel + distancia_transporte
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
    total_emissoes = calcular_pegada_carbono(dados)
    return jsonify({'total_emissoes': total_emissoes})

if __name__ == '__main__':
    app.run(debug=True)
