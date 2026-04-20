from dao.ticket_dao import TicketDAO

class TicketService:
    def __init__(self):
        self.dao = TicketDAO()

    def get_all_tickets(self):
        try:
            # O Service filtra apenas os ativos se necessário, 
            # mas geralmente o DAO já faz isso.
            tickets_dto = self.dao.get_all()
            return [t.to_dict() for t in tickets_dto]
        except Exception as e:
            print(f"Service Error (Get All): {e}")
            return []

    def create_ticket(self, data):
        try:
            # Aqui você poderia validar se o user_id ainda existe e não está deletado
            self.dao.create(data)
        except Exception as e:
            print(f"Service Error (Create): {e}")

    def update_ticket(self, ticket_id, data):
        try:
            self.dao.update(ticket_id, data)
        except Exception as e:
            print(f"Service Error (Update): {e}")

    def delete_ticket(self, ticket_id):
        try:
            # Chamamos o Soft Delete no DAO
            self.dao.soft_delete(ticket_id)
        except Exception as e:
            print(f"Service Error (Delete): {e}")