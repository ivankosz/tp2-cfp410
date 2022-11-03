import random

class Sorteo():

    orden = 0

    def __init__(self) -> None:
        self.sorteo_index= list()
        self.copia = list()

    def set_participante (self, apellido, nombre, dni):
        self.participante = dict()
        Sorteo.orden+=1
        self.participante["ORDEN"]= Sorteo.orden
        self.participante["APELLIDO"]= apellido
        self.participante["NOMBRE"]= nombre
        self.participante["DNI"]= dni
        self.sorteo_index.append(self.participante)
        self.copia = self.sorteo_index.copy()

        return self.participante


    def eliminar_participante (self, dni):
        for dict in self.sorteo_index:
            if dict["DNI"] == dni:
                self.sorteo_index.remove(dict)
        self.copia = self.sorteo_index.copy()

    def get_inscritos (self):
        return self.sorteo_index

    def get_participante (self, dni):
        for dict in self.sorteo_index:
            if dict["DNI"] == dni:
                return dict
    
    def get_inscripciones_copy (self):
        return self.copia

    def finalizar_inscripcion (self):
        pass

    def borrar_inscripciones (self):
        self.sorteo_index.clear()

    def realizar_sorteo (self, vacantes_disponibles):
        self.ganadores= dict()
        for vac in range(vacantes_disponibles):
            self.ganador_sorteo =random.choice(self.sorteo_index)
            self.sorteo_index.remove(self.ganador_sorteo)
            self.ganadores[vac+1]=self.ganador_sorteo
        self.copia = self.sorteo_index.copy()
        return self.ganadores


if __name__=="__main__":
    inscripcion = Sorteo()

    inscripcion.set_participante("KOSZAREK","IVAN","34727040")

    inscripcion.set_participante("PALMA","LAUTARO", "42827077")

    inscripcion.set_participante("PEREZ VALOBRA","SANTIAGO", "01011001")

    #print(inscripcion.get_participante("34727040"))

    #print(inscripcion.get_inscripciones_copy())

    print(inscripcion.realizar_sorteo(2))

    print(inscripcion.get_inscritos())

