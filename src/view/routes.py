from flask import Blueprint, request, jsonify
from controller.controllers import criar_quadra, criar_inquilino, criar_reservas, buscar_reservas, buscar_lista, deletar_reservas
rotas = Blueprint('rotas', __name__)

#Rota para criar a quadra
@rotas.route('/quadras', methods=['POST'])
def add_quadra():
    dados = request.json
    resposta = criar_quadra(dados)
    return resposta

#rota para criar inquilino
@rotas.route('/inquilino', methods=['POST'])
def add_inquilino():
    dados = request.json
    resposta = criar_inquilino(dados)
    return resposta

#rota para fazer a reserva da quadra
@rotas.route('/reservas', methods=['POST'])
def add_reserva():
    dados = request.json
    resposta = criar_reservas(dados)
    return resposta

#rota para listar todas as quadras
@rotas.route('/buscar/<int:id>', methods=['GET'])
def get_reserva(id): # Nome diferente para não confundir com o controller!
    resposta = buscar_reservas(id) # Passamos o ID diretamente, sem request.json
    return resposta

#rota para listar todos
@rotas.route('/lista', methods=['GET'])
def listar_todas():
    resposta = buscar_lista() # 1. Chama a função que criaste
    return resposta           # 2. TEM de ter este return para o Postman ver os dados!

#rota para apagar reserva
# A URL foi ajustada para '/cancelar' para bater certo com o teu Postman
@rotas.route('/cancelar/<int:id>', methods=['DELETE'])
def rota_cancelar_reserva(id): # NOME DIFERENTE para não confundir com o controller!
    resposta = deletar_reservas(id) # Aqui chamamos o controller em segurança
    return resposta