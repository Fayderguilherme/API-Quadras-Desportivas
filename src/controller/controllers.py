# O seu 'C' - A lógica e as regras


from flask import jsonify
from model.models import db, Quadras, Inquilino, Reservas
from datetime import datetime

#Função para criar uma nova quadra
def criar_quadra(dados):
    name = dados.get('name')

    if not name:
        return {"message": "Falta o nome da quadra"}, 400

    nova_quadra = Quadras(name=name)
    db.session.add(nova_quadra)
    db.session.commit()
    return {"message": "Quadra registada com sucesso!"}, 201


#Função para criar um novo inquilino
def criar_inquilino(dados):
    name = dados.get('name')

    if not name:
        return {"message": "Falta o nome do inquilino"}, 400

    novo_inquilino = Inquilino(name=name)
    db.session.add(novo_inquilino)
    db.session.commit()
    return {"message": "Inquilino registado com sucesso!"}, 201

#função para fazer reserva
def criar_reservas(dados):
    id_inquilino = dados.get('inquilino_id')
    id_quadra = dados.get('quadras_id')
    data_reserva = dados.get('data')
    data_formatada = datetime.strptime(data_reserva, '%Y-%m-%d').date()
    horario_reserva = dados.get('horario')
    horario_formatado = datetime.strptime(horario_reserva, '%H:%M:%S').time()


    if not all([id_inquilino, id_quadra, data_reserva, horario_reserva]):
        return {"message": "Faltam dados para a reserva"}, 400

    ocupado = Reservas.query.filter_by(
        quadras_id=id_quadra,
        data=data_formatada,
        horario=horario_formatado
    ).first()

    if ocupado:
        return {"message": "Horário indisponível"}, 400

    criar_reservas = Reservas(
        inquilino_id=id_inquilino,
        quadras_id=id_quadra,
        data=data_formatada,
        horario=horario_formatado
    )
    db.session.add(criar_reservas)
    db.session.commit()
    return jsonify({'message': 'Agenda criada'}), 200


#Função para ver as reservas pelo id
def buscar_reservas(reserva_id):
    reservas = Reservas.query.get(reserva_id)
    if reservas:
        # 1. O controlador vai à base de dados procurar o inquilino específico
        dono = Inquilino.query.get(reservas.inquilino_id)
        
        return {
            "id": reservas.id,
            "data": str(reservas.data),
            "horario": str(reservas.horario),
            "name": dono.name # 2. Agora o Python já sabe extrair o nome!
        }, 200
        
    return {"message": "Reserva não encontrada"}, 404

#Função para ver todas reservas 
def buscar_lista():
    lista = []

    for reserva in Reservas.query.all():
        dono = Inquilino.query.get(reserva.inquilino_id)
        lista.append({
            "id": reserva.id,
            "data": str(reserva.data),
            "horario": str(reserva.horario),
            "name": dono.name if dono else None
        })

    return {"reservas": lista}, 200


#Função para deletar reservas 
def deletar_reservas(reserva_id):
    reservas = Reservas.query.get(reserva_id)
    if reservas:
        db.session.delete(reservas)
        db.session.commit()
        return {"message": "Reserva Cancelada"}, 200
    return {"message": "Reserva não encontrada"}, 404
