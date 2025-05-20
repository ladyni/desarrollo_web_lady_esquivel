import re
import filetype

def validar_comuna(comuna):
    if comuna:
        return True

    return False

def validar_sector(sector):
    if not sector or len(sector) <= 100:
        return True

    return False

def validar_nombre(nombre):
    if nombre and len(nombre) <= 200:
        return True

    return False

def validar_email(email):
    pattern = re.compile(r"^[\w\-\.]+@([\w-]+\.)+[\w-]{2,}$")
    if email and len(email) <= 100 and pattern.match(email):
        return True

    return False

def validar_celular(celular):
    pattern = re.compile(r"^\+[0-9]{3}.[0-9]{8}$")

    if not celular or pattern.match(celular):
        return True

    return False

def validar_dia_hora_inicio(dia_hora_inicio):
    if dia_hora_inicio:
        return True

    return False

def validar_dia_hora_termino(dia_hora_termino):
    return True

def validar_temas(temas, glosa_otro):
    if 'otro' in temas and glosa_otro:
        return True

    if len(temas) > 0:
        return True

    return False

def validar_fotos(fotos):
    for foto in fotos:
        resultado = validar_foto(foto)
        if not resultado:
            return False

    return True

def validar_foto(foto):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}

    # check if a file was submitted
    if foto is None:
        return False

    # check if the browser submitted an empty file
    if foto.filename == "":
        return False

    # check file extension
    ftype_guess = filetype.guess(foto)
    if ftype_guess.extension not in ALLOWED_EXTENSIONS:
        return False
    # check mimetype
    if ftype_guess.mime not in ALLOWED_MIMETYPES:
        return False
    return True

def validar_campos(comuna, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, temas, glosa_otro, fotos):
    print(validar_comuna(comuna))
    print(validar_sector(sector))
    print(validar_nombre(nombre))
    print(validar_email(email))
    print(validar_celular(celular))
    print(validar_dia_hora_inicio(dia_hora_inicio))
    print(validar_dia_hora_termino(dia_hora_termino))
    print(validar_temas(temas, glosa_otro))
    print(fotos)
    print(validar_fotos(fotos))

    return validar_comuna(comuna) and \
    validar_sector(sector) and \
    validar_nombre(nombre) and \
    validar_email(email) and \
    validar_celular(celular) and \
    validar_dia_hora_inicio(dia_hora_inicio) and \
    validar_dia_hora_termino(dia_hora_termino) and \
    validar_temas(temas, glosa_otro) and \
    validar_fotos(fotos)