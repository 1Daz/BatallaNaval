from core.game_logic import Game

def get_valid_coordinate(board_size, prompt):
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value < board_size:
                return value
            else:
                print(f"Ingresa un número entre 0 y {board_size - 1}.\n")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.\n")

def main():
    print("\n########################")
    print("¡Bienvenido a Batalla Naval!\n")

    game = Game(board_size=5)
    num_ships = len(game.ship_sizes)
    print(f"Se desplegaron {num_ships} barcos en el tablero.")

    total_ship_cells = 0
    for ship_location in game.board.ships:
        total_ship_cells += len(ship_location)

    print(f"Hay {total_ship_cells} celdas ocupadas por barcos.\n")
    print("Intenta hundir todos los barcos de la computadora.\n")
    #print("Tablero (oculto):")
    game.get_board_display()
    #print("\nTablero (revelado):")
    
    #game.board.display_ships() # Llamada para mostrar los barcos
    print()

    while not game.has_won():
        print("\n--- Nuevo intento ---")
        row = get_valid_coordinate(game.board.size, "Ingresa la fila: ")
        col = get_valid_coordinate(game.board.size, "Ingresa la columna: ")
        print()

        result = game.process_guess(row, col)
        print(result + "\n")
        game.board.display()
        print()

        if game.has_won():
            print(f"\n¡Ganaste! Hundiste todos los barcos en {game.get_attempts()} intentos.")
            print("########################\n")
            break

if __name__ == "__main__":
    main()