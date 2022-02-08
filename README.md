# kucoin-to-cointracker
Allows you to convert Kucoin mrgin transactions into Cointracker compatible CSV files for manual import.

# Kucoin Margin Transactions -> Cointracker Transactions
There is currently no third-party integration between Cointracker and Kucoin Margin to get margin/leveraged transactions from Kucoin into Cointracker, see this [request](https://community.cointracker.io/t/kucoin-margin-account-is-completely-ignored/1000). This repo allows you to transform Kucoin transactions into something that is relatively easy to import into Cointracker. 

## Pre-requisites
* python3
* pip / pipenv
* TRADE_xxxxxxxxxxxxxxxxxxxxxxxx.csv file (This file can be exported from Kucoin (inside the zip file you download)

## Installation

1. `git clone https://github.com/austinbcomstock/kucoin-to-cointracker.git`

2. `cd ./kucoin-to-cointracker`

3. `pipenv install`

OR

3. `pip install -r requirements.txt`

4. Move the the TRADE_xxxxxxxxxxxxxxxxxxxxxxxx.csv is in the `kucoin-to-cointracker` folder

## Run the script

`pipenv run python kucoin_to_cointracker.py -f TRADE_xxxxxxxxxxxxxxxxxxxxxxxx.csv -o kucoin.csv`

OR

`python kucoin_to_cointracker.py -f TRADE_xxxxxxxxxxxxxxxxxxxxxxxx.csv`

If its another location, `python kucoin_to_cointracker.py -f ./full/location/to/the/TRADE_xxxxxxxxxxxxxxxxxxxxxxxx.csv -o ./full/location/to/the/kucoin.csv`

## See the created files
One csv file output

## Upload the files into Cointracker
Upload the file into Cointracker as a manual wallet with whatever nickname you want.
