"""Importando modulos"""
import time
import os
import return_position as rp

if __name__ == "__main__":
    print("teste")
    print("Este programa salva no arquivo coordenadas_mouse.txt as coordenadas "
          "retornadas pela posição do mouse")
    print()
    print("Após a digitar y e pressionar ENTER, o sistema ira capturar a posição do "
          "mouse após 5 segundos.")
    print()
    print("Para sair digite n.")
    UP = True
    try:
        while UP:
            print()
            nova_captura = input("Realizar nova captura(y/n)? ")
            if nova_captura.lower() == "y":
                time.sleep(3)
                coordinates = rp.get_mouse_postition()
                print()
                print("Posição salva no arquivo.")
                LINE = 1
                if os.path.exists("coordenadas_mouse.txt"):
                    check_file = os.stat("coordenadas_mouse.txt").st_size
                    if check_file != 0:
                        with open("coordenadas_mouse.txt", encoding="utf-8") as f:
                            LINE = len(f.readlines()) + 1
                with open("coordenadas_mouse.txt", "a", encoding="utf-8") as f:
                    f.write(f"{LINE}. {coordinates}\n")
            elif nova_captura.lower() == "n":
                print()
                print("Fechando programa.")
                time.sleep(2)
                UP = False
            else:
                print()
                print("Por favor entre com um valor valido y ou n.")
    except KeyboardInterrupt as error:
        print()
        print("Fechando programa.")
        time.sleep(2)
