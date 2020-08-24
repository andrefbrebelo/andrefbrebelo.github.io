import math
def choose_formula(movement,one_rm,high_Rep_weight,reps):
    epley = high_Rep_weight*(1+(reps/30))
    brzycki = high_Rep_weight*(1.0278-0.0278*reps)
    lombardi = high_Rep_weight*reps**0.10
    mcglothin = (100*high_Rep_weight)/(101.3-2.67123*reps)
    mayhew = 100*high_Rep_weight/(52.2 + 41.9*math.exp(-0.055*reps))
    oconner = high_Rep_weight * (1 + reps/40)
    wathen = 100 * high_Rep_weight / (48.8 + 53.8*math.exp(-0.075*reps))
    list_formulas = ['Epley','Brzycki','Lombardi','McGlothin','Mayhew',"O'Conner",'Wathen']
    difference_chart = [abs(epley-one_rm),abs(brzycki-one_rm),abs(lombardi-one_rm),abs(mcglothin-one_rm),abs(mayhew-one_rm),abs(oconner-one_rm),abs(wathen-one_rm)]
    minimum_deviance = difference_chart.index(min(difference_chart))
    return f'For the given {movement} numbers, the {list_formulas[minimum_deviance]} formula appears to be the most accurate.'

movement = str(input('Which kind of movement or lift would you like to analyze?:'))
one_rm = int(input('Please input your most recently tested 1RM:'))
high_Rep_weight = int(input('How much weight did you use for a recent high rep set?'))
reps = int(input('How many reps did you achieve at that weight?'))


print(choose_formula(movement,one_rm,high_Rep_weight,reps))