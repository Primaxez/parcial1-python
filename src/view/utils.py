def total_participants_list(contest_data):
    """
    Shows table of all participants (CI, Name, First Surname, Time)
    """
    print("Lista con la totalidad de participantes:\n")
    print("----------------------------------------------------------------------------------------------------------------------------")
    print("| {:<10} | {:<15} | {:<23} | {:<16} | {:<17} | {:<5} | {:<5} | {:<8} |".format('CI','Primer Nombre', 'Inicial Segundo Nombre', 'Primer Apellido', 'Segundo Apellido', 'Sexo', 'Edad', 'Tiempo'))
    print("----------------------------------------------------------------------------------------------------------------------------")
    for contest_line in contest_data:
        print("| {:<10} | {:<15} | {:<23} | {:<16} | {:<17} | {:<5} | {:<5} | {:<8} |".format(contest_line.get("ci"),contest_line.get("name"),contest_line.get("middle_name_initial"),contest_line.get("first_surname"),contest_line.get("second_surname"),contest_line.get("sex"),contest_line.get("age"),str(contest_line.get("execution_time"))))
    print("----------------------------------------------------------------------------------------------------------------------------")

def total_participants_ammount(contest_data):
    """
    Show a line with the ammout of participants of the contest
    """
    print("Cantidad total de participantes:\n")
    print(f"Hay un total de {len(contest_data)} participantes")

def total_participants_per_age_group(data_handler):
    """
    Shows a table with the ammout of participants per age group of the contest
    """
    print("Cantidad de participantes por grupo etario:\n")
    print("--------------------------------")
    print("| {:<15} | {:<10} |".format('Grupo Etario','Cantidad'))
    print("--------------------------------")
    print("| {:<15} | {:<10} |".format('Juniors',data_handler.count_participants_age_group('Juniors')))
    print("| {:<15} | {:<10} |".format('Seniors',data_handler.count_participants_age_group('Seniors')))
    print("| {:<15} | {:<10} |".format('Masters',data_handler.count_participants_age_group('Masters')))
    print("--------------------------------")

def total_participants_per_sex(data_handler):
    """
    Shows a line with the ammout of participants per sex of the contest
    """
    print("Cantidad de participantes por sexo:\n")
    print(f"Participaron {data_handler.count_participants_sex('M')} hombres y {data_handler.count_participants_sex('F')} mujeres")

def winners_per_age_group(data_handler):
    """
    Shows a table with the winners of each age group
    """
    print("Ganadores por grupo etario:\n")
    print("--------------------------------------------------------------------------------")
    print("| {:<15} | {:<10} | {:<15} | {:<16} | {:<8} |".format('Grupo Etario', 'CI','Primer Nombre', 'Primer Apellido', 'Tiempo'))
    print("--------------------------------------------------------------------------------")
    for age_group in ("Juniors", "Seniors", "Masters"):
        winner = data_handler.get_winner_age_group(age_group)
        if(winner):
            print("| {:<15} | {:<10} | {:<15} | {:<16} | {:<8} |".format(age_group, winner.get("ci"), winner.get("name"), winner.get("first_surname"), str(winner.get("execution_time"))))
        else:
            print(f"No hay participantes en el grupo etario {age_group}")
    print("--------------------------------------------------------------------------------")

def winners_per_sex(data_handler):
    """
    Shows a table with the winners of each sex group
    """
    print("Ganadores por sexo:\n")
    print("----------------------------------------------------------------------")
    print("| {:<5} | {:<10} | {:<15} | {:<16} | {:<8} |".format('Sexo', 'CI','Primer Nombre', 'Primer Apellido', 'Tiempo'))
    print("----------------------------------------------------------------------")
    for sex_group in ("M", "F"):
        winner = data_handler.get_winner_sex(sex_group)
        if(winner):
            print("| {:<5} | {:<10} | {:<15} | {:<16} | {:<8} |".format(sex_group, winner.get("ci"), winner.get("name"), winner.get("first_surname"), str(winner.get("execution_time"))))
        else:
            print(f"No hay participantes de sexo {sex_group}")
    print("----------------------------------------------------------------------")

def winners_per_age_group_and_sex(data_handler):
    """
    Shows a table with the winners of each age group and sex
    """
    print("----------------------------------------------------------------------------------------")
    print("Ganadores por grupo etario y sexo:\n")
    print("----------------------------------------------------------------------------------------")
    print("| {:<15} | {:<5} | {:<10} | {:<15} | {:<16} | {:<8} |".format('Grupo Etario', 'Sexo', 'CI','Primer Nombre', 'Primer Apellido', 'Tiempo'))
    print("----------------------------------------------------------------------------------------")
    for age_group in ("Juniors", "Seniors", "Masters"):
        for sex_group in ("M", "F"):
            winner = data_handler.get_winner_age_group_and_sex(age_group,sex_group)
            if (winner):
                print("| {:<15} | {:<5} | {:<10} | {:<15} | {:<16} | {:<8} |".format(age_group, sex_group, winner.get("ci"), winner.get("name"), winner.get("first_surname"), str(winner.get("execution_time"))))
            else:
                print(f"No hay participantes {age_group} de sexo {sex_group}")
    print("----------------------------------------------------------------------------------------")

def winner_total(data_handler):
    """
    Shows a line with the winner of the contest
    """
    print("Ganador general:\n")
    winner = data_handler.get_winner_total()
    print(f'Cedula: {winner.get("ci")}, Primer Nombre: {winner.get("name")}, Primer Apellido: {winner.get("first_surname")}, Tiempo: {str(winner.get("execution_time"))}')

def histogram_per_age_group(data_handler):
    """
    Shows a histogram of the participants per age group
    """
    print("Histograma de participante por grupo etario:\n")
    ammount_juniors = data_handler.count_participants_age_group('Juniors')
    ammount_seniors = data_handler.count_participants_age_group('Seniors')
    ammount_masters = data_handler.count_participants_age_group('Masters')
    print("{:<9} {:<4} {:<3} {:<300}".format('Juniors (',ammount_juniors,') |',"".join(["*" for number in range(ammount_juniors)])))
    print("{:<9} {:<4} {:<3} {:<300}".format('Seniors (',ammount_seniors,') |',"".join(["*" for number in range(ammount_seniors)])))
    print("{:<9} {:<4} {:<3} {:<300}".format('Masters (',ammount_masters,') |',"".join(["*" for number in range(ammount_masters)])))

def average_time_per_age_group_and_sex(data_handler):
    """
    Shows a table of the average time of each age group and sex
    """
    print("Promedio de tiempo por grupo etario y sexo:\n")
    print("---------------------------------------------")
    print("| {:<15} | {:<5} | {:<15} |".format("Grupo Etario", "Sexo", "Tiempo Promedio"))
    print("---------------------------------------------")
    for age_group in ("Juniors", "Seniors", "Masters"):
        for sex_group in ("M", "F"):
            average_time = data_handler.get_average_time_age_group_and_sex(age_group,sex_group)
            if (average_time):
                print("| {:<15} | {:<5} | {:<15} |".format(age_group, sex_group, str(average_time)))
            else:
                print(f"No hay participantes {age_group} de sexo {sex_group}")
    print("---------------------------------------------")
