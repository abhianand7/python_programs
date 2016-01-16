def tuples():
    student_tuples = [
            ('john', 'A', 15),
            ('jane', 'B', 12),
            ('dave', 'B', 10),
    ]
    var = sorted(student_tuples, key=lambda var1: var1[2])   # sort by age
    print (var)