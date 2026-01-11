def calc_homework(hwassarg):
    sum_of_grades = 0
    for homework in hwassarg.values():
        sum_of_grades += homework
    final_grade = round(sum_of_grades / len(hwassarg),2)
    print(final_grade)

