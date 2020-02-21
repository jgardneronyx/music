def build_scale(scale,index_start,notes,scale_result):
	scale_index = 0
	for i in range(len(scale)-1):
		scale_index += scale[i]
		if scale_index + index_start > 11:
			scale_index = scale_index - 12
		scale_result.append(notes[index_start+scale_index])

def build_chord(interval,scale_result,chord_result):
	index_start = 0
	scale_index = 0

	for i in range(len(interval)):
		scale_index += interval[i]
		if scale_index + index_start >6:
			scale_index = scale_index - 7
		chord_result.append(scale_result[index_start+scale_index])

def converter(minor,major,triad,seventh):

	for i in range(8):
		minor[i] = int(minor[i])
		major[i] = int(major[i])

	for i in range(3):
		triad[i] = int(triad[i])
	for i in range(4):
		seventh[i] = int(seventh[i])
'''
def converter_dict(minor,major,phyrgian,lydian,mixolydian,locrian):

	for i in range(8):
		minor[i+1] = int(minor[i+1])
		major[i+1] = int(major[i+1])
		phyrgian[i+1] = int(phyrgian[i+1])
		lydian[i+1] = int(lydian[i+1])
		mixolydian[i+1] = int(mixolydian[i+1])
		locrian[i+1] = int(locrian[i+1])
'''

	
