def intToRoman(num):
    basenum={
        0:("","I","II","III","IV","V","VI","VII","VIII","IX"),
        1:("","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"),
        2:("","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"),
        3:("","M","MM","MMM","MMMM","MMMMM","MMMMM","MMMMMM","MMMMMMMM","MMMMMMMMM","MMMMMMMMMM")
    }
    romannum=[]
    romannum.append(basenum[3][num/1000%10])
    romannum.append(basenum[2][num/100%10])
    romannum.append(basenum[1][num/10%10])
    romannum.append(basenum[0][num%10])
    result=""
    for i in romannum:
        result=result+i
    return result
