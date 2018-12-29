from blockcypher import get_broadcast_transactions
import json
from pprint import pprint

#Finds all bitcoin transactions of a specified by the bitcoin variable
#Gets the senders hash, the amount sent
#And the highest receivers hash
def GetTransactions():

    #100000000 = 1 BTC
    #currently: 50BTC
    bitcoin= 10000000000 #change this value to capture transfers of specified amount

    #limit 100 is the highest bitcypher api allows you to go
    bitcoin_transactions = get_broadcast_transactions(limit=100)

    transaction_list = []

    for i in bitcoin_transactions:
        try:
            sender= i['inputs'][0]['addresses'][0]
        except KeyError:
            sender= 'None'
        bitcoin_sent= i['inputs'][0]['output_value']
        receiverLen= len(i['outputs'])
        try:
            receiver= i['outputs'][0]['addresses'][0]
        except TypeError:
            receiver= 'None'

        #find the highest receiver of bitcoin transaction
        highest= 0
        receivers= i['outputs']
        for a,i in enumerate(receivers):
            if receiverLen > 1:
                if receivers[a]['value'] > highest:
                    highest = receivers[a]['value']

        if bitcoin_sent > bitcoin:
            transaction_list.append([sender,bitcoin_sent,receiver,highest])

    return transaction_list
