score = 0
def AgeCalculation(age):
    global score
    if age < 40 :
        score += 0
    elif age >= 40 and age < 60 :
        score += 7
    elif age >= 60 and age < 70 :
        score += 12
    elif age >= 70 and age < 75 :
        score += 15
    elif age >= 75 and age < 80 :
        score += 16
    elif age >= 80 :
        score += 18
        
    return score
        
def HRCalculation(hr):
    global score
    if hr < 40 : 
        score += 11
    elif hr >= 40 and hr < 70 :
        score += 2
    elif hr >= 70 and hr < 120 :
        score += 0
    elif hr >= 120 and hr < 160 :
        score += 4
    elif hr >= 160 :
        score += 7

    return score
        
def BPCalculation(bp):
    global score
    if bp < 70 :
        score += 13
    elif bp >= 70 and bp < 100 :
        score += 5
    elif bp >= 100 and bp < 200 :
        score += 0
    elif bp >= 200 :
        score += 2

    return score

def TPCalculation(tp):
    global score
    if tp >= 39 :
        score += 3
    elif tp < 39 :
        score += 0

    return score
        
def GCSCalculation(gcs):
    global score
    if gcs >= 14 and gcs <= 15:
        score += 0
    elif gcs >= 11 and gcs <= 13:
        score += 5
    elif gcs >= 9 and gcs <= 10:
        score += 7
    elif gcs >= 6 and gcs <= 8:
        score += 13
    elif gcs < 6 :
        score += 26
        
    return score

# def Pao2Calculation(pao2):
  
def BUNCalculation(bun):
    global score
    if bun == 'BUN':
        if bun < 28 :
            score += 0
        elif bun >= 28 and bun < 84 :
            score += 6
        elif bun >= 84 :
            score += 10         
    elif bun == 'urea':
        if bun < 10 :
            score += 0
        elif bun >= 10 and bun < 30 :
            score += 6
        elif bun >= 30 :
            score += 10
    
    return score
            
def UrineCalculation(uo):
    global score
    if uo < 500 :
        score += 11
    elif uo >= 500 and uo < 1000 :
        score += 4 
    elif uo >= 1000 :
        score += 0
   
    return score
        
def NaCalculation(na):
    global score
    if na < 125 :
        score += 5
    elif na >= 125 and na < 145 :
        score += 0
    elif na >= 145 :
        score += 1    
    
    return score

def PotassiumCalculation(pota):
    global score
    if pota < 3.0 :
        score += 3
    elif pota >= 3.0 and pota < 5.0 :
        score += 0
    elif pota >= 5 :
        score += 3

    return score

def BicarbonateCalculation(bicar):
    global score
    if bicar < 15 :
        score += 6
    elif bicar >= 15 and bicar < 20 :
        score += 3
    elif bicar >= 20 :
        score += 0

    return score

def BilirubinCalculation(bil):
    global score
    if bil < 4.0 :
        score += 0
    elif bil >= 4.0 and bil < 6.0 :
        score += 4
    elif bil >= 6.0 :
        score += 9

    return score
        
def WBCCalculation(wbc):
    global score
    if wbc < 1 :
        score += 12
    elif wbc >= 1 and wbc < 20 :
        score += 0
    elif wbc >= 20 :
        score += 3
        
    return score

def Chronic_disease(num):
    global score
    if num == 0 :
        score += 0 
    elif num == 1 :
        score += 9
    elif num == 2 :
        score += 10
    elif num == 3 :
        score += 17

    return score
    
def Type_of_admission(num):
    global score
    if num == 0 :
        score += 0
    elif num == 1 :
        score += 6
    elif num == 2 :
        score += 8
    
    return score

age = int(input('1. Age, years : '))
AgeCalculation(age)

hr = int(input('2. Heart rate : '))
HRCalculation(hr)

bp = int(input('3. systolic BP,mm Hg : '))
BPCalculation(bp)

tp = int(input('4. Temperature ≥39ºC (102.2ºF) : '))
TPCalculation(tp)

gcs = int(input('5. GCS : '))
GCSCalculation(gcs)

# pao2 = int(input('6. PaO₂/FiO₂, if on mechanical ventilation or CPAP : '))
# pao2Calculation(pao2)

bun = float(input('7. BUN, mg/dL (serum urea, mmol/L) : '))
BUNCalculation(bun)

uo = float(input('8. Urine output, mL/day : '))
UrineCalculation(uo)

na = float(input('9. Sodium, mEq/L or mmol/L : '))
NaCalculation(na)

pota = float(input('10. Potassium, mEq/L : '))
PotassiumCalculation(pota)

bicar = float(input('11. Bicarbonate, mEq/L : '))
BicarbonateCalculation(bicar)

bil = float(input('12. Bilirubin : '))
BilirubinCalculation(bil)

wbc = float(input('13. WBC, x 10³/mm³ : '))
WBCCalculation(wbc)

disease = int(input('14. Choose one \n1) None 2) Metastatic cancer 3) Hematologic malignancy 4) AIDS\n:'))
Chronic_disease(disease)

admission = int(input('15. Choose one \n1) Scheduled surgical 2) Medical 3) Unscheduled surgical\n:'))
Type_of_admission(admission)

