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
    for x in self.img:
       vertical.append(x[::-1])
    return Picture(vertical)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    horizontal = []
    for row in self.img:
        horizontal.insert(0, row)
    return Picture(horizontal)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    negative = [
       ''.join(self._invColor(char) for char in x)
       for x in self.img
    ]
    return Picture(negative) 

  def join(p1, p2):
    joined_img = [row + p2_row for row, p2_row in zip(p1.img, p2.img)]
    return Picture(joined_img)

  def up(self, p):
     image = self.img + p.img
     return Picture(image)

  def under(self, p):
    return Picture(self.img + p.img)    
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    image = []
    for i in range(0, len(self.img)):
        image.append(self.img[i] * n)
    return Picture(image)

  def verticalRepeat(self, n):
    image = self.img * n
    return Picture(image)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    rotated = [''.join(row[i] for row in self.img[::-1]) for i in range(len(self.img[0]))]  # rota la imagen 90 grados
    return Picture(rotated) 
  
  # SOBREPONER UNA PIEZA
  def sobreponer(self, p):
    image = []
    for i in range(len(self.img)):
        line = ""
        for j in range(len(self.img[i])):
            if p.img[i][j] != " ":
                line += p.img[i][j]
            else:
                line += self.img[i][j]
        image.append(line)
    return Picture(image)