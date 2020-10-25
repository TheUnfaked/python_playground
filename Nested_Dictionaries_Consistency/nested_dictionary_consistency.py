def nd_consistency(d):
	temp = []
	for i in d.values():
		if temp == []:
			temp = [i for i in i]
		else:
			for j in i:
				if j not in temp:
					return False
	temp = []
	for k,v in d.items():
		temp += [v for v in v]
	temp_d = {i:temp.count(i) for i in temp}
	max_val = max(temp_d.values())
	if all(value == max_val for value in temp_d.values()):
		return True
	else:
		return False
