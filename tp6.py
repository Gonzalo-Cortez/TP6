Datos = {  
    "Alumnos": []  
}  

def agregar_alumno(nombre, apellido, dni, fecha_nacimiento, tutor, notas=None, faltas=0, amonestaciones=0):  
    
    if notas is None:  
        notas = []   
    alumno = {  
        "Nombre": nombre,  
        "Apellido": apellido,  
        "DNI": dni,  
        "Fecha de nacimiento": fecha_nacimiento,  
        "Tutor": tutor,  
        "Notas": notas,  
        "Faltas": faltas,  
        "Amonestaciones": amonestaciones  
    }  
    Datos["Alumnos"].append(alumno)  
    print(f"Alumno {nombre} {apellido} agregado exitosamente.")  

def mostrar_alumno(index):  
   
    try:  
        alumno = Datos["Alumnos"][index]  
        print(f"Datos del alumno:\n"  
              f"Nombre: {alumno['Nombre']}\n"  
              f"Apellido: {alumno['Apellido']}\n"  
              f"DNI: {alumno['DNI']}\n"  
              f"Fecha de Nacimiento: {alumno['Fecha de nacimiento']}\n"  
              f"Tutor: {alumno['Tutor']}\n"  
              f"Notas: {alumno['Notas']}\n"  
              f"Faltas: {alumno['Faltas']}\n"  
              f"Amonestaciones: {alumno['Amonestaciones']}")  
    except IndexError:  
        print("Índice fuera de rango. No se encontró al alumno.")  

def modificar_alumno(index, **datos_modificados):  
    
    try:  
        alumno = Datos["Alumnos"][index]  
        for clave, valor in datos_modificados.items():  
            if clave in alumno:  
                alumno[clave] = valor  
        print(f"Datos del alumno {alumno['Nombre']} {alumno['Apellido']} modificados con éxito.")  
    except IndexError:  
        print("Índice fuera de rango. No se pudo modificar al alumno.")  

def expulsar_alumno(index):  
  
    try:  
        alumno_eliminado = Datos["Alumnos"].pop(index)  
        print(f"Alumno {alumno_eliminado['Nombre']} {alumno_eliminado['Apellido']} expulsado exitosamente.")  
    except IndexError:  
        print("Índice fuera de rango. No se pudo expulsar al alumno.")  

def mostrar_alumnos():  
   
    if not Datos["Alumnos"]:  
        print("No hay alumnos registrados.")  
    else:  
        for i, alumno in enumerate(Datos["Alumnos"]):  
            print(f"Alumno {i + 1}: {alumno['Nombre']} {alumno['Apellido']}, DNI: {alumno['DNI']}")  

def main():  
  
    agregar_alumno("Gonzalo", "Cortez", "43336495", "2001-03-12", "Anacleto Jose", [8, 7, 9], 3, 1)  
    agregar_alumno("Nicole", "Paz", "43650738", "2001-06-15", "Barabara Palavencino", [10, 9, 9], 1, 0)  
    agregar_alumno("Roman", "Santiago", "34567890", "2005-03-30", "Rosa Medina", [6, 5, 7], 2, 2)  

    
    mostrar_alumnos()  
    modificar_alumno(1, Notas=[10, 10, 10], Faltas=2)   
    mostrar_alumno(1)   
    expulsar_alumno(0)  
    mostrar_alumnos()  

if __name__ == "__main__":  
    main()