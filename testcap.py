import unittest
import cap

class TetsCap(unittest.TetsCase):
	"""docstring for ClassName"""
	def tOW():
		text='pakistan'
		result=cap.capTest(text)
	self.asserEqual(result,'Pakistan')
if __name__ == '__main__':
	unittest.main()

