from yfinance import download
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


tickerSymbol = 'COLPAL.NS'

start_date = datetime.datetime(2022,5, 21)
end_date = datetime.datetime.now()
#end_date = datetime.datetime(2015,1, 1)

data=download(tickerSymbol, start=start_date, end=end_date).reset_index()#[["Date","Close"]]


purchase_data = pd.DataFrame(columns=['Date', 'Close','Hike','Quantity'])
sell_data = pd.DataFrame(columns=['Date', 'Close','Hike','Quantity'])
last_trad=data.Close[0]
fund=0

t_shares=0
for i in range(len(data)):
    
    percent_hike=((data.Close[i]-last_trad)/last_trad)*100
    
    
    if percent_hike>6:
        #selling Signal
        
        sell_quantity=round(percent_hike*0.5)
        
        sell_amount=round(sell_quantity)*(data.Close[i])
        
        last_trad=data.Close[i]
        
        if fund<sell_amount:
            print(f"\nCant sell {round(sell_quantity)} shares because of insufficient Fund. {sell_quantity}% increases\n")
            continue
                    
        
        fund=fund-sell_amount
                
        sell_data=pd.concat([sell_data, data.loc[[i]]], ignore_index=True)
        sell_data.Quantity.fillna(-sell_quantity, inplace=True)
        sell_data.Hike.fillna(round(percent_hike,2), inplace=True)
        t_shares=t_shares-round(sell_quantity)
       
        #print(f"S {round(percent_hike,1)}, {round(sell_quantity)} x {round(data.Close[i],1)} = {round(sell_amount,1)}")        
        #print(f"Shares = {t_shares}, Fund = {fund}\n")
        
    if percent_hike<-3:
        #purchasing Signal
        
        purchase_quantity=round(percent_hike)
        purchase_amount=purchase_quantity*(data.Close[i])         
        
        last_trad=data.Close[i] 
        fund=fund-purchase_amount
        
        purchase_data=pd.concat([purchase_data, data.loc[[i]]], ignore_index=True)
        purchase_data.Quantity.fillna(-purchase_quantity, inplace=True)
        purchase_data.Hike.fillna(round(percent_hike,2), inplace=True)
        
        t_shares=t_shares-purchase_quantity
        
        #print(f"P {round(percent_hike,1)},  {round(purchase_quantity)} x {round(data.Close[i],1)} =  {round(purchase_amount,1)}")
        #print(f"Shares = {t_shares}, Fund = {round(fund)}\n")
        


purchase_data["Total"]=purchase_data["Close"]*purchase_data["Quantity"]
sell_data["Total"]=sell_data["Close"]*sell_data["Quantity"]


trade_data=pd.concat([sell_data, purchase_data]).sort_values('Date') #Merge Sell Data And Purchase Data
trade_data["Cummulative Quantity"]=trade_data.Quantity.cumsum()
trade_data["Cummulative Total"]=round(trade_data.Total.cumsum(),2)


current_shares_in_market=trade_data["Cummulative Quantity"].values[-1]
lst_price=data.Close[len(data)-1]

total_purchase=trade_data["Cummulative Total"].values.max()
total_sell=-sum(sell_data["Total"])

profit=total_sell+(lst_price*current_shares_in_market)-total_purchase

print(f"\nFund In Market Currently = {current_shares_in_market} x {lst_price} = {current_shares_in_market*lst_price}")
print(f"Amount Withdrawl = {round(total_sell+(lst_price*current_shares_in_market),2)}")
print(f"Amount Invested = {round(total_purchase,2)}")
print(f"Profit= {round(profit)}")
print(f"ROI= {round((profit)/total_purchase*100,2)}")

print(f"Real ROI = {round((data.Close.values[-1]-data.Close.values[0])/data.Close.values[0]*100,2)}")

#shares_sell_in_loss=int(sum(purchase_data.where(purchase_data.Close>lst_price,0).Quantity)-sum(-sell_data["Quantity"]))
#print(f"Total {shares_sell_in_loss} shares are selled in loss.\n")



        
#Plotting On Graph

fig, ax = plt.subplots(figsize=(10, 4))  #Increase Graph Width
for index, row in sell_data.iterrows():
    ax.text(row['Date'], row['Close'], int(row['Quantity']), ha='center', va='bottom')
    
for index, row in purchase_data.iterrows():
    ax.text(row['Date'], row['Close'], int(row['Quantity']), ha='center', va='bottom')

data.plot(kind='line',x="Date", y="Open", color='green', ax=ax)

#trade_data.plot(kind='line',x="Date", y="Close", color='blue', ax=ax)

sell_data.plot(kind='scatter',x="Date", y="Close", color='green', s=40, ax=plt.gca())
purchase_data.plot(kind='scatter',x="Date", y="Close", color='red', s=40, ax=plt.gca())

plt.show()

trade_data

