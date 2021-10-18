import uuid

from Dominio.Inventario import Inventario
from Dominio.Pregunta import Pregunta
from Infraestructura.Persistencia import Persistencia

if __name__ == '__main__':
    saver = Persistencia()
    inventario = Inventario()
    id_pregunta = uuid.uuid1()
    enunciado = "¿Cual es la capital de Eslovenia?"
    opcion_a="Lisboa"
    opcion_b="Barcelona"
    opcion_c="Piran"
    opcion_d="Liubliana"
    respuesta="Liubliana"
    cod_categoria = 1
    dificultad = "Dificil"
    pre = Pregunta(id_pregunta,enunciado,opcion_a,opcion_b,opcion_c,opcion_d,respuesta,cod_categoria,dificultad);
    saver.save_json(pre);
