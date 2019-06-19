



from time import sleep
from machine import ADC
from machine import Pin

pin1=Pin(5,Pin.IN)
pin2=Pin(4,Pin.OUT)
adc = ADC(0)

l = []
a=0
c=0
suma=0
while True:
  sleep(0.3)
  X=adc.read()
  
  suma=X+suma
  l.append(X)
  c = c + 1
  
  if a == 1:
    pin2.value(1)
    sleep(0.5)
    pin2.value(0)
    sleep(0.5)
  
  if a==0:
    pin2.value(0)
  
  if c == 10:
    print (l)
    suma=(suma/10)
    print("El promedio es : ", suma)
    if suma > 150 :
      a=a+1
    suma=0
    l = []
    c = 0
  
  
  
  
  


