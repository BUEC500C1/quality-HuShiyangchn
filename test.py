import Arabic2Roman as a2r

def test():
	assert a2r.intToRoman(2)=="II"
	assert a2r.intToRoman(4)=="IV"
	assert a2r.intToRoman(9)=="IX"
	assert a2r.intToRoman(20)=="XX"
	assert a2r.intToRoman(58)=="LVIII"
	assert a2r.intToRoman(1994)=="MCMXCIV"
