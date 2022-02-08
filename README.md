# kucoin-to-cointracker
Allows you to convert Kucoin margin transactions into Cointracker compatible CSV files for manual import.

# Kucoin Margin Transactions -> Cointracker Transactions
There is no third-party integration between Cointracker and Kucoin Margin to get margin/leveraged transactions from Kucoin into Cointracker; see this [request](https://community.cointracker.io/t/kucoin-margin-account-is-completely-ignored/1000). This repo allows you to transform Kucoin transactions into something relatively easy to import into Cointracker.

## Pre-requisites
* python3
* pip / pipenv
* TRADE_xxxxxxxxxxxxxxxxxxxxxxxx.csv file (This file is exported from Kucoin Margin transactions - inside the zip file they give you)

## Installation

1. `git clone https://github.com/austinbcomstock/kucoin-to-cointracker.git`

2. `cd ./kucoin-to-cointracker`

3. `pipenv install`

OR

3. `pip install -r requirements.txt`

4. Move the TRADE_xxxxxxxxxxxxxxxxxxxxxxxx.csv to the `kucoin-to-cointracker` folder

## Run the script

`pipenv run python kucoin_to_cointracker.py -f /path/to/KUCOIN.csv

`pipenv run python kucoin_to_cointracker.py -f TRADE_xxxxxxxxxxxxxxxxxxxxxxxx.csv -o cointracker.csv`

OR

`python kucoin_to_cointracker.py -f TRADE_xxxxxxxxxxxxxxxxxxxxxxxx.csv -o cointracker.csv`

## See the created files
Default is ./cointracker.csv (can be changed with -o FILENAME)

## Upload the files into Cointracker
Upload the file into Cointracker as a manual wallet with whatever nickname you want.
