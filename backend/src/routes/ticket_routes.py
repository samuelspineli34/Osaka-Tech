from flask import Blueprint, jsonify, request
from services.ticket_service import TicketService

ticket_bp = Blueprint('ticket', __name__)
ticket_service = TicketService()

@ticket_bp.route('/ticket', methods=['GET'])
def get_all():
    return jsonify(ticket_service.get_all_tickets()), 200

@ticket_bp.route('/ticket', methods=['POST'])
def create():
    # O JSON do front chega aqui e vai para o Service
    ticket_service.create_ticket(request.json)
    return jsonify({"message": "Created"}), 201

@ticket_bp.route('/ticket/<uuid:ticket_id>', methods=['PUT'])
def update(ticket_id):
    ticket_service.update_ticket(str(ticket_id), request.json)
    return jsonify({"message": "Updated"}), 200

@ticket_bp.route('/ticket/<uuid:ticket_id>', methods=['DELETE'])
def delete(ticket_id):
    # O Service vai chamar o soft_delete no DAO
    ticket_service.delete_ticket(str(ticket_id))
    return jsonify({"message": "Deleted (Soft Delete)"}), 200