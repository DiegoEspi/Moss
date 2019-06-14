


from time import sleep
from machine import ADC
from machine import Pin

pin1=Pin(5,Pin.IN)
pin2=Pin(4,Pin.OUT)
adc = ADC(0)
l = []
c = 0
suma = 0
n = 0
pr2 = suma/15
pr1 = 0
while True:
  sleep(0.3)
  X=adc.read()
  print(X)
  if X>500:
    pin2.value(1)
  else:
    pin2.value(0)
  l.append(X)
  c = c + 1
  if c == 15:
    print (l)
    while n < 15:
      suma = suma + float(l[n])
      n = n + 1
    l = []
    c = 0
    print ("sumaaaaa", suma)
  if pr2 > pr1 and pr1 != 0:
    pin2.value(1)
  else:
    pin2.value(0)
  suma = pr2
  pr2 = pr1
  
  
