from menu import menu


def formatOrders(orders):
    quantityOrders = {}
    for order in orders:
        for item in order:
            quantityOrders[item] = 1 + quantityOrders.get(item, 0)
    return quantityOrders


def getTotal(orders, menu):
    total = 0
    for item, quantity in orders.values():
        total += (menu[item] * quantity)
    total += getTax(total)
    return total


def getTax(total):
    return round(total * .08625, 2)


def buildItemLine(quantity, order, price, length):
    line = f"{quantity} {order}"
    line += " " * (length - len(line) - 1 - len(str(price)))
    line += f"${price}"
    line += "\n"
    return line


def printReceipt(orders, menu, subtotal, gratuity, tax):
    s = "------------------------\n"
    s += "Restaurant".center(24)
    s += "\n" * 3
    for quantity, order in orders.items():
        price = menu[order] * quantity
        price = "{:.2f}".format(price)
        s += buildItemLine(quantity, order, price, 24)
    s += "\n" * 3
    subTotWhiteSpace = " "*(24 - 9 - len(subtotal))
    s += f"SUBTOTAL{subTotWhiteSpace}${subtotal}\n"
    taxWhiteSpace = " " * (24 - 4 - len(tax))
    s += f"TAX{taxWhiteSpace}${tax}\n"
    gratuityWhiteSpace = " " * (24 - 9 - len(str(gratuity)))
    s += f"GRATUITY{gratuityWhiteSpace}${gratuity}\n"
    total = float(subtotal) + float(tax) + float(gratuity)
    total = "{:.2f}".format(total)
    totalWhiteSpace = " " * (24 - 6 - len(str(total)))
    s += f"TOTAL{totalWhiteSpace}${total}"
    print(s)
