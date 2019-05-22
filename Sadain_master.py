##Descripcion del programa
"""
Desarrollado por Luis Andrés Murcia
UNAD - CEAD Bogotá JAG - Mayo 2019
"""

"""
Sistema experto que ayuda al diagnostico de enfermedades autoinmunes como:

1 - Lupus Eritematoso Sistémico.

2 - Reumatismo.

3 - Espondilitis Anquilosante.

4 - Psoriasis.

"""
##Importamos la libreria pyknow - https://pyknow.readthedocs.io/en/stable/index.html
from pyknow import *

##Creamos el objeto de conocimiento
class paciente(Fact):
    """Info sobre el paciente"""
    pass

def SUMCAMPOS(p, *fields):
    return sum([p.get(x, 0) for x in fields])

##Creamos la clase que instancia el motor de conocimiento
class DiagnosticoAutoInm(KnowledgeEngine):
    ##Se define la regla de edad para el pacinete
    @Rule(paciente(edad=P(lambda x: x <= 45)))
    def preocupacion(self):
        self.declare(Fact(preocupante=True))

    ##Se define la lista de sintomas indicativos de bajo riesgo
    @Rule(Fact(preocupante=True),
          AS.p << paciente(),
          TEST(lambda p: SUMCAMPOS(p,
                                   'dolor_de_espalda',
                                   'dolor_de_cuello',
                                   'dolor_de_rodillas',
                                   'dolor_de_cabeza',
                                   'dolor_de_manos',
                                   'dolor_de_brazos',
                                   'uveitis',
                                   'fiebre') > 2))
    def tiene_sintomas_autoinmunes(self, p):
        self.declare(Fact(tiene_sintomas_autoinmunes=True))

    #Se describen las reglas para lanzar una alerta de diagnostico de bajo riesgo
    @Rule(Fact(preocupante=True),
          Fact(antecedentes_familiares=True),
          Fact(tiene_sintomas_autoinmunes=True))
    def protocole_risk_low(self):
        print("El paciente puede presentar una enfermedad autoinmune")
        print(test)

    @Rule(Fact(preocupante=True),
        Fact(espondilitis_risk=True),
        Fact(tiene_sintomas_autoinmunes=True))
    def protocole_risk_low(self):
        print("El paciente puede presentar una enfermedad autoinmune")
        print(test)

    @Rule(Fact(preocupante=True),
        Fact(reumatismo_risk=True),
        Fact(tiene_sintomas_autoinmunes=True))
    def protocole_risk_low(self):
        print("El paciente puede presentar una enfermedad autoinmune")
        print(test)

    @Rule(Fact(preocupante=True),
        Fact(lupus_risk=True),
        Fact(tiene_sintomas_autoinmunes=True))
    def protocole_risk_low(self):
        print("El paciente puede presentar una enfermedad autoinmune")

    ##Se define la lista de sintomas indicativos de alto riesgo
    @Rule(Fact(preocupante=True),
        AS.p  << paciente(),
        TEST(lambda p: SUMCAMPOS(p,
                               'bursitis_tendinitis_del_hombro',
                               'bursitis_tendinitis_de_muneca',
                               'bursitis_tendinitis_de_biceps',
                               'bursitis_tendinitis_de_pierna',
                               'bursitis_tendinitis_de_rotula',
                               'bursitis_tendinitis_de_tobillo',
                               'bursitis_tendinitis_de_cadera',
                               'bursitis_tendinitis_de_tendon_de_Aquiles',
                               'osteo_artritis') > 2))

    def tiene_sintomas_autoinmunes_severos(self, p):
        self.declare(Fact(tiene_sintomas_autoinmunes_severos=True))

    #Se describen las reglas para lanzar una alerta de diagnostico de alto riesgo
    @Rule(Fact(preocupante=True),
        Fact(psoriasis_risk=True),
        Fact(tiene_sintomas_autoinmunes_severos=True))
    def protocole_alert_high(self):
        print("¡Advertencia! El pasiente tiene alto riesgo de padecer Psoriasis")

    @Rule(Fact(preocupante=True),
        Fact(espondilitis_risk=True),
        Fact(tiene_sintomas_autoinmunes_severos=True))
    def protocole_risk_high(self):
        print("¡Advertencia! El pasiente tiene alto riesgo de padecer Espondilitis Anquilosante")

    @Rule(Fact(preocupante=True),
        Fact(reumatismo_risk=True),
        Fact(tiene_sintomas_autoinmunes_severos=True))
    def protocole_risk_high(self):
        print("¡Advertencia! El pasiente tiene alto riesgo de padecer Reumatismo")

    @Rule(Fact(preocupante=True),
        Fact(lupus_risk=True),
        Fact(tiene_sintomas_autoinmunes_severos=True))
    def protocole_risk_high(self):
        print("¡Advertencia! El pasiente tiene alto riesgo de padecer lupus")

    @Rule(Fact(preocupante=True),
          paciente(tiene_sintomas_autoinmunes=True))
    def tiene_antecedentes_familiares(self):
        self.declare(Fact(tiene_antecedentes_familiares=True))
        print(test)

    @Rule(Fact(preocupante=True),
          paciente(HLA=MATCH.HLA))
    def lupus(self, HLA):
        lupus = ["HLA1", "HLA2", "IRF5", "PTPN22", "STAT4", "CDKN1A", "ITGAM", "BLK", "TNFSF4", "BANK1"]
        if HLA in lupus:
            self.declare(Fact(lupus_risk=True))
            print("¡Advertencia! Riesgo de lupus")
        else:
            self.declare(Fact(lupus_risk=False))

    @Rule(Fact(preocupante=True),
          paciente(HLA=MATCH.HLA))
    def reumatismo(self, HLA):
        reumatismo = ["HLA-DR4","HLA-DRB1", "CD28", "CD40"]
        if HLA in reumatismo:
            self.declare(Fact(reumatismo_risk=True))
            print("¡Advertencia! Riesgo de Reumatismo")
        else:
            self.declare(Fact(reumatismo_risk=False))

    @Rule(Fact(preocupante=True),
          paciente(HLA=MATCH.HLA))
    def espondilitis(self, HLA):
        espondilitis = ["HLA-b27"]
        if HLA in espondilitis:
            print("¡Advertencia! Riesgo de Espondilitis Anquilosante")
            self.declare(Fact(espondilitis_risk=True))
        else:
            self.declare(Fact(espondilitis_risk=False))

    @Rule(Fact(preocupante=True),
          paciente(HLA=MATCH.HLA))
    def psoriasis(self, HLA):
        psoriasis = ["PSORS1","HLA-C", "HLA-Cw6", "CCHCR1","CDSN"]
        if HLA in psoriasis:
            print("¡Advertencia! Riesgo de Psoriasis")
            self.declare(Fact(psoriasis_risk=True))
        else:
            self.declare(Fact(psoriasis_risk=False))


#Se instancia el motor
engine = DiagnosticoAutoInm()
#Se resetea el motor para comenzar a operar
engine.reset()


# Secuencia de entrada para el medico residente
edad=int(input("Ingrese la edad del paciente: "))

HLA=input("Ingrese el marcador genetico encontrado: ")

dolor_de_espalda=input("¿El paciente presenta dolor de espalda? S/N: ")
if dolor_de_espalda == "s":
    dolor_de_espalda = True
else:
    dolor_de_espalda = False


dolor_de_cuello=input("¿El paciente presenta dolor de cuello? S/N: ")
if dolor_de_cuello == "s":
    dolor_de_cuello = True
else:
    dolor_de_cuello = False

dolor_de_rodillas=input("¿El paciente presenta dolor de rodilla? S/N: ")
if dolor_de_rodillas == "s":
    dolor_de_rodillas = True
else:
    dolor_de_rodillas = False

dolor_de_cabeza=input("¿El paciente presenta dolor de cabeza? S/N: ")
if dolor_de_cabeza == "s":
    dolor_de_cabeza = True
else:
    dolor_de_cabeza = False

dolor_de_manos=input("¿El paciente tiene dolor de manos? S/N: ")
if dolor_de_manos == "s":
    dolor_de_manos = True
else:
    dolor_de_manos = False

dolor_de_brazos=input("¿El paciente presenta dolor de brazos? S/N: ")
if dolor_de_brazos == "s":
    dolor_de_brazos = True
else:
    dolor_de_brazos = False

uveitis=input("¿El paciente tiene uveits? S/N: ")
if uveitis == "s":
    uveitis = True
else:
    uveitis = False

fiebre=input("¿El paciente presenta fiebre? S/N: ")
if fiebre == "s":
    fiebre = True
else:
    fiebre = False

bursitis_tendinitis_del_hombro=input("¿El paciente presenta inflamacion de hombro? S/N: ")
if bursitis_tendinitis_del_hombro == "s":
    bursitis_tendinitis_del_hombro = True
else:
    bursitis_tendinitis_del_hombro = False

bursitis_tendinitis_de_muneca=input("¿El paciente presenta inflamacion de muñeca? S/N: ")
if bursitis_tendinitis_de_muneca == "s":
    bursitis_tendinitis_de_muneca = True
else:
    bursitis_tendinitis_de_muneca = False

bursitis_tendinitis_de_biceps=input("¿El paciente presenta inflamacion de biceps? S/N: ")
if bursitis_tendinitis_de_biceps == "s":
    bursitis_tendinitis_de_biceps = True
else:
    bursitis_tendinitis_de_biceps = False

bursitis_tendinitis_de_pierna=input("¿El presenta presenta inflamacion de piernas? S/N: ")
if bursitis_tendinitis_de_pierna == "s":
    bursitis_tendinitis_de_pierna = True
else:
    bursitis_tendinitis_de_pierna = False

bursitis_tendinitis_de_rotula=input("¿El paciente presenta inflamacion de rotula? S/N: ")
if bursitis_tendinitis_de_rotula == "s":
    bursitis_tendinitis_de_rotula = True
else:
    bursitis_tendinitis_de_rotula = False

bursitis_tendinitis_de_tobillo=input("¿El paciente presenta inflamacion de tobillo? S/N: ")
if bursitis_tendinitis_de_tobillo == "s":
    bursitis_tendinitis_de_tobillo = True
else:
    bursitis_tendinitis_de_tobillo = False

bursitis_tendinitis_de_cadera=input("¿El paciente presenta inflamacion de cadera? S/N: ")
if bursitis_tendinitis_de_cadera == "s":
    bursitis_tendinitis_de_cadera = True
else:
    bursitis_tendinitis_de_cadera = False

bursitis_tendinitis_de_tendon_de_Aquiles=input("¿El paciente presenta inflamacion de tendon de aquiles? S/N: ")
if bursitis_tendinitis_de_tendon_de_Aquiles == "s":
    bursitis_tendinitis_de_tendon_de_Aquiles = True
else:
    bursitis_tendinitis_de_tendon_de_Aquiles = False

osteo_artritis=input("¿El paciente presenta osteo artritis? S/N: ")
if osteo_artritis == "s":
    osteo_artritis = True
else:
    osteo_artritis = False

#Se declaran y asignan las variables con las que trabajará el motor
engine.declare(paciente(edad=edad,
                        HLA=HLA,
                        dolor_de_espalda=dolor_de_espalda,
                        dolor_de_cuello=dolor_de_cuello,
                        dolor_de_rodillas=dolor_de_rodillas,
                        dolor_de_cabeza=dolor_de_cabeza,
                        dolor_de_manos=dolor_de_manos,
                        dolor_de_brazos=dolor_de_brazos,
                        uveitis=uveitis,
                        fiebre=fiebre,
                        bursitis_tendinitis_del_hombro=bursitis_tendinitis_del_hombro,
                        bursitis_tendinitis_de_muneca=bursitis_tendinitis_de_muneca,
                        bursitis_tendinitis_de_biceps=bursitis_tendinitis_de_biceps,
                        bursitis_tendinitis_de_pierna=bursitis_tendinitis_de_pierna,
                        bursitis_tendinitis_de_rotula=bursitis_tendinitis_de_rotula,
                        bursitis_tendinitis_de_tobillo=bursitis_tendinitis_de_tobillo,
                        bursitis_tendinitis_de_cadera=bursitis_tendinitis_de_cadera,
                        bursitis_tendinitis_de_tendon_de_Aquiles=bursitis_tendinitis_de_tendon_de_Aquiles,
                        osteo_artritis=osteo_artritis))

#Se ejecuta el motor y este da un diagnostico basado en las reglas diseñadas
engine.run()
