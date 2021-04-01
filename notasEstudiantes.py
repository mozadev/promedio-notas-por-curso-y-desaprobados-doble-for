#declaracion de variables
list_est=[]
list_cur=[]
list_notas=[]
matriz=[]


#ingreso de variables
#ingreso de estudiantes
n_est=int(input("ingrese numero de estudiantes: "))
for i in range(n_est):
    nomb_est =input("nombre del estudiante ["+str(i)+"]: ")
    list_est.append(nomb_est)


#ingreso de cursos
n_cursos=int(input("ingrese cantidad de cursos: "))
for i in range(n_cursos):
    nom_curs =input("nombre del curso ["+str(i)+"]: ")
    list_cur.append(nom_curs)


#ingreso de notas de los cursos para cada uno de los estudiantes
for i in range(len(list_est)):
    print("\n")
    print("ingreso de notas del estudiante: "+"["+list_est[i]+"]"+"\n")
    for j in range(len(list_cur)):
        nota=int(input("ingrese la nota del curso ["+list_cur[j]+"]:"))
        list_notas.append(nota)
        filas = []
        filas.append(list_est[i])
        filas.append(list_cur[j])
        filas.append(nota)
        matriz.append(filas)


#imprimiendo la matriz
print("estudinate"+" "+"curso"+" "+"nota")
for filas in matriz:
    print(filas)


#consultando por curso : promedio notas y alumanos aprobados
nombre_curso=input("nombre del curso a consultar: ")
suma = 0
lista_aprobados=[]
for fila in matriz:
    if fila[1]==nombre_curso:
        suma=suma+fila[2]
        if fila[2]>10.5:
            aprobado=fila[0]
            lista_aprobados.append(aprobado)
promedio=suma/n_est


# salida de informacion promedio de notas
print("promedio de notas del curso: "+str(promedio))
if len(lista_aprobados)>0:
    print("estudiantes que aprobaron el curso : ", lista_aprobados)
else:
    print("estudiantes que aprobaron el curso: ", 0)


