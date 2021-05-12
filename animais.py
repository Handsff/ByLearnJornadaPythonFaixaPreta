# Dei uma resumida na parte escrita
animais = []

animal = input('nome do animal ou 0 se nao tiver')

while animal != '0':
  especie = input('Digite a espécie: ')
  animais.append([animal, especie])
  animal = input('Se tiver mais animais, digite o nome dele. Ou 0 se não tiver: ')

if len(animais) == 0:
  print('\n\nVocê não tem animais')
else:
  print('\n\nvocê tem os seguintes animais')
  for animal in animais:
    print('- Nome:', animal[0], '| Espécie:', animal[1])
