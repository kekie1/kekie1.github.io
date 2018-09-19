#[4,5],[9,12],[16,],[,]

#     0000000000111111111122222222223333333
#     0123456789012345678901234567890123456
stuff="   text with   some    runs and some not"

def replace_runs(text_in):
	text=list(text_in)
	x=0
	current=[]
	total=[]
	running=False
	while x<len(text):
		if text[x]==" ":
			if not running:
				current.append(x)
			running=True
		else:
			if running:
				current.append(x)
				total.append(current)
				current=[]
				running=False
		x+=1
	
	print(total)
	to_delete=[]
	for i in total:
		if i[0]+1==i[1]:
			to_delete.append(i)
	for i in to_delete:
		total.remove(i)
	
	for i in total:
		text[i[0]:i[1]]="X"*(i[1]-i[0])
	
	
	return ''.join(text).replace("X","&nbsp")
	
print(replace_runs(stuff))