# A console program to convert celsius degrees to fahrenheit degrees and vice versa
# Konsoliohjelma celsius-asteiden muuntamiseksi fahrenheit-asteiksi ja päinvastoin

operations = [0, 1, 2]
again = True
selectAgain = ['k', 'K']

def intro():
    print('')
    print('ASTEMUUNNIN')
    print('Tämän ohjelman avulla voit muuttaa celsius-asteet fahrenheit-asteiksi tai päinvastoin')

def closure():
    print('Ohjelma lopetettu, kiitos kun käytit')
    print('')

def operationsInfo():
    print('')
    print('Toiminnot:')
    print('0 lopeta')
    print('1 celsius-asteista fahrenheit-asteiksi')
    print('2 fahrenheit-asteista celsius-asteiksi')
    print('')

def quitWithErrorMessage():
    print('Virheellinen syöte')
    quit()

def checkedDegrees(inp):
    try:
        asteet = float(inp)
        return asteet
    except ValueError:
        quitWithErrorMessage()

def getOperation(operations):
    operationsInfo()
    needInput = True
    while needInput:
        inp = input('Valitse haluamasi toiminto antamalla sitä vastaava numero: ').strip()
        if inp.isdigit():
            operation = int(inp)
            if operation in operations:
                needInput = False
        if needInput:
            print('Virheellinen syöte. ', end='')
    return operation
    
def celToFah(celsius):
    return (celsius * 1.8) + 32

def FahToCel(fahrenheit):
    return (fahrenheit - 32) / 1.8

def convert(operation):
    match operation:
        case 0:
            closure()
            quit()
        case 1:
            inp = input('Anna celsius-asteet: ')
            celsius_degrees = checkedDegrees(inp)
            result = celToFah(celsius_degrees)
            print(f'{celsius_degrees} celsius-astetta on {result:.2f} fahrenheit-astetta')
        case 2:
            inp = input('Anna fahrenheit-asteet: ')
            fahrenheit_degrees = checkedDegrees(inp)
            result = FahToCel(fahrenheit_degrees)
            print(f'{fahrenheit_degrees} fahrenheit-astetta on {result:.2f} celsius-astetta')

def checkAgain():
    global again
    print('')
    inp = input('Uudestaan? Anna k-kirjain ja paina Enter: ')
    if inp not in selectAgain:
        again = False

def main():
    intro()
    while again:
        operation = getOperation(operations)
        result = convert(operation)
        checkAgain()
    closure()

# PROGRAM START HERE
main()