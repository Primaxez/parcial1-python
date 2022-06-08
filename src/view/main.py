import os
from data_reading.file_path_handler import FileHandler
from exceptions.incomplete_file_error import IncompleteFileError
from exceptions.not_text_file_error import NotTextFileError
from view.utils import (
    average_time_per_age_group_and_sex,
    histogram_per_age_group,
    total_participants_ammount, 
    total_participants_list, 
    total_participants_per_age_group, 
    total_participants_per_sex,
    winner_total,
    winners_per_age_group,
    winners_per_age_group_and_sex,
    winners_per_sex)

def header(file_path):
    """
    Prints the app header
    """
    os.system("cls")
    print("Aplicacion de Analisis de Competencia")
    print("Alumno: Alejandro Pestana\n")
    if(file_path.file_dir):
        print(f"Archivo cargado actualmente:\n{file_path.file_dir}")
    print("-------------------------------------")

def menu_actions(file_path: FileHandler):
    """
    Displays actions menu
    """
    loop_check = 1
    while loop_check:
        header(file_path)
        print("1. Lista con la totalidad de participantes (tabla)")
        print("2. Cantidad total de participantes (una línea)")
        print("3. Cantidad de participantes por grupo etario (tabla, solo el grupo y la cantidad)")
        print("4. Cantidad de participantes por sexo (línea, sólo el grupo y la cantidad)")
        print("5. Ganadores por grupo etario (tabla)")
        print("6. Ganadores por sexo (tabla)")
        print("7. Ganadores por grupo etario y sexo (tabla)")
        print("8. Ganador general (línea)")
        print("9. Histograma de participante por grupo etario")
        print("10. Promedio de tiempo por grupo etario y sexo")
        print("11. Regresar")
        print("-------------------------------------")
        try:
            option = int(input("Indica una opcion: "))
            if (option != 11):
                header(file_path)
            contest_data = file_path.data_handler.contest_data
        except ValueError:
            option = -1
        match option:
            case 1:
                total_participants_list(contest_data)
            case 2:
                total_participants_ammount(contest_data)
            case 3:
                total_participants_per_age_group(file_path.data_handler)
            case 4:
                total_participants_per_sex(file_path.data_handler)
            case 5:
                winners_per_age_group(file_path.data_handler)
            case 6:
                winners_per_sex(file_path.data_handler)
            case 7:
                winners_per_age_group_and_sex(file_path.data_handler)
            case 8:
                winner_total(file_path.data_handler)
            case 9:
                histogram_per_age_group(file_path.data_handler)
            case 10:
                average_time_per_age_group_and_sex(file_path.data_handler)
            case 11: 
                loop_check = 0
            case _:
                print("\nOpcion incorrecta.")
        if (option != 11):
            input("Presione enter para continuar.")

def menu_load_file(file_path):
    """
    Displays file loading menu
    """
    header(file_path)
    print("Indique direccion del archivo")
    print('Ejemplo local: "../data/competencia.txt" si ejecutas desde /src/')
    print('Ejemplo absoluto: "C:/Users/user/Desktop/Parcial 1 Python/parcial1-python/data/competencia.txt"')
    print("-------------------------------------")
    try:
        file_path.file_dir = input("")
    except (FileNotFoundError,
            NotTextFileError,
            IncompleteFileError) as e:
            print(f"\n{e}")

def menu_file(file_path) -> int:
    """
    Displays file menu
    """
    loop_check = 1
    while loop_check:
        header(file_path)
        print("1. Cargar archivo")
        print("2. Salir")
        print("3. Regresar")
        print("-------------------------------------")
        try:
            option = int(input("Indica una opcion: "))
        except ValueError:
            option = -1
        match option:
            case 1:
                menu_load_file(file_path)
                loop_check = 0
            case 2:
                exit()
            case 3:
                loop_check = 0
            case _:
                input("\nOpcion incorrecta. Presione enter para continuar.")

def main():
    """
    Displays main menu of the app
    """
    loop_check = 1
    file_path = FileHandler()
    while loop_check:
        header(file_path)
        print("1. Archivo")
        print("2. Acciones")
        print("-------------------------------------")
        try:
            option = int(input("Indica una opcion: "))
        except ValueError:
            # If something other than a number is indicated, then it's handled like a wrong option
            option = -1
        match option:
            case 1:
                menu_file(file_path)
            case 2:
                if(file_path.data_handler.contest_data != []):
                    menu_actions(file_path)
                else:
                    print("\n¡Errror: No hay datos cargados en el sistema!")
            case _:
                print("\nOpcion incorrecta.")
        input("Presione enter para continuar.")