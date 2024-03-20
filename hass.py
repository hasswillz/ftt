import numpy as np
import pandas as pd
def main():
	dict1={'col1':[1,2,3,4], 'col2':[5,6,7,8], 'col3':['one', 'two','Three','four']}
	df1= pd.DataFrame(data=dict1)
	print(df1)
if __name__ == '__main__':
	main()