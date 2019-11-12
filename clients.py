class Client():
    """
    Clase para inicializar un objeto
    con la informacion de los clientes.
    """

    CLIENT = {
        'name': 0,
        'age': 1,
        'address': 2,
        'country': 3,
        'dni': 4,
        'entry_date': 5,
        'email': 6,
        'job': 7
    }

    def __init__(self, *args):
        self.name = args[self.CLIENT['name']]
        self.age = args[self.CLIENT['age']]
        self.address = args[self.CLIENT['address']]
        self.country = args[self.CLIENT['country']]
        self.dni = args[self.CLIENT['dni']]
        self.entry_date = args[self.CLIENT['entry_date']]
        self.email = args[self.CLIENT['email']]
        self.job = args[self.CLIENT['job']]
