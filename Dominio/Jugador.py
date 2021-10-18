class Jugador:

    def __init__(self,id_jugador,nombre,apellido,profesion,historial,password,*args):
        self.id_jugador = id_jugador
        self.nombre = nombre
        self.apellido = apellido
        self.profesion = profesion
        self.historial = historial
        self.password = password

    def __str__(self):
        return f"{self.id_jugador}--{self.nombre}--{self.apellido}--{self.profesion}--{self.historial}--{self.password}"

    def __repr__(self):
        return f"\nCedula: {self.id_jugador}\nNombre: {self.nombre}\nApellido: {self.apellido}\nProfesion: {self.profesion}" \
               f"\nHistorial: {self.historial}\nContraseña: {self.password}\n"