class Alumno:
    #atributos
    nacionalidad='peruano'
    nota1,nota2,nota3=0,0,0
    #Constructor: valores que van a tener por defecto mi clase, que se le instancia a una variable
    def __init__(self,nota1,nota2,nota3):
        self.nota1=nota1
        self.nota2=nota2
        self.nota3=nota3
        self.promedio=0
        self.resultado='Pendiente'
        self.nom=''
        self.dist=''
    #Métodos: Son las funciones de la clase
    def datos(self):
        self.nom=input('Ingrese nombre del alumno: ')
        self.dist=input('Ingrese el distrito del alumno: ')
    def promediar(self):
        promedio=self.promedio=(self.nota1+self.nota2+self.nota3)/3
    def calificar(self):
        if self.promedio>=13:
            self.resultado='Aprobado'
        else:
            self.resultado='Reprobado'
alum1=Alumno(8,15,12)
alum1.datos()
alum1.promediar()
alum1.calificar()
print('El alumno {} es del distrito de {}.'.format(alum1.nom,alum1.dist))
print('El promedio del primer alumno es: {}.'.format(alum1.promedio))
print('El alumno está: {}'.format(alum1.resultado))
alum2=Alumno(13,15,18)
alum2.promediar()
alum2.calificar()
print('El promedio del segundo alumno es: {}.'.format(alum2.promedio))
print('El alumno está: {}'.format(alum2.resultado))