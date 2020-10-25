def nd_consistency(d):
	temp = []
	for k,v in d.items():
		temp += [v for v in v]
	temp_d = {i:temp.count(i) for i in temp}
	max_val = max(temp_d.values())
	if all(value == max_val for value in temp_d.values()):
		return True
	else:
		return False
