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

    numdict[1000000] = ' مليون '
    numdict[2000000] = ' مليونان '
        
    million= " ملايين "

    result=numdict.get(num)
    if result==None:
        numstr=str(num)
        lenstr=len(numstr)
        if lenstr==2:
            #0 to 99
            units=int(numstr[1])
            dozens=int(numstr[0])
            if dozens==1:
                return numdict[units] + " " + numdict[dozens*10]
            return numdict[units] + " و " + numdict[dozens*10]
        elif lenstr==3:
            # 0 to 999
            hundreds=int(numstr[0])
            restdozens=int(numstr[1:])
            return numdict[hundreds * 100] + " و " + nTol(restdozens)
        elif 7>lenstr>=4:
            # 0 to 999 999
            thousands=int(numstr[:-3])
            resthundreds=int(numstr[-3:])
            if thousands<=10:
                return numdict.get(thousands*1000, nTol(thousands) + millier) + " و "  + nTol(resthundreds)
            else:
                return nTol(thousands) + numdict[1000] + "و" + nTol(resthundreds)
        elif lenstr>=7:
            # 0 to 999 999 999
            millions=int(numstr[:-6])
            restthousands=int(numstr[-6:])
            if millions<=10:
                return numdict.get(millions*1000000, nTol(millions) + million) + " و "  + nTol(restthousands)
            else:
                return nTol(millions) + numdict[1000000] + "و" + nTol(restthousands)
            
    return result
x=0
while x<1000000000000:
    x= input (" : المرجو منكم ادخال رقم\n")
    print nTol(x)

    
