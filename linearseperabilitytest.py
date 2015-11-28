import numpy


class LStest():
	
	def __init__(self,cl1_data,cl2_data):
		try:
			import cvxopt
		except ImportError:
			print "CVXOPT Module not found. Please install."
			
		