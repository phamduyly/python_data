#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
import itertools
import numpy as np
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import pandas as pd
import statsmodels.api as sm
import matplotlib
matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 12
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color'] = 'k'


# In[2]:


df = pd.read_excel("Sample - Superstore.xls")
#only taking the Furniture row out of category
furniture = df.loc[df['Category'] == 'Furniture']


# In[3]:


furniture.head


# In[4]:


furniture.describe()


# In[5]:


df.dtypes


# In[6]:


furniture['Order Date'].min(), furniture['Order Date'].max()


# In[7]:


furniture = furniture.sort_values('Order Date')
furniture.isnull().sum()


# In[8]:


#sum Sales group by order date and reset index 
furniture1 = furniture.groupby('Order Date')['Sales'].sum().reset_index()


# In[9]:


furniture.describe()


# In[10]:


furniture1.describe() 


# In[11]:


#start converting data to only have a.Time and b.Sales metrics 
furniture1.head()


# In[12]:


#indexing 
furniture = furniture1.set_index('Order Date')
furniture.index


# In[13]:


#resample the sales 
#use the avg daily sales value for that month instead, and we are using the start
# of each month as the timestamp
y = furniture['Sales'].resample('MS').mean()


# In[14]:


y['2017']


# In[15]:


#plot config: 
y.plot()
plt.show()


# In[16]:


#Showed a.Obeserved, trend, seasonal, residual 
from pylab import rcParams
rcParams['figure.figsize'] = 18, 8
decomposition = sm.tsa.seasonal_decompose(y, model='additive')
fig = decomposition.plot()
plt.show()


# In[17]:


#Start Implement 'Time series forecasting' with ARIMA

p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))


# In[19]:


#CODE BLOCK that having trouble 


#for param in pdq:
#    for param_seasonal in seasonal_pdq:
#        try:
#            mod = sm.tsa.statespace.SARIMAX(y,
#                                            order=param,
#                                            seasonal_order=param_seasonal,
#                                            enforce_stationarity=False,
#                                            enforce_invertibility=False)
#results = mod.fit()
#print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
#        except:
#            continue


# In[20]:


#starting ARIMA 
#starting on using ARIMA as Time seris forecasting 
mod = sm.tsa.statespace.SARIMAX(y,
                                order=(1, 1, 1),
                                seasonal_order=(1, 1, 0, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary().tables[1])


# In[21]:


#Diagnostics running. This is to investigate any unsual behavior
results.plot_diagnostics(figsize=(16, 8))
plt.show()


# In[28]:


#Validating forecasting 
#to help understand the accuracy of our forecast, we compare predicted sales ot rea
#with thre real sales of the time series, and we set forecasts 
pred = results.get_prediction(start=pd.to_datetime('2017-01-01'),dynamic=False)
pred_ci = pred.conf_int()

ax = y['2014':].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='One-step aheaed Forecast',alpha=.7,figsize=(14,7))

ax.fill_between(pred_ci.index, 
               pred_ci.iloc[:, 0],
               pred_ci.iloc[:, 1], color='k', alpha=.2)

ax.set_xlabel('Date')
ax.set_ylabel('Furniture Sales')
plt.legend()

plt.show()


# In[29]:


y.plot()
plt.show() 


# In[30]:


#Showing the mean squared error of forecast 

y_forecasted = pred.predicted_mean
y_truth = y['2017-01-01':]

#What is the meaning of this LINE
mse = ((y_forecasted - y_truth) ** 2).mean()
print(mse)
#MSE = estimator measures the average of the squares of the errors
print('The Mean Squared Error of our forecasts is {}'.format(round(mse,2)))


# In[31]:


y_forecasted = pred.predicted_mean
y_truth = y['2017-01-01':]

#RESEARCHED. More about how to use plot to really draw with plot(ident 2 line)
y_forecasted.plot()
y_truth.plot()


# In[32]:


#RMSE - shows the model was able to forecast withint the best range of 
print('The Root Mean Squared Error of our forecasts is {}'.format(round(np.sqrt(mse), 2)))


# In[33]:


#NEXT STEP - Producing and visualizing forecasts
pred_uc = results.get_forecast(steps=100)
pred_ci = pred_uc.conf_int()

ax = y.plot(label='observed', figsize=(14, 7))
pred_uc.predicted_mean.plot(ax=ax, label='Forecast')
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.25)

#Start to have this data set information

ax.set_xlabel('Date')
ax.set_ylabel('Furniture Sales')

plt.legend()
plt.show()


# In[34]:


#Time series of furniture vs office suplies
furniture = df.loc[df['Category'] == 'Furniture']
office = df.loc[df['Category'] == 'Office Supplies']
furniture.shape, office.shape


# In[35]:


# START DATA EXPLORATION

cols = ['Row ID', 'Order ID', 'Ship Date', 'Ship Mode', 'Customer ID', 'Customer Name', 'Segment', 'Country', 'City', 'State', 'Postal Code', 'Region', 'Product ID', 'Category', 'Sub-Category', 'Product Name', 'Quantity', 'Discount', 'Profit']
furniture.drop(cols, axis=1, inplace=True)
office.drop(cols, axis=1, inplace=True)
furniture = furniture.sort_values('Order Date')
office = office.sort_values('Order Date')
furniture = furniture.groupby('Order Date')['Sales'].sum().reset_index()
office = office.groupby('Order Date')['Sales'].sum().reset_index()
furniture = furniture.set_index('Order Date')
office = office.set_index('Order Date')
y_furniture = furniture['Sales'].resample('MS').mean()
y_office = office['Sales'].resample('MS').mean()
furniture = pd.DataFrame({'Order Date':y_furniture.index, 'Sales':y_furniture.values})
office = pd.DataFrame({'Order Date': y_office.index, 'Sales': y_office.values})
store = furniture.merge(office, how='inner', on='Order Date')
store.rename(columns={'Sales_x': 'furniture_sales', 'Sales_y': 'office_sales'}, inplace=True)
store.head()


# In[36]:


plt.figure(figsize=(20, 8))
plt.plot(store['Order Date'], store['furniture_sales'], 'b-', label = 'furniture')
plt.plot(store['Order Date'], store['office_sales'], 'r-', label = 'office supplies')
plt.xlabel('Date'); plt.ylabel('Sales'); plt.title('Sales of Furniture and Office Supplies')
plt.legend();


# In[37]:


first_date = store.ix[np.min(list(np.where(store['office_sales'] > store['furniture_sales'])[0])), 'Order Date']
print("Office supplies first time produced higher sales than furniture is {}.".format(first_date.date()))


# In[40]:


#Modelling time series with prohet
#Used to display patterns on different time scales such as YEARLY, WEEKLY, DAILY
from fbprophet import Prophet
furniture = furniture.rename(columns={'Order Date': 'ds', 'Sales': 'y'})
furniture_model = Prophet(interval_width=0.95)
furniture_model.fit(furniture)
office = office.rename(columns={'Order Date': 'ds', 'Sales': 'y'})
office_model = Prophet(interval_width=0.95)
office_model.fit(office)
furniture_forecast = furniture_model.make_future_dataframe(periods=36, freq='MS')
furniture_forecast = furniture_model.predict(furniture_forecast)
office_forecast = office_model.make_future_dataframe(periods=36, freq='MS')
office_forecast = office_model.predict(office_forecast)
plt.figure(figsize=(18, 6))
furniture_model.plot(furniture_forecast, xlabel = 'Date', ylabel = 'Sales')
plt.title('Furniture Sales');


# In[41]:


furniture_names = ['furniture_%s' % column for column in furniture_forecast.columns]
office_names = ['office_%s' % column for column in office_forecast.columns]
merge_furniture_forecast = furniture_forecast.copy()
merge_office_forecast = office_forecast.copy()
merge_furniture_forecast.columns = furniture_names
merge_office_forecast.columns = office_names
forecast = pd.merge(merge_furniture_forecast, merge_office_forecast, how = 'inner', left_on = 'furniture_ds', right_on = 'office_ds')
forecast = forecast.rename(columns={'furniture_ds': 'Date'}).drop('office_ds', axis=1)
forecast.head()


# In[ ]:


#Trend and Forecast Viz
plt.figure(figsize=(10, 7))
plt.plot(forecast['Date'], forecast['furniture_trend'], 'b-')
plt.plot(forecast['Date'], forecast['office_trend'], 'r-')
plt.legend(); plt.xlabel('Date'); plt.ylabel('Sales')
plt.title('Furniture vs. Office Supplies Sales Trend');


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




