def Backtest(close,quantity):
  current_shares_in_market=quantity.dropna().cumsum().values[-1]
  lst_price=close[len(data)-1]
  total=close*quantity
  total_purchase=total.cumsum().max()
  total_sell=-total[total < 0].sum()

  profit=total_sell+(lst_price*current_shares_in_market)-total_purchase

  print(f"\nFund In Market Currently = {current_shares_in_market} x {lst_price} = {current_shares_in_market*lst_price}")
  print(f"Amount Withdrawl = {round(total_sell+(lst_price*current_shares_in_market),2)}")
  print(f"Amount Invested = {round(total_purchase,2)}")
  print(f"Profit= {round(profit)}")
  print(f"ROI = {round((profit)/total_purchase*100,2)}")

  print(f"Real ROI = {round((close.values[-1]-close.values[0])/close.values[0]*100,2)}")



               #--------------------------------Plotting Graph--------------------------------#
               
  fig, ax = plt.subplots(figsize=(10, 4))
  plt.plot(close, color='g')
  close.loc[quantity[quantity > 0].dropna().index]



  for i, txt in enumerate(quantity):
    if txt > 0:
        plt.annotate(int(txt), (quantity.index[i], close[i]), textcoords="offset points", xytext=(0,5), ha='center')

    if txt < 0:
        plt.annotate(int(txt), (quantity.index[i], close[i]), textcoords="offset points", xytext=(0,5), ha='center')


  entry = pd.Series(np.nan, index=close.index)
  exit = pd.Series(np.nan, index=close.index)

  entry[quantity > 0] = close[quantity > 0]
  exit[quantity < 0] = close[quantity < 0]

  plt.scatter(close.index, entry, marker='^', color='green')
  plt.scatter(close.index, exit, marker='o', color='red',s=50)
  
  
Backtest(data.Close, data.Quantity)   #close price of stocks and quantity of stocks to purchase ie,[0,0,4,7,-3,0,5,0,-2,-3]
