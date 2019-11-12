from tools import get_data_from_csv, search_in_csv, last_row, create_user_in_csv

from flask_login import UserMixin


class User(UserMixin):
    """
    Clase que hereda de UserMixin para iniciar sesion y demas.
    """

    def __init__(self, *args):
        self.id = args[0]
        self.username = args[1]
        self.password = args[2]

    @staticmethod
    def get(id):
        """
        Metodo para obtener el usuario por id.
        """
        users = get_data_from_csv('files/users.csv')
        search_in_csv(users, 'id', id)
        return User(*search_in_csv(users, 'id', id))

    @staticmethod
    def get_by_username(name):
        users = get_data_from_csv('files/users.csv')
        user = search_in_csv(users, 'name', name)
        if not user:
            return None
        else:
            return User(*user)

    @staticmethod
    def last():
        """
        Metodo para obtener el ultimo usuario.
        """
        users = get_data_from_csv('files/users.csv')
        return User(*last_row(users))

    @classmethod
    def create(cls, username, password):
        """
        Metodo para crear un usuario.
        """
        last_user = cls.last()
        new_id = int(last_user.id) + 1
        user = '{},{},{}'.format(
            new_id, username, password
        )
        create_user_in_csv(user, 'files/users.csv')

        return User.get(new_id)
