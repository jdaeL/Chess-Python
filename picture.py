from colors import inverter # Importa el diccionario de colores y su inversión

class Picture:
  def __init__(self, img):
    self.img = img                  # incializacion de 'img'


  def __eq__(self, other):
    return self.img == other.img    # compara si dos objetos Picture son iguales basándose en sus imágenes

  def _invColor(self, color):
    if color not in inverter:       # verifica si el color tiene un valor de inversión en el diccionario
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    vertical = self.img[::-1]       # invierte el orden de las filas en la imagen
    return Picture(vertical)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    horizontal = [row[::-1] for row in self.img]     # invierte el orden de los elementos en cada fila de la imagen
    return Picture(horizontal)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    negative = []
    for row in self.img:
        negative_row = ''.join(self._invColor(color) for color in row)  # invierte el color de cada elemento en la fila
        negative.append(negative_row)                                   # agrega la fila invertida a negative
    return Picture(negative) 

  def join(p1, p2):
    joined_img = [row + p2_row for row, p2_row in zip(p1.img, p2.img)]
    return Picture(joined_img)

  def up(self, p):
    return Picture(p.img + self.img)    # concatena las filas de la figura recibida y la figura actual

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    return Picture(self.img + p.img)    # concatena las filas de la figura actual y la figura recibida
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    repeated = [row * n for row in self.img]    # repite cada fila de la imagen 'n' veces
    return Picture(repeated)

  def verticalRepeat(self, n):
    repeated = self.img * n     # repite la imagen completa 'n' veces
    return Picture(repeated)    

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    rotated = [''.join(row[i] for row in self.img[::-1]) for i in range(len(self.img[0]))]  # rota la imagen 90 grados
    return Picture(rotated) 
    