class UserDTO:
    def __init__(self, id, name, email, department):
        self.id = str(id) if id else None # Converte objeto UUID para string
        self.name = name
        self.email = email
        self.department = department

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "department": self.department
        }