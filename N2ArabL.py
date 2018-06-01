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
 
    numdict[100] = 'مائة'
    numdict[200] = 'مائتان'
    numdict[300] = 'ثلاثمائة'
    numdict[400] = 'أربعمائة'
    numdict[500] = 'خمسمائة'
    numdict[600] = 'ستمائة'
    numdict[700] = 'سبعمائة'
    numdict[800] = 'ثمانمائة'
    numdict[900] = 'تسعمائة'

    numdict[1000] = ' ألف '
    numdict[2000] = ' ألفان '
    millier= " الاف "
    
    result=numdict.get(num)
    if result==None:
        numstr=str(num)
        lenstr=len(numstr)
        if lenstr==2:
            if int(numstr[0])==1:
                return numdict[int(numstr[1])] + " " + numdict[int(numstr[0])*10]
            return numdict[int(numstr[1])] + " و " + numdict[int(numstr[0])*10]
        elif lenstr==3:
            return numdict[int(numstr[0]) * 100] + " و " + nTol(int(numstr[1:]))
        elif lenstr>=4:
            if int(numstr[:-3])<=10:
                return numdict.get(int(numstr[:-3])*1000, nTol(int(numstr[:-3])) + millier) + " و "  + nTol(int(numstr[-3:]))
            else:
                return nTol(int(numstr[:-3])) + numdict[1000] + "و" + nTol(int(numstr[-3:]))
        

                  
    return result
x=0
while x<1000000:
    x= input (" : المرجو منكم ادخال رقم\n")
    print nTol(x)
    
print "اعتذر لم أتعلم بعد كتابة الأرقام الاكبر من 99999"    
