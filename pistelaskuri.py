# REFEREE POINTS CALCULATOR
# A program to calculate referee points for one performance
# Points from each referee are entered and total points are calculated
# Default values are for calculating ski jumping style points

# Functional constants with default values
ref_points_min = 0
ref_points_max = 20
point_interval = 0.5 # Positive number
referees_total = 5 # Min 1
popWorstAndBest = True # True has effect if referees_total is min 3

# Secure working functional constants
point_interval = abs(point_interval)
if referees_total < 1:
    referees_total = 1
if referees_total < 3:
    popWorstAndBest = False

# Message constants
# Here in Finnish
programNameInfo = 'TUOMARIPISTEIDEN LASKURI'
pointsInfo = 'Pistetyyppi: mäkihypyn tyylipisteet' # Type of sports and points, here style points in ski jumping
descriptionInfo = (f'Otetaan vastaan {referees_total} tuomarin pisteet ja lasketaan suorituksen kokonaispisteet') # Program description
quitInfo = 'Paina Enter, jos haluat keskeyttää.' # Press Enter to quit the program
inputInfo = 'Suorituksen pisteet, tuomari nro' # When asking referee points
inputErrorInfo = (f'Virheellinen syöte. {quitInfo}')
pointsErrorInfo = (f'Pisteiden oltava {ref_points_min}-{ref_points_max} ja {point_interval} pisteen tarkkuudella. {quitInfo}') # When error in points range or interval
pointsTotalInfo = 'Pisteet yhteensä:'

# General variables
style_points = []
refereeNo = 1

def intro():
    print(programNameInfo)
    print(pointsInfo)
    print(descriptionInfo)
    print(quitInfo)

def isCorrectPoints(ref_points):
    correctRange = (ref_points >= ref_points_min) and (ref_points <= ref_points_max)
    residual = ref_points % point_interval
    correctInterval = (residual == 0) or (round(residual, 10) == point_interval)
    return correctRange and correctInterval

def getRefereePoints():
    global refereeNo
    while refereeNo <= referees_total:
        inp = input(f'{inputInfo} {refereeNo}: ')
        if inp == '':
            quit()
        try:
            ref_points = float(inp)
        except ValueError:
            print(inputErrorInfo)
            continue
        if isCorrectPoints(ref_points):
            style_points.append(ref_points)
            refereeNo += 1
        else:
            print(pointsErrorInfo)

def pointsPopper():
    style_points.sort()
    last_index = len(style_points) - 1
    style_points.pop(last_index)
    style_points.pop(0)

def main():
    intro()
    getRefereePoints()
    if popWorstAndBest:
        pointsPopper()
    result_points = sum(style_points)
    print(f'{pointsTotalInfo} {result_points:.1f}')

# PROGRAM START HERE
main()