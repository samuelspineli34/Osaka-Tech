from dao.user_dao import UserDAO

class UserService:
    def __init__(self):
        self.dao = UserDAO()

    def get_all_users(self):
        try:
            users_dtos = self.dao.get_all_users()
            
            # Converts the list of DTO objects into a list of dictionaries (to become JSON)
            return [user.to_dict() for user in users_dtos]
            
        except Exception as e:
            print(f"Service Error: {e}")
            return [] # Returns an empty list in case of error
    
    def get_user_by_id(self, user_id):
        user_dto = self.dao.get_by_id(user_id)
        return user_dto.to_dict() if user_dto else None
        
    def create_user(self, data):
        self.dao.create(data['name'], data['email'], data['department'])

    def update_user(self, user_id, data):
        self.dao.update(user_id, data['name'], data['email'], data['department'])

    def delete_user(self, user_id):
        self.dao.delete(user_id)