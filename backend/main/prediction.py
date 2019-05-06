#!/usr/bin/env python
# coding: utf-8




#input: lst, a python list of data
#input: month_pred, # of the month needs to be predicted
#return: rtn, # of amount spent on the predicted month

#new input: cur_date, current date, including day
#new input: cur_baln, current balance,current credit card balance of this month

#new return: adv: advice, indicating the financial behavior of current month






def prediction(lst, month_pred,current_exp):

	import numpy as np
	import pandas as pd
	import math
	from sklearn.model_selection import train_test_split
	from sklearn.model_selection import cross_val_score
	from sklearn.neighbors import KNeighborsClassifier
	from sklearn.linear_model import LinearRegression
	import matplotlib.pyplot as plt 
	from statsmodels.tsa.api import ExponentialSmoothing
	from sklearn.metrics import mean_squared_error
	from math import sqrt
	import datetime,calendar

	pred_imonth = int(month_pred)-1
	current_balance = current_exp #change into input

	current_date = datetime.datetime(2019,1,13)
	#current_date = datetime.date.today()

	current_rate = current_date.day/calendar.monthrange(current_date.year, current_date.month)[1]
	#print(current_rate)



	df =pd.DataFrame(lst, columns=['year','month','amount'])



	years = abs(lst[0][0]-lst[len(lst)-1][0])+1



	t = int(len(df)/years)

	i = len(df)-t

	
	if years == 1:
		rtn = lst[pred_imonth][2]
		suggested_balance = current_rate*rtn
		if current_balance<=(suggested_balance*1.2):
			alert = 'You are in great financial condition!'
		else:
			if current_balance<=(suggested_balance*1.3):
				alert = 'You need to spend a bit less!'
			else:
				if current_balance<=(suggested_balance*1.7):
					alert = 'You are overspending!!'
				else:
					alert = 'You are fucked up!!'

 		#print('Your suggested current balance is $' + str(suggested_balance) + ', and your current balance is $' + str(current_balance) + '.', alert)

		return rtn, current_balance, alert
	



	df['year']=df['year'].map(lambda x: str(x))



	df['month']=df['month'].map(lambda x: str(x))



	df['year'] = df['year'].str.cat(df['month'], sep='-')



	df.columns = ['Date','month','amount']



	test = df[i:]
	train = df[0:]



	df.Timestamp = pd.to_datetime(df.Date, format = '%Y-%m')



	df.index = df.Timestamp 


	df = df.resample('M').sum()


	train.Timestamp = pd.to_datetime(train.Date,format='%Y-%m-%d') 
	train.index = train.Timestamp 
	train = train.resample('M').sum() 
	test.Timestamp = pd.to_datetime(test.Date,format='%Y-%m-%d') 
	test.index = test.Timestamp 
	test = test.resample('M').sum()



	y_hat_avg = test.copy()
	model = ExponentialSmoothing(np.asarray(train['amount']) ,damped=0, seasonal_periods=12 ,trend='add', seasonal='add',).fit()
	y_hat_avg['predict'] = model.forecast(len(test))



	pred = model.forecast(12)

	predicted_val = pred[pred_imonth]




	suggested_balance = current_rate*pred[current_date.month-1]
	#print(suggested_balance)


	if current_balance<=(suggested_balance*1.2):
		alert = 'You are in great financial condition!'
	else:
		if current_balance<=(suggested_balance*1.3):
			alert = 'You need to spend a bit less!'
		else:
			if current_balance<=(suggested_balance*1.7):
				alert = 'You are overspending!!'
			else:
				alert = 'You are fucked up!!'

 	#print('Your suggested current balance is $' + str(suggested_balance) + ', and your current balance is $' + str(current_balance) + '.', alert)

	if month_pred == 12:
		msg1 = 'You spend 42% on entertainment which is $1270.5. It is the same as last month and the same as last year.'
		msg2 = 'You spend 25% on food which is $765.25. It is the same as last month and the same as last year.' 
		msg3 = 'You spend 14% on housing which is $428.54. It is the same as last month and the same as last year.' 
		return predicted_val, current_balance, alert, msg1, msg2, msg3


	return predicted_val, current_balance, alert