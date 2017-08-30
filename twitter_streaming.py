#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "805498537-o049VRBSFJQZLiVvCVbFPdHYvoDczD6wSJvE5zbJ"
access_token_secret = "GGTKKxysLSnaje3hLRdP8R4DGVkxIrJarZTKzRZ9GDl0N"
consumer_key = "PVD3UnWMJEWoBMip2fIE6cCoA"
consumer_secret = "kuzyoSmkllnC3lRjSv1NNNYP7gdQMCcwkAWWXDxFKNHIyMvTEZ"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=[ 'NEO', 'Monaco', 'OmiseGO', 'Ethereum', 'Qtum', 'Bitcoin Cash', 'Bitcoin', 'TenX', 'Lisk', 'Ripple', 'Litecoin', 'Monero', 'Ark', 'DigiByte', 'SysCoin', 'Stratis', 'AdEx', 'Ubiq', 'Storj', 'TokenCard', 'Civic', 'Dash', 'Nexus', 'Siacoin', 'Basic Attention Token', 'Zcash', 'Ethereum Classic', 'Verge', 'BitShares', 'Status', 'PIVX', 'NEM', 'Waves', 'NAV Coin', 'Expanse', 'Metal', 'Decred', 'Factom', 'Nxt', 'Golem', 'Blitzcash', 'Rise', 'Edgeless', 'Musicoin', 'Blocknet', 'Steem', 'Komodo', 'GameCredits', 'GeoCoin', 'LBRY Credits', 'KoreCoin', 'Byteball', 'Legends Room', 'Bancor', 'Vertcoin', 'Patientory', 'DECENT', 'Cofound.it', 'Crown', 'Stellar Lumens', 'FirstBlood', 'Elastic', 'Safe Exchange Coin', 'Dogecoin', 'MaidSafeCoin', 'Triggers', 'Wings', 'Breakout Stake', 'Numeraire', 'FunFair', 'PinkCoin', 'ExclusiveCoin', 'Gnosis', 'ReddCoin', 'Viacoin', 'Shift', 'Particl', 'ZClassic', 'Augur', 'Lunyr', 'Qwark', 'FlorinCoin', 'WeTrust', 'Nexium', 'Aragon', 'ZCoin', 'Ardor', 'Burst', 'DigixDAO', 'ZenCash', 'NuBits', 'Darcrus', 'Quantum Resistant Ledger', 'Counterparty', 'Voxels', 'I/O Coin', 'Humaniq', 'Synereo', 'SingularDTV', 'iExec RLC', 'Bytecent', 'HempCoin', 'EuropeCoin', 'Diamond', 'Mysterium', 'MonetaryUnit', 'Synergy', 'Matchpool', 'FoldingCoin', 'OKCash', 'Databits', 'Radium', 'BitBean', 'adToken', 'Einsteinium', 'PotCoin', 'MonaCoin', 'Bata', 'APX', 'Circuits of Value', 'Gulden', 'BitBay', 'BlackCoin', 'CloakCoin', 'Chronobank', 'NeosCoin', 'SpreadCoin', 'Aeon', 'ParkByte', 'Curecoin', 'CannabisCoin', 'Omni', 'Boolberry', 'Dynamic', 'Peercoin', 'Golos Gold', 'eBoost', 'DopeCoin', 'Creditbit', 'Unobtanium', 'Xaurum', 'ArtByte', 'vTorrent', 'Breakout', 'EverGreenCoin', 'DigitalNote', 'VeriCoin', 'Syndicate', 'Magi', 'Swarm City', 'Energycoin', 'Hacker Gold', 'Clams', 'WhiteCoin', 'Emercoin', 'VeriumReserve', 'Vcash', 'ClubCoin', 'Groestlcoin', 'ION', 'SIBCoin', 'Bitcrystals', 'Feathercoin', 'Sequence', 'GridCoin', 'LoMoCoin', 'UnbreakableCoin', 'Melon', 'Capricoin', 'FairCoin', 'Steem Dollars', 'DT Token', 'Bitswift', 'BitSend', 'Golos', 'Incent', 'Agoras Tokens', 'Gambit', 'Project Decorum', 'BitcoinDark', 'TransferCoin', 'Myriad', 'e-Gulden', 'Tokes', 'Influxcoin', 'Rubycoin', 'Internet of People', 'Global Currency Reserve', 'Sphere', 'GoldCoin', 'Startcoin', 'SolarCoin', 'TrustPlus', 'Pesetacoin', 'SaluS', 'Stealthcoin', 'Memetic', 'Auroracoin', '2GIVE',])
