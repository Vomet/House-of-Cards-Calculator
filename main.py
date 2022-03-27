def card_calc(num_layers):
  card_total = 0
  while num_layers > 0:
    card_total += (num_layers * 2) + (num_layers - 1)
    num_layers -= 1
  return card_total

def start():
  num_layers = input('Enter number of layers: ')
  try:
    num_layers = int(num_layers)
  except:
    print('Enter a number.')
    start()
  card_total = card_calc(num_layers)
  print(card_total)
  start()


print('Welcome to House of Cards Calculator!')
start()