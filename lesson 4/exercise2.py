from __future__ import unicode_literals, print_function

	#lists
houston = [
	'1', '2', 
	'3', '4',
	'5', '6',
	'7', '8',
	'9', '10'
]
atlanta = [
	'6', '7',
	'8', '9',
	'10', '11',
	'12', '13'
]

chicago = [
	'6', '7',
	'8', '9',
	'14', '15',
	'16', '17'
]

   #Sets has braces like dictionaries
	 #class = set
houston_Set = set(houston)
atlanta_Set = set(atlanta)
chicago_Set = set(chicago)

HA = houston_Set & atlanta_Set
HAC = houston_Set & atlanta_Set & chicago_Set
ChicagoOnly = chicago_Set.difference(houston_Set).difference(atlanta_Set)

print()
print("duplicates between houston and atlanta are: {}".format(HA))
print("duplicates between all 3 sites are: {}".format(HAC))
print("numbers unique to chicago are: {}".format(ChicagoOnly))
