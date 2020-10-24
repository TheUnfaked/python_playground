def nd_consistency(d):
	counter = 0
	temp = []
	for k,v in d.items():
		temp += [v for v in v]
		counter += 1
	temp_d = {i:temp.count(i) for i in temp}
	if all(value == counter for value in temp_d.values()):
		return True
	else:
		return False
