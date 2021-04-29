l=list(range(100))
bg=['#00ffff']*100

_js={
	'tk':{
		'n':(8,6),
		'buttom':(100,100),
		'delta':(5,5),
		'w':(200,1),
		'/nick':'Q\u03c9Q',
	},
	'text':l,
	'bg':bg,
	's':'qwq',
}

import fastgui

def press(i:int):
	l[i]=l[i]+1000
	_js['s']+=str(i)
	if i==40:
		return fastgui.DESTROY
	elif i==30:
		return fastgui.JUMP

fastgui.mtgui(_js,press,hz=0.1)

