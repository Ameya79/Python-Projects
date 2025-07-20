import art
print(art.logo)


def max_bid(dic_having_all_bidders):
    max_bid = 0
    name_of_bidder = ''
    for bidder in dic_having_all_bidders: #i used hold but its outside the def dont forget to passs the paramax_bideter
        if dic_having_all_bidders[bidder] > max_bid:
            max_bid = dic_having_all_bidders[bidder]
            winner = (bidder)
        
    print(f'The winner is {winner}! with a bid of ${max_bid}')
    

# TODO-1: Ask the user for input
over = False
hold = {} #keeping it outside the while loop ensures it does NOT reset
while not over:
    name = input('Enter name of the bidder: ')
    price = int(input('Enter bid $ : '))
# TODO-2: Save data into dictionary {name: price}
# basically add to dic using basic add technique
    hold[name]=price
    # print(hold)
    yn = input('Are the others in the bid type y for yes n for no: ').lower()
# TODO-3: Whether if new bids need to be added
    if yn == 'n':
        max_bid(hold)   
        over = True 
        
    elif yn == 'y':
        print('\n'*100)

#TODO-4: copmare the bids in the dic



#how dooes it work
#take name input and bid => put in dic => ask if other  ppl are there => repeat same till not there using while loop => 
# when not there => go to def fn , which uses for loop and compares it with the max bid which takes on the value of the value hav ng the max bid
#  and the name of the bidder string catches the name of the bidder which had the max bid offered




