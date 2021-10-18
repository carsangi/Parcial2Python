
import sqlite3
import jsonpickle
from Dominio.Jugador import Jugador
from Dominio.Categoria import Categoria
from Dominio.Pregunta import Pregunta


class Persistencia():

    def connect(self):
        self.con = sqlite3.connect("qqsm.db")
        self.__crearTablaJugador()

    def __crearTablaJugador(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE PLAYER(id_jugador text primary key,nombre text, apellido text," \
                    " profesion text, historial text, password text) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_bd(self,objeto):
        cursor = self.con.cursor()

        if isinstance(objeto,Jugador):
            query = "insert into PLAYER(id_jugador ,nombre, apellido ," \
                    "profesion,historial,password ) values(" \
                    f" ?,?,?,?,?,?)"
            cursor.execute(query, (str(objeto.id_jugador), objeto.nombre, objeto.apellido,
                                   objeto.profesion, objeto.historial,objeto.password))
        self.con.commit()

    @classmethod
    def save_json(cls, objeto):
        if isinstance(objeto,Categoria):
            text_open = open("../Files/" + str(objeto.codigo) +"_"+str(objeto.categoria) +'.json', mode='w')
            json_gui = jsonpickle.encode(objeto)
            text_open.write(json_gui)
            text_open.close()

        if isinstance(objeto,Pregunta):
            text_open = open("../Files/" + str(objeto.id_pregunta) +"_"+str(objeto.dificultad) +'.json', mode='w')
            json_gui = jsonpickle.encode(objeto)
            text_open.write(json_gui)
            text_open.close()

        if isinstance(objeto,Jugador):
            text_open = open("Files/" + str(objeto.id_jugador) + '.json', mode='w')
            json_gui = jsonpickle.encode(objeto)
            text_open.write(json_gui)
            text_open.close()

    @classmethod
    def load_json(cls, file_name):
        text_open = open("Files/" + file_name, mode='r')
        json_gui = text_open.readline()
        objeto = jsonpickle.decode(json_gui)
        text_open.close()
        return objeto