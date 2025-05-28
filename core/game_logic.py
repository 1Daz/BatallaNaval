import random
from .board import Board

class Game:
    def __init__(self, board_size=5):
        self.board = Board(board_size)
        self.ship_sizes = self._generate_ship_sizes(min_total_size=6, max_total_size=9, possible_sizes=[1, 2, 3])
        self.board.place_all_ships(self.ship_sizes)
        self.attempts = 0

    def _generate_ship_sizes(self, min_total_size, max_total_size, possible_sizes):
        ship_sizes = []
        current_total_size = 0
        while current_total_size < min_total_size:
            possible_additions = [size for size in possible_sizes if current_total_size + size <= max_total_size]
            if not possible_additions:
                break
            ship_size = random.choice(possible_additions)
            ship_sizes.append(ship_size)
            current_total_size += ship_size

        while current_total_size < max_total_size and random.random() < 0.7:
            possible_additions = [size for size in possible_sizes if current_total_size + size <= max_total_size]
            if not possible_additions:
                break
            ship_size = random.choice(possible_additions)
            ship_sizes.append(ship_size)
            current_total_size += ship_size

            if len(ship_sizes) > 7:
                break

        total_size = sum(ship_sizes)
        while total_size < min_total_size:
            possible_additions = [size for size in possible_sizes if total_size + size <= max_total_size]
            if not possible_additions:
                break
            add_size = random.choice(possible_additions)
            ship_sizes.append(add_size)
            total_size += add_size
        while total_size > max_total_size and ship_sizes:
            largest_ship_size = max(ship_sizes)
            ship_sizes.remove(largest_ship_size)
            total_size -= largest_ship_size
            if total_size < min_total_size and [s for s in possible_sizes if total_size + s <= max_total_size]:
                add_size = random.choice([s for s in possible_sizes if total_size + s <= max_total_size])
                ship_sizes.append(add_size)
                total_size += add_size

        final_total_size = sum(ship_sizes)
        if not (min_total_size <= final_total_size <= max_total_size):
            return self._generate_ship_sizes(min_total_size, max_total_size, possible_sizes)

        return ship_sizes

    def process_guess(self, row, col):
        """Procesa un intento de disparo del jugador."""
        if not (0 <= row < self.board.size and 0 <= col < self.board.size):
            return "¡Coordenadas fuera del tablero!"

        if self.board.grid[row][col] != '~':
            return "¡Ya disparaste a esta coordenada!"

        self.attempts += 1
        hit = self.board.check_hit(row, col)
        if hit:
            self.board.update(row, col, '*')
            ship_sunk = False
            for ship in self.board.ships:
                if not ship:
                    self.board.update(row, col, '*') # Marca en el tablero como hundido
                    ship_sunk = True
                    break
            if ship_sunk:
                return "¡Hundiste un barco!"
            else:
                return "¡Impacto!"
        else:
            self.board.update(row, col, 'X')
            return "¡Agua!"

    def get_board_display(self):
        """Obtiene la representación visual del tablero."""
        return self.board.display()

    def has_won(self):
        """Verifica si el jugador ha ganado (todos los barcos hundidos)."""
        return self.board.all_ships_sunk()

    def get_attempts(self):
        """Obtiene el número de intentos realizados."""
        return self.attempts