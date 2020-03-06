import numpy as np

def main():
    midsem = np.random.randint(low = 0, high = 30, size  = 20)
    endsem = np.random.randint(low = 0, high = 50, size  = 20)
    assignment = np.random.randint(low = 0, high = 20, size  = 20)
    total = []
    for i in range(20):
        total.append(midsem[i] + endsem[i] + assignment[i])
        print("student - %d, midsem = %d, assignement = %d, endsem = %d, total = %d" %(i + 1, midsem[i], assignment[i], endsem[i], midsem[i] + assignment[i] + endsem[i]))
    mean = np.array(total).mean()
    print("Class avg is : ", mean)
    stu_grade = []
    grade_fr = {'S' : 0, 'A' : 0, 'B' : 0, 'C' : 0, 'D' : 0, 'E' : 0}
    for i in range(20):
        if(total[i] < 0.5*mean):
            grade = 'E'
        elif(total[i] >= 90):
            grade = 'S'
        elif(total[i] >= 80):
            grade = 'A'
        elif(total[i] >= 70):
            grade = 'B'
        elif(total[i] >= 60):
            grade = 'C'
        else:
            grade = 'E'
        stu_grade.append({'Total' : total[i], 'Grade' : grade})
        grade_fr[grade] += 1
        print("Student {}, total = {}, grade = {}".format(i + 1, stu_grade[-1]['Total'], stu_grade[-1]['Grade']))

    print('\n')
    for key in grade_fr.keys():
        print("Frequency of grade {} is {}".format(key, grade_fr[key])) 

if(__name__ == '__main__'):
    main()