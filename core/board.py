import random

class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [['~' for _ in range(size)] for _ in range(size)]
        self.ships = []  # Lista para almacenar la ubicación de cada barco (conjunto de celdas)
        self.ship_sizes_placed = [] # Para recordar el tamaño de cada barco colocado

    def place_ship(self, ship_size):
        """Intenta colocar un barco de un tamaño dado en el tablero."""
        orientation = random.choice(['horizontal', 'vertical'])
        for _ in range(100):
            if orientation == 'horizontal':
                row = random.randint(0, self.size - 1)
                col = random.randint(0, self.size - ship_size)
                locations = set([(row, col + i) for i in range(ship_size)])
            else:
                row = random.randint(0, self.size - ship_size)
                col = random.randint(0, self.size - 1)
                locations = set([(row + i, col) for i in range(ship_size)])

            if not any(loc in existing_ship for existing_ship in self.ships for loc in locations):
                self.ships.append(locations)
                self.ship_sizes_placed.append(ship_size) # Aquí se guarda el tamaño
                return True
        return False

    def place_all_ships(self, ship_sizes):
        """Coloca todos los barcos de los tamaños especificados."""
        for size in ship_sizes:
            if not self.place_ship(size):
                raise Exception(f"No se pudo colocar un barco de tamaño {size}") # Esto es para un manejo de errores más robusto

    def update(self, row, col, result):
        """Actualiza una celda del tablero con el resultado del disparo."""
        self.grid[row][col] = result

    def display(self):
        """Muestra el tablero en la consola."""
        print("  " + " ".join(map(str, range(self.size))))
        for i, row in enumerate(self.grid):
            print(f"{i} {' '.join(row)}")

    def check_hit(self, row, col):
        """Verifica si un disparo impactó en algún barco."""
        for ship in self.ships:
            if (row, col) in ship:
                ship.discard((row, col))
                return True
        return False

    def all_ships_sunk(self):
        """Verifica si todos los barcos han sido hundidos."""
        return all(not ship for ship in self.ships)
    

    def display_ships(self):
        """Muestra el tablero con la ubicación de los barcos revelada."""
        revealed_grid = [['~' for _ in range(self.size)] for _ in range(self.size)]
        for i, ship in enumerate(self.ships):
            ship_size = self.ship_sizes_placed[i]
            marker = str(ship_size)
            for r, c in ship:
                revealed_grid[r][c] = marker
        print("  " + " ".join(map(str, range(self.size))))
        for i, row in enumerate(revealed_grid):
            print(f"{i} {' '.join(row)}")