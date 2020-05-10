from __future__ import print_function
from builtins import str
from builtins import range
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import dictionaries as dlg_populate
import sys, os
from collections import deque

num_of_items = {'1':'0', '2':'0', '3':'0', '4':'0', '5':'0', '6':'0', '7':'0', '8':'0', '9':'0' , '10':'0', '11':'0', '12':'0', '13':'0'}
item_types = {'1':[], '2': [], '3':[], '4':[], '5':[], '6':[], '7':[], '8':[], '9':[] , '10':[], '11':[], '12':[], '13':[]}
user_control_list = []

def populate_lists(self, gs_dict, info_dict):
	items = list(self.ui.scene.items())
	
	searched_items = []
	for item in items:
		if item.data(1).toString() == 'W':
			item_id = str(item.data(1).toString() + item.data(2).toString()).encode('utf_8')
			count = int(num_of_items['1'])
			count += 1
			num_of_items['1'] = str(count)
			item_types['1'].append(item_id[1:])
			item_types['1'].sort(key = int)
		elif item.data(1).toString() == 'R':
			count = int(num_of_items['3'])
			count += 1
			num_of_items['3'] = str(count)
			item_id = str(item.data(1).toString() + item.data(2).toString()).encode('utf_8')
			item_types['3'].append(item_id[1:])
			item_types['3'].sort(key = int)
		elif item.data(1).toString() == 'U':
			item_id = str(item.data(1).toString() + item.data(2).toString()).encode('utf_8')
			item_types['4'].append(item_id[1:])
			item_types['4'].sort(key = int)
			count = int(num_of_items['4'])
			count += 1
			num_of_items['4'] = str(count)
		elif item.data(1).toString() == 'J':
			item_id = str(item.data(1).toString() + item.data(2).toString()).encode('utf_8')
			item_types['5'].append(item_id[1:])
			item_types['5'].sort(key = int)
			count = int(num_of_items['5'])
			count += 1
			num_of_items['5'] = str(count)
		elif item.data(1).toString() == 'L':
			item_id = str(item.data(1).toString() + item.data(2).toString()).encode('utf_8')
			start = str(item.data(3).toString()).encode('utf_8')
			stop = str(item.data(4).toString()).encode('utf_8')
			#print item_id, start, stop
			if start[0] == 'W':
				x = item_id[1:] not in item_types['2']
				if x == True:
					item_types['2'].append(item_id[1:])
					item_types['2'].sort(key = int)
					count = int(num_of_items['2'])
					count += 1
					num_of_items['2'] = str(count)
			elif start[0] == 'J':
				x = item_id[1:] not in item_types['8']
				if x == True:
					item_types['8'].append(item_id[1:])
					item_types['8'].sort(key = int)
					count = int(num_of_items['8'])
					count += 1
					num_of_items['8'] = str(count)
			elif start[0] == 'I':
				x = item_id[1:] not in item_types['10']
				if x == True:
					item_types['10'].append(item_id[1:])
					item_types['10'].sort(key = int)
					count = int(num_of_items['10'])
					count += 1
					num_of_items['10'] = str(count)
			elif stop[0] == 'R':
				if start[0] == 'U':
					x = item_id[1:] not in item_types['7']
					if x == True:					
						item_types['7'].append(item_id[1:])
						item_types['7'].sort(key = int)
						count = int(num_of_items['7'])
						count += 1
						num_of_items['7'] = str(count)
				else:
					x = item_id[1:] not in item_types['6']
					if x == True:
						item_types['6'].append(item_id[1:])
						item_types['6'].sort(key = int)
						count = int(num_of_items['6'])
						count += 1
						num_of_items['6'] = str(count)
			elif stop[0] == 'U':
				x = item_id[1:] not in item_types['11']
				if x == True:
					item_types['11'].append(item_id[1:])
					item_types['11'].sort(key = int)
					count = int(num_of_items['11'])
					count += 1
					num_of_items['11'] = str(count)
			elif start[0] == 'R':
				x = item_id[1:] not in item_types['6']
				if x == True:
					item_types['6'].append(item_id[1:])
					item_types['6'].sort(key=int)
					count = int(num_of_items['6'])
					count += 1
					num_of_items['6'] = str(count)
			
		elif item.data(1).toString() == 'S':
			item_id = str(item.data(1).toString() + item.data(2).toString()).encode('utf_8')
			item_types['12'].append(item_id[1:])
			item_types['12'].sort(key = int)
			count = int(num_of_items['12'])
			count += 1
			num_of_items['12'] = str(count)
		elif item.data(1).toString() == 'I':
			item_id = str(item.data(1).toString() + item.data(2).toString()).encode('utf_8')
			item_types['13'].append(item_id[1:])
			item_types['13'].sort(key = int)
			count = int(num_of_items['13'])
			count += 1
			num_of_items['13'] = str(count)
system = []
first_item = 1
def find_path(self,block):
	global first_item
	if first_item == 1:
		block = 'W' + str(item_types['1'][0])
		first_item = 2
		system.append(block)
		#find_path(self, child)
	
	#nchild = ''
	items = list(self.ui.scene.items())
	for item in items:
		name = str(item.data(1).toString() + item.data(2).toString()).encode('utf_8')
		if name == block:
			nchild = str(item.data(6).toString()).encode('utf_8')
			print(nchild)
			if nchild == '1':
				child = str(item.data(61).toString()).encode('utf_8')
				system.append(child)
				find_path(self, child)
			elif nchild == '0':				
				break
			else:
				try:
			#elif int(nchild) > 1:
					temp_child_list = []
					for i in range(int(nchild)):
						child = str(item.data('6'+str(i+1)).toString()).encode('utf_8')
						system.append(child)
						find_path(self, child)
				except:
					pass
	#print system
			

def run_path(self, gs_dict, dialog_dict):
	find_path(self, 'no_block')
	"""
	items = self.ui.scene.items()
	for item in items:
		lst = ['W', 'R', 'J', 'U', 'S', 'I']
		ident = unicode(item.data(1).toString()).encode('utf_8')
		if ident in lst:
			nchild = unicode(item.data(6).toString()).encode('utf_8')
			num = unicode(item.data(2).toString()).encode('utf_8')
			print ident+num, nchild
	"""
