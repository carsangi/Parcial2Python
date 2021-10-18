from Dominio.Categoria import Categoria
from Dominio.Pregunta import Pregunta
from Dominio.Jugador import Jugador


class Inventario:

    def __init__(self):
        self.jugadores = []
        self.categorias = []
        self.preguntas = []

    def agregar_objeto(self, objeto):
        if type(objeto) == Jugador:
            if len(list(self.buscarJugadorDocumento(objeto.id_jugador,objeto.password))) == 0:
                self.jugadores.append(objeto)
            else:
                print('Jugador ya existe')
                raise Exception('Jugador ya existe')

        if type(objeto) == Categoria:
            if len(list(self.buscarCategoriaCodigo(objeto.codigo))) == 0:
                self.categorias.append(objeto)
            else:
                print('Categoria repetida')
                raise Exception('Categoria repetida')

        if type(objeto) == Pregunta:
            if len(list(self.buscarPreguntaId(objeto.id_pregunta))) == 0:
                self.preguntas.append(objeto)
            else:
                print('Pregunta ya existe')
                raise Exception('Pregunta ya existe')

    def buscarJugadorDocumento(self,id_jugador,password):
        for i in self.jugadores:
            if i.id_jugador == id_jugador and i.password == password:
                yield i

    def buscarCategoriaCodigo(self,codigo):
        for i in self.categorias:
            if i.codigo == codigo:
                yield i

    def buscarPreguntaId(self,id_pregunta):
        for i in self.preguntas:
            if i.id_pregunta == id_pregunta:
                yield i

    def eliminarListas(self):
        self.jugadores.clear()
        self.categorias.clear()
        self.preguntas.clear()
