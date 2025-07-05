import json
import os  #biblioteca QUe serve para lidar com operações de sistema, como descobrir onde estão os arquivos e caminhos validos entre pastas
import hashlib   #Usei hash para guardar a senha de forma segura, evitando salvar a senha real e protegendo os dados do usuário

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class User:
    def __init__(self, id, name, email, birthdate, password_hash=None):
        self.id = id
        self.name = name
        self.email = email
        self.birthdate = birthdate
        self.password_hash = password_hash  # Armazenar a senha como hash


    def __repr__(self):
        return (f"User(id={self.id}, name='{self.name}', email='{self.email}', "
                f"birthdate='{self.birthdate}')")


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'birthdate': self.birthdate,
            'password_hash': self.password_hash,
            'role': getattr(self, 'role', 'comum')
        }


    @classmethod
    def from_dict(cls, data):
        role = data.get('role', 'comum')
        if role == 'admin':
            return Administrador(
                id=data['id'],
                name=data['name'],
                email=data['email'],
                birthdate=data['birthdate'],
                password_hash=data.get('password_hash')
                )
        else:
            return UsuarioComum(
                id=data['id'],
                name=data['name'],
                email=data['email'],
                birthdate=data['birthdate'],
                password_hash=data.get('password_hash')
            )

    def set_password(self, plain_password):
        # Cria o hash da senha e salva
        self.password_hash = hashlib.sha256(plain_password.encode()).hexdigest()

    def check_password(self, plain_password):
        # Confere se o hash bate com o armazenado
        if not self.password_hash:
            return False
        return self.password_hash == hashlib.sha256(plain_password.encode()).hexdigest()

class UsuarioComum(User):
    def __init__(self, id, name, email, birthdate, password_hash=None, role=None):
        super().__init__(id, name, email, birthdate, password_hash)
        self.role = 'comum'


class Administrador(User):
    def __init__(self, id, name, email, birthdate, password_hash=None, role=None):
        super().__init__(id, name, email, birthdate, password_hash)
        self.role = 'admin'

class UserModel:
    FILE_PATH = os.path.join(DATA_DIR, 'users.json')

    def __init__(self):
        self.users = self._load()


    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [User.from_dict(item) for item in data]


    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([u.to_dict() for u in self.users], f, indent=4, ensure_ascii=False)


    def get_all(self):
        return self.users


    def get_by_id(self, user_id: int):
        return next((u for u in self.users if u.id == user_id), None)

    def get_by_email(self, email: str):
        return next((u for u in self.users if u.email == email), None)


    def add_user(self, user: User):
        self.users.append(user)
        self._save()


    def update_user(self, updated_user: User):
        for i, user in enumerate(self.users):
            if user.id == updated_user.id:
                self.users[i] = updated_user
                self._save()
                break


    def delete_user(self, user_id: int):
        self.users = [u for u in self.users if u.id != user_id]