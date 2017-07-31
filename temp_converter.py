# Please modify the following program to now convert from input Fahrenheit
# to Celsius

def doConversion():
    tempInCAsString = input('Enter the temperature in Celsius: ')
    tempInC = int( tempInCAsString )
    tempInF = tempInC * 9 / 5 + 32
    print('The temperature in Fahrenheit is', tempInF, 'degrees')

for conversionCount in range( 3 ):
    doConversion()
