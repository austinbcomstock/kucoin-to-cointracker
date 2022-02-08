import pandas as pd
import argparse

def load_kucoin_file(file):
    return pd.read_csv(file, index_col=False)

def convert_kucoin_to_cointracker(df):

    # # Strip the clock times to only leave the dates
    # df.entryDate = pd.to_datetime(df['tradeCreatedAt']).apply(lambda x: x.date())
    
    # Need to split symbol into receive and sent currencies columns
    df[['Received Currency', 'Sent Currency']] = df['symbol'].str.split('-', expand=True)
    
    # Filter on only the columns we care about from Kucoin
    df = df[['tradeCreatedAt', 'size', 'Received Currency', 'funds', 'Sent Currency', 'fee', 'feeCurrency']]

    # Change the column names to what Cointracker wants
    df.columns = ['Date', 'Received Quantity', 'Received Currency', 'Sent Quantity', 'Sent Currency', 'Fee Amount', 'Fee Currency']

    return df

def export_csv(df, filename):
    df.to_csv(filename, index=False)

def main(args):

    # Ignoring deprecated feature warning
    pd.set_option('mode.chained_assignment', None)

    df = load_kucoin_file(args.file)
    cointracker_dataframe = convert_kucoin_to_cointracker(df)
    export_csv(cointracker_dataframe, filename='./kucoin.csv')
        
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=f'')
    # Positional
    parser.add_argument('-f', '--file', type=str, metavar='',help="the file location of the Kucoin export csv file")
    args = parser.parse_args()
    main(args)