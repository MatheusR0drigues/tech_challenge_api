from flask import Blueprint, jsonify
from data_extractor import extrair_dados

api = Blueprint('api', __name__)

valid_anos = set(range(1970, 2023))  # 1970 a 2022
valid_opcoes = {
    'opt_02': None,  # Produção não tem subopção
    'opt_03': {'subopt_01', 'subopt_02', 'subopt_03', 'subopt_04'},  # Processamento
    'opt_04': None,  # Comercialização não tem subopção
    'opt_05': {'subopt_01', 'subopt_02', 'subopt_03', 'subopt_04', 'subopt_05'},  # Importação
    'opt_06': {'subopt_01', 'subopt_02', 'subopt_03', 'subopt_04'}  # Exportação
}

@api.route('/dados/<ano>/<opcao>', defaults={'subopcao': None}, methods=['GET'])
@api.route('/dados/<ano>/<opcao>/<subopcao>', methods=['GET'])
def get_dados(ano, opcao, subopcao):
    try:
        if int(ano) not in valid_anos:
            return jsonify({"error": f"Ano '{ano}' inválido. Escolha entre 1970 e 2022."}), 400
        if opcao not in valid_opcoes:
            return jsonify({"error": f"Opção '{opcao}' inválida."}), 400
        if valid_opcoes[opcao] is not None and (subopcao is None or subopcao not in valid_opcoes[opcao]):
            if subopcao is None:
                return jsonify({"error": f"A opção '{opcao}' requer uma subopção."}), 400
            else:
                return jsonify({"error": f"Subopção '{subopcao}' inválida para a opção '{opcao}'."}), 400

        dados = extrair_dados(ano, opcao, subopcao)
        if dados:
            return jsonify(dados)
        else:
            return jsonify({"message": "Nenhum dado encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
