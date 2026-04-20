import psycopg2
from config.config import Config
from dto.ticket_dto import TicketDTO
from datetime import datetime

class TicketDAO:
    def get_connection(self):
        return psycopg2.connect(**Config.get_db_config(), application_name='ServiceDesk', client_encoding='utf8')

    def get_all(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        # IMPORTANTE: Filtrar apenas os que NÃO foram deletados
        query = """
            SELECT t.id, t.title, t.description, t.status, t.priority, t.user_id, u.name, t.created_at 
            FROM tickets t 
            JOIN users u ON t.user_id = u.id 
            WHERE t.deleted_at IS NULL 
            ORDER BY t.created_at DESC
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        tickets = [TicketDTO(*row) for row in rows]
        cursor.close()
        conn.close()
        return tickets

    def create(self, data):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tickets (title, description, priority, user_id) VALUES (%s, %s, %s, %s)",
            (data['title'], data['description'], data['priority'], data['user_id'])
        )
        conn.commit()
        cursor.close()
        conn.close()

    def update(self, ticket_id, data):
        conn = self.get_connection()
        cursor = conn.cursor()
        query = """
            UPDATE tickets 
            SET title=%s, description=%s, status=%s, priority=%s, user_id=%s, updated_at=NOW() 
            WHERE id=%s AND deleted_at IS NULL
        """
        cursor.execute(query, (data['title'], data['description'], data['status'], data['priority'], data['user_id'], ticket_id))
        conn.commit()
        cursor.close()
        conn.close()

    def soft_delete(self, ticket_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        # Não removemos a linha, apenas carimbamos a data de deleção
        cursor.execute("UPDATE tickets SET deleted_at = NOW() WHERE id = %s", (ticket_id,))
        conn.commit()
        cursor.close()
        conn.close()