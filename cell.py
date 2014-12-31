"""
Erica Johnson
29 Dec 2014
"""

class Cell:
	
	def __init__(self, allele_1, allele_2):
	    self.allele_1 = allele_1
	    self.allele_2 = allele_2
	    self.BMR = self.find_BMR()
	    
	def dominant_allele(self):
	    if self.allele_2 in self.allele_1['dominant_over']:
	        return self.allele_1
	    elif self.allele_1 in self.allele_2['dominant_over']:
	        return self.allele_2
	    else:
	        return 'neither'
	        
	def find_BMR(self):
	    dominant = self.dominant_allele()
	    if dominant == 'neither':
	        average_BMR = (self.allele_1['BMR'] + self.allele_2['BMR'])/2
	        return average_BMR
	    else:
	        return dominant['BMR']