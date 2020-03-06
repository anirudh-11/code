import numpy as np

def main():
    midsem = np.random.randint(low = 0, high = 30, size  = 20)
    endsem = np.random.randint(low = 0, high = 50, size  = 20)
    assignment = np.random.randint(low = 0, high = 20, size  = 20)
    total = []
    for i in range(20):
        total.append(midsem[i] + endsem[i] + assignment[i])
        print("student - %d, midsem = %d, assignement = %d, endsem = %d, total = %d" %(i + 1, midsem[i], assignment[i], endsem[i], midsem[i] + assignment[i] + endsem[i]))
#     total = [20,
# 30,
# 40,
# 78,
# 70,
# 65,
# 65,
# 88,
# 87,
# 78,
# 76,
# 68,
# 45,
# 69,
# 93,
# 23,
# 45,
# 78,
# 97,
# 78
# ]
    mean = np.array(total).mean()
    minimum_passing_mark = 0.5 * mean
    passing_student_mean = np.array(list(filter((lambda num : num >= minimum_passing_mark), total))).mean()
    x = passing_student_mean - minimum_passing_mark
    s_cutoff = max(total) - 0.1 * (max(total) - passing_student_mean)
    y = s_cutoff - passing_student_mean
    a_cutoff = passing_student_mean + y * 5 / 8
    b_cutoff = passing_student_mean + y * 2 / 8
    c_cutoff = passing_student_mean - x * 2 / 8
    d_cutoff = passing_student_mean - x * 5 / 8
    e_cutoff = minimum_passing_mark
    print("Class avg is : ", mean)
    stu_grade = []
    grade_fr = {'S' : 0, 'A' : 0, 'B' : 0, 'C' : 0, 'D' : 0, 'E' : 0, 'U' : 0}
    for i in range(20):
        if(total[i] >= s_cutoff):
            grade = 'S'
        elif(total[i] >= a_cutoff):
            grade = 'A'
        elif(total[i] >= b_cutoff):
            grade = 'B'
        elif(total[i] >= c_cutoff):
            grade = 'C'
        elif(total[i] >= d_cutoff):
            grade = 'D'
        elif(total[i] >= e_cutoff):
            grade = 'E'
        else:
            grade = 'U'
        stu_grade.append({'Total' : total[i], 'Grade' : grade})
        grade_fr[grade] += 1
        print("Student {}, total = {}, grade = {}".format(i + 1, stu_grade[-1]['Total'], stu_grade[-1]['Grade']))

    print('\n')
    for key in grade_fr.keys():
        print("Frequency of grade {} is {}".format(key, grade_fr[key])) 

    print("\n")
    print("Class Mean = {}\nMinimum Passing Mark = {}\nPassing Student Mean = {}\nX = {}\nY = {}\nS_cutoff = {}\nA_cutoff = {}\nB_cutoff = {}\nC_cutoff = {}\nD_cutoff = {}\nE_cutoff = {}".format(mean, minimum_passing_mark, passing_student_mean, x, y, s_cutoff, a_cutoff, b_cutoff, c_cutoff, d_cutoff, e_cutoff))

if(__name__ == '__main__'):
    main()