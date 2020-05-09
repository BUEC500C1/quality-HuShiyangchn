def intToRoman(num):
    if not isinstance(num,int):
        return "Wrong type of input please type a integer number"
    basenum={
        0:("","I","II","III","IV","V","VI","VII","VIII","IX"),
        1:("","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"),
        2:("","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"),
        3:("","M","MM","MMM","MMMM","MMMMM","MMMMM","MMMMMM","MMMMMMMM","MMMMMMMMM","MMMMMMMMMM")
    }
    romannum=[]
    romannum.append(basenum[3][int(num/1000%10)])
    romannum.append(basenum[2][int(num/100%10)])
    romannum.append(basenum[1][int(num/10%10)])
    romannum.append(basenum[0][int(num%10)])
    result=""
    if num > 0 and num < 5000:
        for i in romannum:
            result=result+i
    else:
        return "The input is wrong"

    return result

print(intToRoman(25))