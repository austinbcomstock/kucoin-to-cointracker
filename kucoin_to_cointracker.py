import pandas as pd
import argparse

def load_kucoin_file(file):
    return pd.read_csv(file, index_col=False)

def convert_kucoin_to_cointracker(df):
    
    # Need to split symbol into 'Received Currency' and 'Sent Currency' columns
    df[['Received Currency', 'Sent Currency']] = df['symbol'].str.split('-', expand=True)
    
    # Filter on only the columns we care about from Kucoin
    df = df[['tradeCreatedAt', 'size', 'Received Currency', 'funds', 'Sent Currency', 'fee', 'feeCurrency']]

    # Change the column names to what Cointracker expects
    df.columns = ['Date', 'Received Quantity', 'Received Currency', 'Sent Quantity', 'Sent Currency', 'Fee Amount', 'Fee Currency']

    return df

def export_csv(df, filename):
    df.to_csv(filename, index=False)

def main(args):

    # Ignoring deprecated feature warning
    pd.set_option('mode.chained_assignment', None)

    # Load the CSV file
    df = load_kucoin_file(args.file)
    
    # Convert the transactions
    cointracker_dataframe = convert_kucoin_to_cointracker(df)
    
    # Export the Cointracker CSV file
    export_csv(cointracker_dataframe, filename=args.output)
        
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=f'Kucoin Margin export CSV to Cointracker compatible CSV file')
    # Positional
    parser.add_argument('-f', '--file', type=str, metavar='', help="Location of the Kucoin Margin CSV file")
    parser.add_argument('-o', '--output', type=str, default='./cointracker.csv', metavar='',help="Location to output the Cointracker compatible CSV file")
    args = parser.parse_args()
    main(args)
