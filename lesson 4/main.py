# def func1(txturl):
#     count = 0
#     with open (txturl, 'r',encoding='utf-8') as f:
#         data = f.read()
#         words = data.split()
#         count += len(words)
#     print("Total Words:" ,count)


def func2(sublist):
    with open('myfile.csv', 'w', encoding='utf-8') as f:
        for item in sublist:
            # בדיקה האם האיבר הוא רשימה
            if isinstance(item, list):
                # המרת כל איבר ברשימה למחרוזת וחיבורם בפסיקים
                f.write(','.join(str(x) for x in item) + ',')
            else:
                # אם זה מחרוזת או מספר רגיל
                f.write(str(item) + ',')
        f.write('\n')


# func1(r'C:\Users\User\Desktop\year b\python\H.W\lesson 4\file.txt')

a = [[1.2,'a',3],[1.2,'w',4],[1.4,'q',2]]
func2(a)

