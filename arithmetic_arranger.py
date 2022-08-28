import re
import math

#split işlemindeki indeks sayıları
firstNumIndex = 0
operatorIndex = 1
secondNumIndex = 2

#sayıların maksimum karakter sayısı
maxDigit = 4
#işlemler arası boşluk sayısı
spacePerProblem = 4

def arithmetic_arranger(problems, sol=False):
  count = 1
  #cevaplanıp cevaplanmayacağını kontrol eder
  answer = False

  if sol:
    #problems = problems[0]
    answer = True
  
  #soruları tek tek saklamak için boş liste tanımı
  splitQuestion = []
  splitQuestion.clear()
  #her işlem için iki sayı arasındaki en fazla karakterli olan sayının basamak sayısını tutan liste
  maxDigitEachProblem = []
  maxDigitEachProblem.clear()
  #sırasıyla işlemleri saklayacak boş liste tanımı
  operators = []
  operators.clear()
  #her satır için boş liste
  section1 = ["  "] # her zaman ilk iki karakter boşluk
  section2 = []     # ilk karakter operatör ile başlayacak
  section3 = ["--"] # her zaman ilk iki karakter "-"
  section4 = []
  
  #problem sayısı hata kontrolü
  if len(problems) >= 6:
    return "Error: Too many problems."

  for question in problems:
    '''
    split işlemi
    1. split ilk sayı    - splitQuestion [0] - firstNumIndex
    2. split işlem       - splitQuestion [1] - operatorIndex
    3. split ikinci sayı - splitQuestion [2] - secondNumIndex
    '''
    splitQuestion = re.split("\s", question)

    #sayıların sayı olup olmaması kontrolü
    if not splitQuestion[secondNumIndex].isdigit() \
    or not splitQuestion[firstNumIndex].isdigit():
      return "Error: Numbers must only contain digits."

    #dört basamaktan büyük sayı hata kontrolü
    num1 = int(splitQuestion[firstNumIndex])
    num2 = int(splitQuestion[secondNumIndex])
    num1Digit = howManyDigit(num1)
    num2Digit = howManyDigit(num2)
    if num1Digit > maxDigit or num2Digit > maxDigit:
      return "Error: Numbers cannot be more than four digits."

    #sırasıyla her işlem için maksimum basamağa sahip sayının basamağını saklar
    maxDigitEachProblem = max(num1Digit, num2Digit)
      
    #operatör hata kontrolü
    operator = splitQuestion[operatorIndex]
    #if not splitQuestion[operatorIndex] in ("+","-"):
      

    if operator == '+':
      solution = num1 + num2
    elif operator == '-':
      solution = num1 - num2
    else:
      return "Error: Operator must be '+' or '-'."
    solutionDigit = howManyDigit(solution)
    
    section1.append(" " * (maxDigitEachProblem - num1Digit))
    section1.append(str(num1))
    section2.append(operator)
    section2.append(" ")
    section2.append(" " * (maxDigitEachProblem - num2Digit))
    section2.append(str(num2))
    section3.append("-" * maxDigitEachProblem)
    section4.append(" " * ((maxDigitEachProblem + 2) - solutionDigit))
    section4.append(str(solution))
    
    if count < len(problems):
      section1.append(" " * spacePerProblem)
      section1.append("  ")
      section2.append(" " * spacePerProblem)
      section3.append(" " * spacePerProblem)
      section3.append("--")
      section4.append(" " * spacePerProblem)
      
    section1Final = "".join(section1)
    section2Final = "".join(section2)
    section3Final = "".join(section3)
    section4Final = "".join(section4)
    count = count + 1

  if answer == True:
    return section1Final + "\n" + section2Final + "\n" + section3Final + "\n" + section4Final
  return section1Final + "\n" + section2Final + "\n" + section3Final

#basamak sayısını döndüren fonksiyon
def howManyDigit(number):
  if number > 0:
    digits = int(math.log10(number))+1
  elif number == 0:
    digits = 1
  elif number < 0:
    digits = int(math.log10(-number))+2
  return digits