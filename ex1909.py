#Exercise: Managing a Shopping List
ShoppingCart= [
    
    {
        "ItemName":"apples",
        "Quantity":"2",
        "Price":"0.99"},

    {
        "ItemName":"bananas",
        "Quantity":"3",
        "Price":"1.87"},

    {
        "ItemName":"strawberries",
        "Quantity":"10",
        "Price":"2.56"},
    
    {
        "ItemName":"avocados",
        "Quantity":"10",
        "Price":"2.56"}
]

add= [
    {
        "ItemName":"peppers",
        "Quantity":"11",
        "Price":"2.06"},

    {
        "ItemName":"carrots",
        "Quantity":"20",
        "Price":"2.1"},

    {
        "ItemName":"broccoli",
        "Quantity":"5",
        "Price":"1,99"},
    ]

ShoppingCart.extend(add)
ShoppingCart[-1]["Quantity"]=3
ShoppingCart.pop(-1)
print(ShoppingCart)



