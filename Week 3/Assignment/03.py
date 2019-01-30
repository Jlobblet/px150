def mean_rms_file(flnm):
	opfile = open(flnm,"r")
	data = list(())
	for line in opfile:
		data.append(float(line[:-1]))#eliminates \n on each line
	opfile.close()
	mean = 0
	for i in data:
		mean += i
	mean = mean/len(data)
	variance = 0
	for i in data:
		variance += (i - mean)**2/len(data)
	rms = (variance+mean**2)**0.5
	return tuple((mean,rms))