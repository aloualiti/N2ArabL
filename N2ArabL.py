from __future__ import unicode_literals # الكتابة باللغة العربية
def nTol(num):
    numdict = {}
    numdict[0] = 'صفر'
    numdict[1] = 'واحد'
    numdict[2] = 'إثنان'
    numdict[3] = 'ثلاثة'
    numdict[4] = 'أربعة'
    numdict[5] = 'خمسة'
    numdict[6] = 'ستة '
    numdict[7] = 'سبعة'
    numdict[8] = 'ثمانية'
    numdict[9] = 'تسعة'

 

    result=numdict.get(num, "اعتذر لم أتعلم بعد كتابة الأرقام الاكبر من 9")
           
    return result
x=0
while x<10:
    x= input (" : المرجو منكم ادخال رقم\n")
    print nTol(x)

    
