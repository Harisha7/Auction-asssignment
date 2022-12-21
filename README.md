# Auction-asssignment
Implementing backend for auction application using REST API.



POST /app/login user login JSON body: takes the following properties 
email: string  , password: string

Returns loggedin or not

POST app/register register new user JSON body: takes the following properties

firstname: string , lastname: string, email: string , password: string

Returns registered or not

DELETE /app/login

users logout Returns logged out True

GET /app/user get current user returns info about current logged in user

POST /app/update_bid update bid

JSON body: takes the following properties

users: int ,price: int,auction_ item: int

returns updated or not

POST /app/add_item add item to the item table JSON body: takes the following properties

title: string, description: string, start_time: string, end_time: string

returns if item is added or not

GET /app/get_listitem get auction_itemList returns array of items

GET /app/get_item get specific item JSON body: takes the following properties id: int returns auction_item object

GET /app/get_itemwithimages get auction_items with images url returns list of auction_items with images url

GET /app/get_currentbid get current bids returns a list of current ongoing bids

GET /app/get_fivelatestbids get five latest bids

returns an array of five latest bids
