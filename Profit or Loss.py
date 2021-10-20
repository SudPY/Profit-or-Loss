def Profit(costPrice, sellingPrice) :
    profit = (sellingPrice - costPrice)

    return profit

def Loss(costPrice, sellingPrice) :
    loss = (costPrice - sellingPrice)
    
    return loss

if __name__ == "__main__":

    costPrice = int(input("Please enter the cost price : "))
    sellingPrice = int(input("Please enter the selling price : "))

    if sellingPrice == costPrice:
        print("Neither profit nor loss.")
    
    elif sellingPrice > costPrice:
        print("Rs.", Profit(costPrice, sellingPrice), "profit.")
    
    else:
        print("Rs.", Loss(costPrice, sellingPrice), "loss.")
