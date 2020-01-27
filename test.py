import Arabic2Roman as a2r

def test():
	assert a2r.Arabic2Roman(2)=="II"
	assert a2r.Arabic2Roman(4)=="IV"
	assert a2r.Arabic2Roman(9)=="IX"
	assert a2r.Arabic2Roman(20)=="XX"
	assert a2r.Arabic2Roman(58)=="LVIII"
	assert a2r.Arabic2Roman(1994)=="MCMXCIV"
