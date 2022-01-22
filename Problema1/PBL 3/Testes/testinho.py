class Ponto():
	def __init__(self,x,y):
		self.x = (x)
		self.y = (y)

	def alterar_cord(self,valor_x,valor_y):
		self.x = (valor_x)
		self.y = (valor_y)
		
	def __repr__(self):
		return "({}, {})".format(self.x,self.y)

def main():
	pos1 = gerar_coord()
	save_pos1 = '{}'.format(pos1)
	editar_coord(pos1)
	pos2 = gerar_coord2()
	distancia = distancia_pontos(pos1,pos2)
	print('{}\n{}\n{}'.format(save_pos1,pos1,distancia))
	
def gerar_coord():
	xy_1 = input().split(',')
	pos1 = Ponto(xy_1[0],xy_1[1])
	return pos1

def editar_coord(pos1):
	xy_1 = input().split(',')
	pos1.alterar_cord(xy_1[0],xy_1[1])

def gerar_coord2():
	xy_2 = input().split(',')
	pos2 = Ponto(xy_2[0],xy_2[1])
	return pos2	
	
def distancia_pontos(pos1,pos2):
	dist = ((float(pos1.x)-float(pos2.x))**2+(float(pos1.y)-float(pos2.y))**2)**0.5
	return '{:.2f}'.format(dist)

if __name__ == '__main__':
	main()