from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
import random

def index(request):

	return render(request, 'ninja_gold/index.html')
	

def process(request, building):
	
	if request.method == "POST":

		farm = random.randrange(10, 21)
		cave = random.randrange(5, 11)
		house = random.randrange(2, 6)
		casino = random.randrange(0, 51) 

		if building == 'farm':
			try:
				request.session['money'] += farm
			except:
				request.session['money'] = 0

			try:
				request.session['activities'].append('Earned {} golds from the {}! {}'.format(farm, "Farm", datetime.now()))
			except:
				request.session['activities'] = []

		elif building == 'cave':
			try:
				request.session['money'] += cave
			except:
				request.session['money'] = 0

			try:
				request.session['activities'].append('Earned {} golds from the {}! {}'.format(cave, "Cave", datetime.now()))
			except:
				request.session['activities'] = ['']

		elif building == 'house':
			try:
				request.session['money'] += house
			except:
				request.session['money'] = 0

			try:
				request.session['activities'].append('Earned {} golds from the {}! {}'.format(house, "House", datetime.now()))
			except:
				request.session['activities'] = ['']

		elif building == 'casino':
			try:
				if random.randrange(0, 2) == 1:
					request.session['money'] += casino

					try:
						request.session['activities'].append('Earned {} golds from the {}! {}'.format(casino, "Casino", datetime.now()))
					except:
						request.session['activities'] = ['']
				else:
					request.session['money'] -= casino

					try:
						request.session['activities'].append('LOST {} golds from the {}! {}'.format(casino, "Casino", datetime.now()))
					except:
						request.session['activities'] = ['']
			except:
				request.session['money'] = 0

		elif building == 'clear':
				request.session['money'] = 0
				request.session['activities'] = []

		else:
			pass

		return redirect('/')
	
	else:
		return redirect('/')

