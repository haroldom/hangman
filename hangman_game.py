
# Hola!
# Extraño o extraña
# Muchas gracias por descargar
# El juego está en su versión beta
# Se pueden presentar algunos errores o bugs
# Comunícate con @Harold Ormeño para corregirlo


# Sigue teniendo un gran día!


from operator import le
import os
import random



# Selecciona una palabra aleatoria de la base de datos
def word_random(database):
    # Lectura de la base de datos de las palabras en base a un número random

    word_number = random.randint(0,170)
    words = []
    letter_number = 0
    
    with open(database, 'r', encoding="utf-8") as word_list:
        for line in word_list:
            words.append(line.rstrip())

    selected_word = words[word_number]

    for i in selected_word:
        letter_number+=1
    
    caracter = []
    
    for indice in range(len(selected_word)):
            caracter.append(selected_word[indice])


    return selected_word, caracter, letter_number 

    # Retorna la palabra seleccionada y la cantidad de espacios




def print_title(print_big_title, print_small_title,columns,sprites):
    os.system("cls")
    if columns > 63:
        print(print_big_title)
        print("\n")
    else:
        print(print_small_title)
        print("\n")
    print("¡Let's go play!".center(columns))

def validation_word(letters):
    condition_for = False
    condition = False
    repeated_letters = 0
    while condition == False:
        my_word = input("Escribe una letra... \n")
        for indice in range(len(letters)):
            if my_word == letters[indice]:
                condition_for = True
                
            if condition_for == True:
                repeated_letters += 1
                condition_for = False   
        break
    
    if repeated_letters > 0:
        condition = True

    return condition, repeated_letters, my_word

def ingresar_input(letters):
    fun_validation = validation_word(letters)
    my_letter = fun_validation[2]
    the_validation = fun_validation[0]
    return my_letter, the_validation


def determinar_ganador(the_word, my_word):
    if my_word == the_word:
        return True
    else:
        return False

def recargar_pantalla_condition(x_word, database,letter_number, letters, the_word,the_validation, my_letter,spaces, my_spaces, sprites, columns, print_big_title, print_small_title):
    os.system("cls")
    indices_remplazar = []
    print_title(print_big_title, print_small_title,columns,sprites)
    ganaste = False
    primera_ronda = 1
    mi_palabra_victoria = []
    validar_mi_palabra_victoria = ""
    errores = 0
    espacios_modificados = []
    nueva_partida = 0
    corregir_bug = False
    ya_no_entrar = False

    for x in range(letter_number):
        mi_palabra_victoria.append("_")

    while ganaste == False:
        ## Letters contiene todas las letras
        if primera_ronda != 1:
            registrar_input = ingresar_input(letters)
            my_letter = registrar_input[0]
            the_validation = registrar_input[1]

        if the_validation == True:
            os.system("cls")
            print_title(print_big_title, print_small_title,columns,sprites)

            for num in range(len(the_word)):
                if the_word[num] == my_letter:
                    indices_remplazar.append(num)
            for x in range(len(indices_remplazar)):
                spaces[indices_remplazar[x]] = (f"{my_letter} ")
                mi_palabra_victoria[indices_remplazar[x]] = (f"{my_letter}")


            espacios_modificados = "".join(spaces)
            espacios_modificados = espacios_modificados.center(columns)
            print(espacios_modificados)
            print(f"\n\n{sprites[errores]}\n\n")
            primera_ronda -= 1 
            indices_remplazar.clear()
            validar_mi_palabra_victoria = "".join(mi_palabra_victoria)

            ganaste = determinar_ganador(the_word, validar_mi_palabra_victoria)
        else:
            if primera_ronda == 1:
                print(my_spaces)
                errores += 1
                print(f"\n\n{sprites[errores]}\n\n") 
                primera_ronda -= 1
            else:
                os.system('cls')
                print_title(print_big_title, print_small_title,columns,sprites)
                if len(espacios_modificados) == 0:
                    print(my_spaces) 
                    errores += 1
                    print(f"\n\n{sprites[errores]}\n\n") 
                    primera_ronda -= 1
                else:
                    print(espacios_modificados) 
                    errores += 1
                    print(f"\n\n{sprites[errores]}\n\n") 
                    primera_ronda -= 1
                if errores == 6:
                    print("¡Perdiste!, No pasa nada, inténtalo de nuevo")
                    print(f"La palabra era: {x_word[0]}")  
                    break
        if  ganaste == True:
            print('¡Felicidades jugador, Ganaste!')
            break
    
    return False    

def reload_modify(print_big_title, print_small_title, columns, sprites,database):
    os.system("cls")
    print_title(print_big_title, print_small_title,columns,sprites)
    space_main = "_ "
    x_word = word_random(database)
    the_word = x_word[0]
    letter_number = x_word[2]
    letters = x_word[1]
    spaces = []
    count = 0


    for i in the_word:
        spaces.append(space_main)


    for number in range(len(spaces)):
        count += 1
        if count == len(spaces):
            my_spaces = spaces[number]*count
    
    my_spaces = my_spaces.center(columns)
    print(my_spaces)
    print(f"\n\n{sprites[0]}\n\n")      
    

    fun_validation = validation_word(letters)
    my_letter = fun_validation[2]
    the_validation = fun_validation[0]


    
    recargar_pantalla_condition(x_word,database, letter_number,letters, the_word,the_validation, my_letter,spaces,my_spaces, sprites, columns, print_big_title, print_small_title) 
    print("¿Quieres jugar de nuevo?")
    mi_condicion = False
    error_nueva_partida = False
    while mi_condicion == False:
        while error_nueva_partida == False:
            try:
                nueva_partida = int(input("1. Sí    2. No \n Escribe aquí... ")) 
                break
            except ValueError:
                print("Por favor introduce un número")
        if nueva_partida == 1:
            play(database,print_big_title, print_small_title,columns,sprites)
            break
        elif nueva_partida == 2:
            print("Muchas gracias por probar la beta, te espero pronto:D")
            mi_condicion = True
            break
        else:
            print("Por favor introduce una opción válida")


def play(database, print_big_title, print_small_title,columns,sprites):
    reload_modify(print_big_title, print_small_title, columns, sprites,database)

    

# Literalmente, la función del menú principal
def run_main_menu(database, columns, main_menu, print_menu, print_cat, print_big_title, print_small_title,sprites):
    #Dependiendo del tamaño de la ventana, imprimir el titulo grande, o el titulo pequeño
    os.system("cls")
    if columns > 63:
        print(print_big_title)
        print("\n\n\n\n")
        print(print_cat)
        print(print_menu)
    else:
        print(print_small_title)
        print(print_menu)


    print("\n")
    error_menu2 = 1

    while error_menu2 == 1:
        try:
            option = int(input("Escribe aquí... "))
            error_menu2 -= 1
        except ValueError:
            print("Por favor, escribe un número")

    error_menu = 1
    while error_menu == 1:
        if option == 1:
            play(database, print_big_title, print_small_title, columns,sprites)
            break
        elif option == 2:
            print("Por el momento, esta opción no se encuentra disponible, por favor introduzca otra opción")
            try:
                option = int(input("Escribe aquí... "))
                error_menu2 -= 1
            except ValueError:
                print("Por favor, escribe un número")
        elif option == 3:
            print("Por el momento, esta opción no se encuentra disponible, por favor introduzca otra opción")
            try:
                option = int(input("Escribe aquí... "))
                error_menu2 -= 1
            except ValueError:
                print("Por favor, escribe un número")
        elif option == 4:
            os.system("cls")
            print("Adiós")
            break
        else:
            print("Por favor, escribe una opción válida")
            try:
                option = int(input("Escribe aquí... "))
                error_menu2 -= 1
            except ValueError:
                print("Por favor, escribe un número")




def run():
    
    # VARIABLES PRINCIPALES
    terminal_size = os.get_terminal_size()
    columns = terminal_size.columns
    rows = terminal_size.lines
    database = './Base_de_datos/data.txt'

    

    sprite1_a = "  +---+"
    sprite1_b = "  |   |"
    sprite1_c = "      |"
    sprite1_d = "      |"
    sprite1_e = "      |"
    sprite1_f = "      |"
    sprite1_g = "========="

    sprite2_a = "  +---+"
    sprite2_b = "  |   |"
    sprite2_c = "  O   |"
    sprite2_d = "      |"
    sprite2_e = "      |"
    sprite2_f = "      |"
    sprite2_g = "========="

    sprite3_a = "  +---+"
    sprite3_b = "  |   |"
    sprite3_c = "  O   |"
    sprite3_d = "  |   |"
    sprite3_e = "      |"
    sprite3_f = "      |"
    sprite3_g = "========="

    sprite4_a = "  +---+"
    sprite4_b = "  |   |"
    sprite4_c = "  O   |"
    sprite4_d = " /|   |"
    sprite4_e = "      |"
    sprite4_f = "      |"
    sprite4_g = "========="

    sprite5_a = "  +---+"
    sprite5_b = "  |   |"
    sprite5_c = "  O   |"
    sprite5_d = " /|\  |"
    sprite5_e = "      |"
    sprite5_f = "      |"
    sprite5_g = "========="
    
    sprite6_a = "  +---+"
    sprite6_b = "  |   |"
    sprite6_c = "  O   |"
    sprite6_d = " /|\  |"
    sprite6_e = " /    |"
    sprite6_f = "      |"
    sprite6_g = "========="
    
    sprite7_a = "  +---+"
    sprite7_b = "  |   |"
    sprite7_c = "  O   |"
    sprite7_d = " /|\  |"
    sprite7_e = " / \  |"
    sprite7_f = "      |"
    sprite7_g = "========="



    sprite1 = f"{sprite1_a.center(columns).rstrip()}\n{sprite1_b.center(columns).rstrip()}\n{sprite1_c.center(columns).rstrip()}\n{sprite1_d.center(columns).rstrip()}\n{sprite1_e.center(columns).rstrip()}\n{sprite1_f.center(columns).rstrip()}\n{sprite1_g.center(columns).rstrip()}"
    sprite2 = f"{sprite2_a.center(columns).rstrip()}\n{sprite2_b.center(columns).rstrip()}\n{sprite2_c.center(columns).rstrip()}\n{sprite2_d.center(columns).rstrip()}\n{sprite2_e.center(columns).rstrip()}\n{sprite2_f.center(columns).rstrip()}\n{sprite2_g.center(columns).rstrip()}"
    sprite3 = f"{sprite3_a.center(columns).rstrip()}\n{sprite3_b.center(columns).rstrip()}\n{sprite3_c.center(columns).rstrip()}\n{sprite3_d.center(columns).rstrip()}\n{sprite3_e.center(columns).rstrip()}\n{sprite3_f.center(columns).rstrip()}\n{sprite3_g.center(columns).rstrip()}"
    sprite4 = f"{sprite4_a.center(columns).rstrip()}\n{sprite4_b.center(columns).rstrip()}\n{sprite4_c.center(columns).rstrip()}\n{sprite4_d.center(columns).rstrip()}\n{sprite4_e.center(columns).rstrip()}\n{sprite4_f.center(columns).rstrip()}\n{sprite4_g.center(columns).rstrip()}"
    sprite5 = f"{sprite5_a.center(columns).rstrip()}\n{sprite5_b.center(columns).rstrip()}\n{sprite5_c.center(columns).rstrip()}\n{sprite5_d.center(columns).rstrip()}\n{sprite5_e.center(columns).rstrip()}\n{sprite5_f.center(columns).rstrip()}\n{sprite5_g.center(columns).rstrip()}"
    sprite6 = f"{sprite6_a.center(columns).rstrip()}\n{sprite6_b.center(columns).rstrip()}\n{sprite6_c.center(columns).rstrip()}\n{sprite6_d.center(columns).rstrip()}\n{sprite6_e.center(columns).rstrip()}\n{sprite6_f.center(columns).rstrip()}\n{sprite6_g.center(columns).rstrip()}"
    sprite7 = f"{sprite7_a.center(columns).rstrip()}\n{sprite7_b.center(columns).rstrip()}\n{sprite7_c.center(columns).rstrip()}\n{sprite7_d.center(columns).rstrip()}\n{sprite7_e.center(columns).rstrip()}\n{sprite7_f.center(columns).rstrip()}\n{sprite7_g.center(columns).rstrip()}"

    sprites = [sprite1, sprite2, sprite3, sprite4, sprite5, sprite6, sprite7]


    # DISEÑO DE INTERFAZ

    title_columns = 63
 

    #Titulo grande
    big_title1 = "██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗"
    big_title2 = "██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║"
    big_title3 = "███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║"
    big_title4 = "██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║"
    big_title5 = "██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║"
    big_title6 = "╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝"
    big_title7 = "by Harold Ormeño"

    #Titulo pequeño
    small_title1 = "█░█ ▄▀█ █▄░█ █▀▀ █▀▄▀█ ▄▀█ █▄░█"
    small_title2 = "█▀█ █▀█ █░▀█ █▄█ █░▀░█ █▀█ █░▀█"
    small_title3 = "by Harold Ormeño"

    # Gato decorativo
    cat_menu1 = """                          __..--''``\--....___   _..,_"""
    cat_menu2 = """      ///// _.-'    .-/";  `        ``<._  ``-+'~=. ////"""
    cat_menu3 = """    ///_.-' _..--.'-    \                    `(^) ) //"""
    cat_menu4 = """   // ((..-' // (< -     ;_..__               ; `' //"""
    cat_menu5 = """  ////////////// `-._,_)'//////``--...____..-' /////"""
    cat_menu6 = """ //////////////////////////////////////////////////"""
    cat_menu7 = """//////////////////////////////////////////////////"""

    # Variables para imprimir en consola el menú principal
    main_menu = ["Bienvenido a Hangman 2021", "Selecciona una opción", "1.- Jugar", "2.-Dificultad (No disponible)", "3.- Logros (No disponible)", "4.- Salir del Juego", " ","Versión: Beta 1.0"]
    print_menu = f"{main_menu[0].center(columns).rstrip()}\n\n{main_menu[1].center(columns).rstrip()}\n{main_menu[2].center(columns).rstrip()}\n{main_menu[3].center(columns).rstrip()}\n{main_menu[4].center(columns).rstrip()}\n{main_menu[5].center(columns).rstrip()}\n{main_menu[6].center(columns).rstrip()}\n{main_menu[7].center(columns).rstrip()}"
    print_cat =  f"{cat_menu1.center(columns).rstrip()}\n{cat_menu2.center(columns).rstrip()}\n{cat_menu3.center(columns).rstrip()}\n{cat_menu4.center(columns).rstrip()}\n{cat_menu5.center(columns).rstrip()}\n{cat_menu6.center(columns).rstrip()}\n{cat_menu7.center(columns).rstrip()}\n"
    print_big_title = f"{big_title1.center(columns).rstrip()}\n{big_title2.center(columns).rstrip()}\n{big_title3.center(columns).rstrip()}\n{big_title4.center(columns).rstrip()}\n{big_title5.center(columns).rstrip()}\n{big_title6.center(columns).rstrip()}\n{big_title7.center(columns).rstrip()}"
    print_small_title = f"{small_title1.center(columns).rstrip()}\n{small_title2.center(columns).rstrip()}\n{small_title3.center(columns).rstrip()}"

    
    
    # IMPRIMIRMOS EL MENÚ PRINCIPAL
    run_main_menu(database, columns, main_menu, print_menu, print_cat, print_big_title, print_small_title,sprites)

    



if __name__ == '__main__':
    run()