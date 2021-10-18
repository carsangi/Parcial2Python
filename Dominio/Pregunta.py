class Pregunta:

    def __init__(self,id_pregunta,enunciado,opcion_a,opcion_b,opcion_c,opcion_d,respuesta,cod_categoria,dificultad):
        self.id_pregunta = id_pregunta
        self.enunciado = enunciado
        self.opcion_a = opcion_a
        self.opcion_b = opcion_b
        self.opcion_c = opcion_c
        self.opcion_d = opcion_d
        self.respuesta = respuesta
        self.cod_categoria = cod_categoria
        self.dificultad = dificultad

    def __str__(self):
        return f"{self.id_pregunta}--{self.enunciado}--{self.opcion_a}--{self.opcion_b}--{self.opcion_c}--{self.opcion_d}--{self.respuesta}--{self.cod_categoria}--{self.dificultad}"

    def __repr__(self):
        return f"\nCodigo: {self.id_pregunta}\nPregunta: {self.enunciado}\nOpcion A: {self.opcion_a}\nOpcion B: {self.opcion_b}\nOpcion C: {self.opcion_c}\nOpcion D: {self.opcion_d}\nRespuesta: {self.respuesta}\nCodigo Categoria: {self.cod_categoria}\nDificultad: {self.dificultad}"