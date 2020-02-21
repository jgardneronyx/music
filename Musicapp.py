# when creating diatonic harmonies we can just add major or minor thirds 
# from the root and the second note. The choice of interval is simple.
# chose an interval that keeps you in the parent scale. 
# For example C D E F G A B is the Cmaj Scale. The ii chord is Dmin
# A minor 3rd brings us to F and a major 3rd brings us to A 

import key_modules as km
# unix pipelines
def INSTRUCTIONS():
	print("<< THE SCALE CONSTRUCTOR PROGRAM >>\n")
	print("This program builds a scale around a particular note ")
	print("The user will provide the note of their choice ")
	print("As well as the scale type.\n ")
	print("USER INPUT HELP")
	print("---------------\n")
	print("1.Chosing a Scale")
	print("Enter scale choice as follows\n")
	print("'Major','Minor','Dorian','Phyrgian','Lydian','Mixolydian','Locrian'")
	print("For Pentatonic scales chose 'Pentatonic(M) or Pentatonic(m)\n")
	print("2.Chose note to build scale around C, Ab,..etc")
	print("The program will now build your chosen scale and harmonize it :)\n")

def get_scale_type():
	s_types = ['Major','Minor','Dorian','Phyrgian','Lydian','Mixolydian','Locrian','Pentatonic(M)','Pentatonic(m)']
	scale_type = 0
	while scale_type not in s_types:
		scale_type = input("Please enter choice for scale type: ")
		if scale_type not in s_types:
			print("NOT A VALID SCALE")
	return scale_type


def get_key(notes):
	key = ' '
	while key not in notes:
		key = input("Please enter key to start with: ")
		if key not in notes:
			print("Please enter valid note")

	return key

def main():

	with open("outfile.txt") as file:
		
		members = file.readlines(); # adding each line of file to a list

		# making each element of 'members' list into a list itself; previously they were str
		major_notes = list(members[0].replace("\n","").split(',')) 
		minor_notes = list(members[1].replace("\n","").split(','))
		major = list(members[2].replace("\n","").split(','))
		minor = list(members[3].replace("\n","").split(','))
		triad = list(members[4].replace("\n","").split(','))
		seventh = list(members[5].replace("\n","").split(','))
		
		#converting str objects in major, minor, and dorian into int objects
		km.converter(minor,major)
			
		print("\n")
		INSTRUCTIONS()

		again = 'y'
	while again == 'y':

	# creating list objects for use
		scale_result = []
		chord_result = []
		harmony_triad = []
		harmony_seventh = []
	# user choses type of scale they would like to build

		scale_type = get_scale_type()
				# un-generalizng
		if scale_type == 'Major':
			notes = major_notes 
			scale = major

		elif scale_type == 'Minor':
			notes = minor_notes
			scale = minor
		
		elif scale_type == 'Dorian':
			notes = minor_notes
			scale = minor
			minor[5] = 2
			minor[6] = 1

		elif scale_type == 'Phyrgian':
			notes = minor_notes
			scale = minor
			minor[1]= 1
			minor[2] = 2
		
		elif scale_type == 'Lydian':
			notes = major_notes
			scale = major
			major[3] = 2
			major[4] = 1

		elif scale_type == 'Mixolydian':
			notes = major_notes
			scale = major
			major[6] = 1
			major[7] = 2

		elif scale_type == 'Locrian':
			notes = minor_notes
			scale = minor
			minor[1] = 1
			minor[2] = 2
			minor[5] = 2
			minor[4] = 1

		# Remember list changes length after pop so need to update index choice

		elif scale_type == 'Pentatonic(M)':
			notes = major_notes
			scale = major
			major.pop(4)
			major.pop(6)
			major[3] = 3


		elif scale_type == 'Pentatonic(m)':
			notes = minor_notes
			scale = minor
			minor.pop(2)
			minor.pop(5)
			minor[1] = 3
			minor[4] = 3

		else:
			print("DO NOTHING")

		# user now choses note to build scale around, also used as index 
		key = get_key(notes)
		
		# converting key into int so we can use as index
		index_start = notes.index(key)
		
		#building scale	
		km.build_scale(scale,index_start,notes,scale_result)


		
		#formatting output scale(s) + chord(s)
		print("The " + key , " "+ scale_type," Scale is \n" )
		for item in scale_result:
			print(item, end = ' ')
		print("\n")

		
		# building harmonies 
		if scale_type == 'Major':
			km.build_harmony(scale_result,harmony_triad,harmony_seventh)
			print("The harmonization of the " + key, " "+ scale_type," Scale in triad chords is \n")
			harmonization_order= ['Maj','min','min','Maj','Maj','min','dim']
			ho_index = 0
			sc_index = 0

			for item in harmony_triad:
				print(scale_result[sc_index], harmonization_order[ho_index])
				ho_index += 1
				sc_index += 1
				for note in item:
					print(note, end = ' ')
				print('\n')

			print("The harmonization of the " + key, " "+ scale_type," Scale in seventh chords is \n")
			ho_index = 0
			sc_index  =0
			for item in harmony_seventh:
				print(scale_result[sc_index], harmonization_order[ho_index], "7")
				ho_index += 1
				sc_index += 1
				for note in item:
					print(note, end = ' ')
				print('\n')



		again = input("Would you like to build another scale(y/n): ")

if __name__ == '__main__':
	main()