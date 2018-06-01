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

    numdict[10] = 'عشرة'
    numdict[11] = 'احدا عشر'
    numdict[12] = 'اثنا عشر'
  
    numdict[20] = 'عشرون'
    numdict[30] = 'ثلاثون'
    numdict[40] = 'أربعون'
    numdict[50] = 'خمسون'
    numdict[60] = 'ستون'
    numdict[70] = 'سبعون'
    numdict[80] = 'ثمانون'
    numdict[90] = 'تسعون'
 

    result=numdict.get(num)
    if result==None:
        numstr=str(num)
        lenstr=len(numstr)
        if lenstr==2:
            if int(numstr[0])==1:
                return numdict[int(numstr[1])] + " " + numdict[int(numstr[0])*10]
            return numdict[int(numstr[1])] + " و " + numdict[int(numstr[0])*10]
                  
    return result
x=0
while x<100:
    x= input (" : المرجو منكم ادخال رقم\n")
    print nTol(x)
    
print "9اعتذر لم أتعلم بعد كتابة الأرقام الاكبر من 9"    
