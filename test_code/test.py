def calculate_circle(radius):
    area = 3.14159 * (radius ** 2)
    circumference = round((2 * 3.14159 * radius),2) # round ใช้เลือกเศษทศนิยม เลข 2 ด้านหลังสุดคือการบอกว่าเอาทศนิยม 2 ตำแหน่ง
    return area,circumference

def analyze_scores(scores):
    total = sum(scores)
    average = total / (len(scores))
    highest = max(scores)
    lowest = min(scores)
    scores_pass = []
    for i in range (len(scores)):
        if scores[i] >= 70:
            scores_pass.append(scores[i])
    book_score = {"total":total,"average":average,"highest":highest,"lowest":lowest,"scores_pass":scores_pass}
    return book_score

def count_vowels_consonants(text):
    new = text.upper().replace(" ", "") # แทนที่ หา " " แทนที่โดยการไม่ว่าง
    new = list(new)
    return new
    
def count_vowels_consonants(text):
    new = text.upper().replace(" ", "") # แทนที่ หา " " แทนที่โดยการไม่ว่าง ""
    new = list(new)
    vowels = 0
    consonants_counts = 0
    
    for i in range(len(new)):
        if new[i].isdigit():
            continue
        elif new[i] == "A" or new[i] == "E" or new[i] == "I" or new[i] == "O" or new[i] == "U":
            vowels += 1
        else:
            consonants_counts += 1
        
    return vowels,consonants_counts
e,i =  count_vowels_consonants("Hello world")
print(e,i)
