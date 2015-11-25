import numpy as np
import csv
import pickle

class read_WDBCdata():
	
	def __init__(self,filename):
		#super(read_WDBCdata, self).__init__()
		self.csvfile = open(filename)
		self.csvdata = csv.reader(self.csvfile, delimiter=',',quotechar='|')
		self.list_data = []
		#no_dims+2(id,tumor state)
		self.data = 0

		self.read_data()
		self.no_samples = len(self.list_data);#no_samples
		self.no_dims = len(self.list_data[0])
		self.data_new = np.empty((self.no_samples,self.no_dims-2));
		self.labels = np.arange(self.no_samples)
		self.convert_to_nparray()
		self.csvfile.close()
		#self.get_data()
		
	def read_data(self):
		for row in self.csvdata:
			self.list_data.append(row)
	def convert_to_nparray(self):
		self.data = np.array(self.list_data)
	
		self.labels = self.data[:,1]=='B' #one for benign, zero for malignant
		self.labels = np.ndarray.astype(self.labels,'int')
		self.data_new = self.data[:,2:self.no_dims]
	
	def acquire_data(self):
		self.container = (self.data_new,self.labels)
		return self.container
		
	def write_data(self):
		pickle.dump(self.container,open("wdbcdata.p","wb"))
		
		