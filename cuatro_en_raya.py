#Libreria para el menu del juego
from IPython.display import clear_output

class Cuatroenraya:
    """Inicializa el estado de la clase.
    filas -- int que determina el numero de filas del tablero
    columnas -- int que determina el numero de columnas del tablero"""

    def __init__(self, filas, columnas):
        self._filas = filas
        self._columnas = columnas
        self._tablero = self.crear_tablero()

    def crear_tablero(self):
        '''Metodo en el que se crea el tablero del juego.'''
        tablero = [None] * self._filas
        for i in range(self._filas):
            tablero[i] = ['.'] * self._columnas
        return tablero

    def mostrar_tablero(self):
        '''Metodo para mostrar el tablero por pantalla'''
        for num in range(self._columnas):
            print(num, end="  ")
        for fila in self._tablero:
            print('')
            for casilla in fila:
                print(casilla, end='  ')

    def introducir_ficha(self, columna, color):
        """Metodo para introducir fichas en el tablero

        color -- str que indica el color o simbolo
        columna -- int que indica en que columna se agregara la ficha"""
        if columna >= self._columnas or columna < 0:
            print("Error: Numero de columna equivocado")
            return
        elif self._tablero[0][columna] != ".":
            print("Error: columna llena")
            return
        else:
            for fila in range(self._filas-1, -1, -1):
                if self._tablero[fila][columna] == ".":
                    self._tablero[fila][columna] = color
                    return

    def revisar_filas(self, color):
        '''Metodo que comprueba si un jugador ha llenado 4 fichas en una fila
        
        color -- str que indica el color o simbolo'''
        num_filas = self._filas
        num_columna = self._columnas
        for r in range(num_filas):
            for c in range(num_columna - 3):
                if self._tablero[r][c] == color and self._tablero[r][c+1] == color and self._tablero[r][c+2] == color and self._tablero[r][c+3] == color:
                    return True
    def revisar_columnas(self, color):
        '''Metodo que comprueba si un jugador ha llenado 4 fichas en una columna
        
        color -- str que indica el color o simbolo'''
        num_filas= self._filas
        num_columna= self._columnas
        for c in range(num_columna):
            for r in range(num_filas - 3):
                if self._tablero[r][c] == color and self._tablero[r+1][c] == color and self._tablero[r+2][c] == color and self._tablero[r+3][c] == color:
                    return True
    def revisar_diagonal_derecha(self, color):
        '''Metodo que comprueba si un jugador ha llenado 4 fichas en una diagonal derecha
        
        color -- str que indica el color o simbolo'''
        num_filas= self._filas
        num_columna= self._columnas
        for c in range(num_columna - 3):
            for r in range(num_filas -1, 2, -1):
                if self._tablero[r][c] == color and self._tablero[r-1][c+1] == color and self._tablero[r-2][c+2] == color and self._tablero[r-3][c+3] == color:
                    return True
    def revisar_diagonal_izquierda(self, color):
        '''Metodo que comprueba si un jugador ha llenado 4 fichas en una diagonal izquierda
        
        color -- str que indica el color o simbolo'''
        num_filas= self._filas
        num_columna= self._columnas
        for c in range(num_columna -1, 2, -1):
            for r in range(num_filas -1, 2, -1):
                if self._tablero[r][c] == color and self._tablero[r-1][c-1] == color and self._tablero[r-2][c-2] == color and self._tablero[r-3][c-3] == color:
                    return True
    def comprobar_ganador(self, color):
        '''Comprueba si hay un cuatro en raya'''
        return self.revisar_filas(color) or self.revisar_columnas(color) or self.revisar_diagonal_derecha(color) or self.revisar_diagonal_izquierda(color)
    
    def jugar(self, player1= "x", player2= "o"):
        '''Metodo para jugar'''
        self._turno= player2
        while True:
            self._turno = player1 if self._turno == player2 else player2
            self.mostrar_tablero()
            columna= int(input("Turno del jugador: {}".format(self._turno)))
            self.introducir_ficha(columna, self._turno)
            clear_output(wait=False)
            if self.comprobar_ganador(self._turno):
                print("\n\nGanador el jugador {}!!\n\n".format(self._turno))
                self.mostrar_tablero()
                break