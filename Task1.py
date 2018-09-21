
#This function should return sorted list of distinct elements of e
def unique(e):
	e = list(set(e))
	return(sorted(e))


#This function should return transposed dict d. It is garantueed that all the values of dict d are distinct.
def transposeDict(d):
  return {key: value for (value, key) in d.items()}



#This function should return minimal positive integer which is not present at list e.
def mex(e):
  return min([i for i in range(1, len(e)+5) if i not in e])

#This function should return dict with counts of every symbol from string s.
frequencyDict = lambda s: {el: s.count(el) for el in s}
