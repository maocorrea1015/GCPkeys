def generar_combinaciones():
    print("Generador de Diccionario para Contraseñas")
    print("----------------------------------------")
    
    datos = {
        'nombres': input("Nombre(s): ").split(),
        'apellidos': input("Apellido(s): ").split(),
        'cc': input("Número de documento (CC): "),
        'nacimiento': input("Fecha de nacimiento (DDMMAAAA): "),
        'mama': input("Nombre de la madre: ").split(),
        'papa': input("Nombre del padre: ").split(),
        'hermanos': input("Nombres de hermanos (separados por espacio): ").split(),
        'tios': input("Nombres de tíos (separados por espacio): ").split(),
        'abuelos': input("Nombres de abuelos (separados por espacio): ").split(),
        'mascotas': input("Nombres de mascotas (separados por espacio): ").split(),
    }

    nombre_archivo = input("Ingrese el nombre del archivo (sin extensión): ") + ".txt"
    
    combinaciones = set()
    
    for nombre in datos['nombres']:
        combinaciones.add(nombre.lower())
        combinaciones.add(nombre.capitalize())

    for apellido in datos['apellidos']:
        combinaciones.add(apellido.lower())
        combinaciones.add(apellido.capitalize())

    for nombre in datos['nombres']:
        for apellido in datos['apellidos']:
            combinaciones.add(f"{nombre.lower()}{apellido.lower()}")
            combinaciones.add(f"{nombre.capitalize()}{apellido.capitalize()}")
            combinaciones.add(f"{nombre.lower()}.{apellido.lower()}")

    if datos['cc']:
        combinaciones.add(datos['cc'])
        combinaciones.add(datos['cc'][-4:])  

    if datos['nacimiento']:
        combinaciones.add(datos['nacimiento'])
        combinaciones.add(datos['nacimiento'][-4:])  
        combinaciones.add(datos['nacimiento'][:4])   

    
    familiares = datos['mama'] + datos['papa'] + datos['hermanos'] + datos['tios'] + datos['abuelos']
    for familiar in familiares:
        combinaciones.add(familiar.lower())
        combinaciones.add(familiar.capitalize())

    
    combinaciones_lista = list(combinaciones)  
    for palabra in combinaciones_lista:
        for i in range(100):
            combinaciones.add(f"{palabra}{i}")
            combinaciones.add(f"{palabra}_{i}")
            combinaciones.add(f"{palabra}.{i}")
            if i < 10:
                combinaciones.add(f"{palabra}0{i}")

    
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        for item in sorted(combinaciones):
            f.write(f"{item}\n")
    
    print(f"\nSe generaron {len(combinaciones)} combinaciones en '{nombre_archivo}'")

if __name__ == "__main__":
    generar_combinaciones()
