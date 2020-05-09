import Arabic2Roman as a2r

def test():
	assert a2r.intToRoman(2)=="II"
	assert a2r.intToRoman(4)=="IV"
	assert a2r.intToRoman(9)=="IX"
	assert a2r.intToRoman(20)=="XX"
	assert a2r.intToRoman(58)=="LVIII"
	assert a2r.intToRoman(1994)=="MCMXCIV"
	assert a2r.intToRoman(77.77) == "Wrong type of input please type a integer number"
	assert a2r.intToRoman(-4257) == "The input is wrong"
	assert a2r.intToRoman(755) != "IDCLV"
	assert a2r.intToRoman(50001) == "The input is wrong"