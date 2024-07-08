investment_in_bitcoin = float(input("How much have you invest in the bitcoin: "))
bitcoin_to_usd = float(input("Number of bitcoin u will convert in USD: "))
dollar_bitcoin_falls = float(input("How many dollar does the bitcoin falls: $"))

def bitcoinToUSD(bitcoin_amount, bitcoin_value_usd):
  usd_value = investment_in_bitcoin * bitcoin_to_usd
  return usd_value

investment_in_usd = bitcoinToUSD(investment_in_bitcoin, bitcoin_to_usd)
if investment_in_usd <= dollar_bitcoin_falls:
  print("Investment below","$",dollar_bitcoin_falls,"SELL!")
else:
  print("Investment above","$",dollar_bitcoin_falls)
