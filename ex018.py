import math
an = float(input('Dígite o ângulo que você deseja: '))
seno = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan =math.tan(math.radians(an))
print('O ângulo de {:.3f} tem:'.format(an))
print('Seno:{:.3f}'.format(seno))
print('Cosseno:{:.3f}'.format(cos))
print('Tangente:{:.3f}'.format(tan))
