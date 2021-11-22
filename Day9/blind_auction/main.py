from art import logo

print(logo)
print("Welcome to the secret auction program.")

bids = {}
continue_program = True
while continue_program:
    bidder = input("What is you name? ")
    bid = int(input("What's your bid? $"))
    bids[bidder] = bid
    any_bidder = input("Are there any other bidders? ")
    if any_bidder == "no":
        continue_program = False

max_bid = 0
for bidder in bids:
    if bids[bidder] > max_bid:
        max_bid = bids[bidder]
        max_bidder = bidder
print(f"The winner is {max_bidder} with a bid of ${max_bid}.")
