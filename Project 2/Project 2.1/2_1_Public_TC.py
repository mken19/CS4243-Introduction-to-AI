public_1 = {
    'domains' : {
        "A" : [1,2,3,4,5],
        "B" : [2,3,4,5,6],
        "C" : [3,4,5,6,7],
        "D" : [5,7,9,11,13]
    },
    'constraints' : {
        ("A", "B") : lambda a, b : a + b == 8 and a >= b,
        ("B", "C") : lambda b, c : b <= c / 2,
        ("C", "D") : lambda c, d : (c + d) % 2 == 0
    }
}
'''
Possible solution: {'A': 5, 'B': 3, 'C': 7, 'D': 5}
'''

public_2 = {
    'domains' : {
        "A" : [1,2,3,4,5,6,7,8,9,10],
        "B" : [1,2,3,4,5,6,7,8,9,10],
        "C" : [1,2,3,4,5,6,7,8,9,10],
        "D" : [1,2,3,4,5,6,7,8,9,10]
    },
    'constraints' : {
        ("A", "B") : lambda a, b : a * b < 50,
        ("A", "C") : lambda a, c : (a + c) % 10 == 0,
        ("A", "D") : lambda a, d : a + d > 10,
        ("B", "C") : lambda b, c : b > c // 3 and b < c,
        ("B", "D") : lambda b, d : (b + d) % 2 == 1,
        ("C", "D") : lambda c, d : (c % d) == 0 and c != d
    }
}
'''
Possible solution: {'A': 10, 'B': 4, 'C': 10, 'D': 1}
'''

public_3 = {
    'domains' : {
        "A" : [x for x in range(1,11)],
        "B" : [x for x in range(2,11,2)],
        "C" : [x for x in range(3,11,3)],
        "D" : [x for x in range(4,11,4)],
        "E" : [x for x in range(11)],
        "F" : [x for x in range(11)],
        "G" : [x for x in range(11)]
    },
    'constraints' : {
        ("A", "B") : lambda a, b : b % a == 0 and a != b,
        ("B", "C") : lambda b, c : c % b == 0 and b != c,
        ("C", "D") : lambda c, d : d % c == 0 and c != d,
        ("E", "F") : lambda e, f : e * f == f * e
    }
}
'''
Possible solution: None
'''

domains_4 = {
    '1': [108, 25, 128, 107, 144, 195, 117, 130, 188, 73, 163, 197, 79, 64, 113, 118, 106, 63, 193, 149, 8, 23, 119, 140,
       66, 19, 53, 115, 176, 174, 20, 40, 136, 57, 88, 120, 62, 137, 187, 22, 147, 83, 89, 21, 179, 177, 71, 27, 133,
       173, 2, 192, 30, 72, 178, 99, 84, 47, 74, 75, 109, 48, 145, 58, 182, 34, 37, 181, 3, 1, 138, 60, 17, 104, 123,
       110, 44, 129, 33, 35, 97, 70, 127, 54, 121, 92, 77, 194, 161, 167, 42, 124, 12, 67, 166, 169, 101, 189, 158, 185],
    '2': [26, 126, 55, 36, 104, 166, 2, 175, 152, 146, 71, 103, 76, 81, 119, 8, 111, 114, 106, 80, 46, 52, 139, 91, 102,
       93, 172, 75, 41, 115, 153, 170, 178, 45, 192, 12, 100, 120, 186, 190, 194, 37, 143, 176, 156, 157, 61, 62, 95,
       88, 65, 83, 110, 22, 137, 162, 151, 33, 66, 196, 4, 49, 199, 197, 28, 131, 159, 89, 96, 132, 59, 15, 169, 70,
       108, 86, 24, 79, 198, 129, 101, 58, 140, 16, 195, 9, 121, 150, 5, 181, 138, 118, 20, 107, 147, 109, 60, 14, 54, 48],
    '3': [76, 172, 181, 194, 93, 143, 22, 26, 166, 125, 102, 82, 191, 118, 65, 108, 70, 35, 188, 40, 51, 106, 111, 52, 37,
       160, 2, 5, 21, 89, 184, 105, 14, 139, 66, 134, 152, 83, 50, 28, 3, 39, 107, 71, 9, 18, 33, 55, 113, 30, 151, 7,
       81, 195, 147, 64, 31, 121, 90, 199, 135, 178, 200, 53, 20, 109, 187, 99, 63, 128, 13, 79, 198, 86, 104, 16, 146,
       193, 192, 189, 185, 136, 75, 110, 161, 162, 87, 154, 19, 129, 69, 123, 27, 142, 95, 77, 34, 156, 67, 173],
    '4': [158, 148, 142, 2, 193, 80, 122, 19, 191, 99, 3, 87, 197, 32, 17, 108, 137, 54, 168, 143, 79, 176, 94, 178, 174,
       41, 134, 160, 12, 43, 190, 116, 170, 141, 107, 125, 71, 35, 110, 150, 52, 132, 81, 128, 83, 47, 169, 185, 146,
       34, 14, 29, 109, 114, 74, 24, 119, 28, 1, 67, 96, 101, 155, 162, 145, 31, 144, 126, 7, 111, 84, 30, 70, 136, 124,
       4, 57, 167, 104, 68, 102, 48, 23, 63, 46, 91, 55, 39, 117, 147, 103, 183, 92, 85, 62, 56, 152, 10, 120, 58],
    '5': [63, 103, 41, 168, 189, 64, 15, 85, 107, 146, 114, 151, 163, 167, 112, 53, 98, 51, 60, 82, 195, 32, 16, 115, 187,
       99, 150, 162, 185, 29, 72, 94, 43, 142, 111, 159, 153, 198, 148, 70, 104, 182, 152, 18, 45, 136, 14, 188, 24, 90,
       139, 5, 173, 109, 110, 183, 73, 130, 181, 140, 56, 55, 74, 11, 10, 178, 156, 196, 134, 58, 193, 81, 54, 22, 174,
       179, 197, 93, 106, 124, 164, 75, 12, 149, 86, 157, 79, 33, 6, 95, 145, 154, 138, 199, 30, 8, 155, 27, 78, 68],
    '6': [25, 190, 93, 48, 137, 69, 49, 55, 139, 198, 14, 132, 200, 2, 163, 112, 135, 106, 125, 28, 75, 13, 156, 59, 63,
       165, 180, 197, 88, 104, 122, 72, 175, 5, 10, 100, 121, 62, 131, 80, 184, 32, 123, 166, 79, 57, 20, 99, 118, 1,
       29, 119, 24, 159, 40, 98, 7, 113, 56, 60, 41, 34, 109, 19, 105, 176, 151, 110, 101, 162, 76, 38, 46, 111, 21, 27,
       167, 58, 91, 188, 68, 47, 36, 115, 158, 15, 9, 31, 174, 117, 171, 64, 61, 3, 136, 43, 22, 192, 172, 152],
    '7': [16, 69, 58, 104, 15, 68, 22, 192, 84, 130, 155, 180, 46, 129, 87, 91, 65, 186, 190, 140, 171, 21, 132, 113, 47,
       80, 149, 156, 151, 141, 176, 27, 52, 164, 191, 99, 44, 125, 109, 177, 59, 35, 139, 143, 185, 193, 96, 118, 124,
       108, 30, 71, 114, 41, 67, 66, 181, 147, 17, 184, 162, 135, 20, 23, 75, 61, 100, 92, 1, 145, 105, 56, 188, 38, 34,
       74, 183, 158, 94, 2, 50, 26, 3, 86, 62, 122, 93, 60, 173, 119, 166, 78, 127, 152, 73, 40, 4, 79, 110, 121],
    '8': [19, 128, 181, 136, 36, 148, 195, 21, 3, 97, 49, 14, 189, 111, 80, 18, 28, 57, 192, 131, 182, 83, 34, 51, 191, 53,
       16, 67, 152, 41, 137, 171, 30, 42, 74, 101, 176, 29, 54, 112, 139, 123, 120, 47, 175, 17, 1, 24, 52, 141, 22, 56,
       90, 143, 199, 107, 130, 6, 31, 132, 168, 4, 104, 59, 149, 86, 122, 172, 127, 45, 114, 85, 133, 7, 102, 65, 40,
       118, 84, 162, 109, 2, 23, 197, 72, 92, 147, 12, 69, 32, 169, 8, 15, 68, 71, 35, 187, 150, 124, 140],
    '9': [107, 61, 157, 117, 17, 26, 7, 127, 96, 98, 100, 38, 140, 172, 101, 31, 79, 114, 10, 130, 161, 78, 189, 74, 48,
       192, 23, 39, 15, 118, 69, 158, 35, 86, 199, 93, 143, 163, 20, 149, 43, 132, 62, 168, 50, 92, 5, 53, 103, 12, 112,
       40, 47, 109, 25, 181, 58, 177, 180, 99, 169, 173, 156, 54, 170, 171, 84, 116, 45, 142, 81, 97, 57, 133, 60, 137,
       121, 175, 33, 111, 162, 136, 22, 190, 165, 134, 146, 52, 14, 151, 196, 94, 195, 91, 108, 41, 147, 49, 19, 150],
    '10': [16, 121, 127, 139, 120, 112, 194, 32, 129, 80, 7, 30, 151, 57, 49, 142, 74, 124, 148, 62, 48, 31, 53, 170, 65,
        43, 56, 64, 186, 39, 2, 37, 46, 162, 35, 149, 160, 152, 10, 8, 79, 55, 51, 23, 3, 164, 110, 161, 54, 197, 22,
        115, 91, 176, 167, 144, 78, 100, 90, 76, 153, 61, 190, 87, 106, 135, 131, 40, 159, 105, 41, 17, 44, 180, 50,
        107, 155, 99, 113, 29, 67, 4, 89, 200, 137, 96, 60, 28, 175, 38, 165, 150, 94, 174, 172, 179, 14, 177, 128, 191]
    }

constraints_4 = {
    ('4', '1'):  lambda x, y : (x * y) % 6 == 0,
    ('6', '10'): lambda x, y : (x + y) % 2 == 0,
    ('6', '3'):  lambda x, y : abs(x - y) < 50,
    ('4', '7'):  lambda x, y : abs(x - y) < 50,
    ('5', '4'):  lambda x, y : (x + y) % 2 == 0,
    ('8', '5'):  lambda x, y : abs(x - y) < 50,
    ('10', '5'): lambda x, y : (x % 10) > (y % 5),
    ('9', '4'):  lambda x, y : (x % 10) > (y % 5),
    ('2', '3'):  lambda x, y : (x % 10) > (y % 5),
    ('7', '9'):  lambda x, y : (x + y) % 2 == 0,
    ('3', '4'):  lambda x, y : (x + y) % 2 == 0,
    ('9', '6'):  lambda x, y : (x + y) % 2 == 1,
    ('10', '7'): lambda x, y : abs(x - y) < 50,
    ('5', '7'):  lambda x, y : (x + y) % 2 == 0,
    ('5', '2'):  lambda x, y : (x + y) % 2 == 1,
    ('1', '10'): lambda x, y : (x + y) % 2 == 0
}

public_4 = {
    'domains' : domains_4,
    'constraints' : constraints_4
}
'''
Possible solution: {'1': 108, '2': 26, '3': 181, '4': 19, '5': 63, '6': 190, '7': 15, '8': 19, '9': 107, '10': 16}
'''

public_5 = {
    'domains' : {
    '1' : [1,2,3,4,5,6,7,8,9],
    '2' : [1,2,3,4,5,6,7,8],
    '3' : [1,2,3,4,5,6,7],
    '4' : [1,2,3,4,5,6],
    '5' : [1,2,3,4,5],
    '6' : [1,2,3,4],
    '7' : [1,2,3],
    '8' : [1,2],
    '9' : [1]
    },
    'constraints' : {
        ('1', '2') : lambda x, y: x > y,
        ('2', '3') : lambda x, y: x > y,
        ('3', '4') : lambda x, y: x > y,
        ('4', '5') : lambda x, y: x > y,
        ('5', '6') : lambda x, y: x > y,
        ('6', '7') : lambda x, y: x > y,
        ('7', '8') : lambda x, y: x > y,
        ('8', '9') : lambda x, y: x > y,
    }
}
'''
Possible solution: {'1': 9, '2': 8, '3': 7, '4': 6, '5': 5, '6': 4, '7': 3, '8': 2, '9': 1}
'''

public_6 = {
    'domains' : {
        '1' : [5, 61, 77, 52, 32, 30, 36, 91, 80, 93],
        '2' : [41, 21, 39, 79, 86, 9, 89, 37, 7, 64], 
        '3' : [25, 44, 62, 27, 74, 59, 28, 59, 28, 8],
        '4' : [14, 89, 57, 29, 33, 1, 41, 26, 33, 20],
        '5' : [50, 26, 48, 2, 85, 48, 63, 53, 22, 87],
        '6' : [44, 57, 3, 13, 7, 76, 94, 53, 42, 39],
        '7' : [66, 7, 20, 79, 96, 16, 35, 55, 77, 50],
        '8' : [66, 63, 92, 99, 23, 29, 9, 82, 92, 98],
        '9' : [22, 67, 80, 66, 26, 16, 11, 99, 63, 40],
        '10' : [70, 54, 34, 78, 61, 4, 18, 78, 55, 18]
    },
    'constraints' : {
        ('1', '2') : lambda x, y : x + y == 68,
        ('3', '4') : lambda x, y : x + y == 41,
        ('5', '6') : lambda x, y : x + y == 107,
        ('7', '8') : lambda x, y : x + y == 25,
        ('9', '10') : lambda x, y : x + y == 169
    }
}
'''
Possible solution: {'1': 61, '2': 7, '3': 27, '4': 14, '5': 50, '6': 57, '7': 16, '8': 9, '9': 99, '10': 70}
'''

public_7 = {
    'domains' : {
        '0' : [5,4,3,2,1],
        '1' : list(range(1,1024)),
        '2' : list(range(1,1024)),
        '3' : list(range(1,1024)),
        '4' : list(range(1,1024)),
        '5' : list(range(1,1024)),
        '6' : list(range(1,1024)),
        '7' : list(range(1,1024)),
        '8' : list(range(1,1024)),
        '9' : list(range(1,1024)),
    },
    'constraints' : {
        ("0", "1") : lambda x, y : y % x == 0 and x != y,
        ("1", "2") : lambda x, y : y % x == 0 and x != y,
        ("2", "3") : lambda x, y : y % x == 0 and x != y,
        ("3", "4") : lambda x, y : y % x == 0 and x != y,
        ("4", "5") : lambda x, y : y % x == 0 and x != y,
        ("5", "6") : lambda x, y : y % x == 0 and x != y,
        ("6", "7") : lambda x, y : y % x == 0 and x != y,
        ("7", "8") : lambda x, y : y % x == 0 and x != y,
        ("8", "9") : lambda x, y : y % x == 0 and x != y
    }
}
'''
Possible solution: {'0': 1, '1': 2, '2': 4, '3': 8, '4': 16, '5': 32, '6': 64, '7': 128, '8': 256, '9': 512}
'''