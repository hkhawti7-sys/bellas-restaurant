# Bella's Restaurent Ordering System

A simple Python program to take food orders for a restaurant called
Bella's Restaurent. It runs in the terminal.

## What it does

- Shows the food menu.
- Lets you make an order for a customer.
- Adds 19% tax and shows a receipt.
- Saves the order to a text file.

## How to install

Only Python 3 is needed.

## How to run

Open a terminal in this folder and run:

```
python3 main.py
```

## How to use it

1. Choose `1` to see the menu.
2. Choose `2` to make an order. Type the customer name and phone, then
   add items by their id (for example `B01`). Press Enter to finish.
3. The program shows the receipt and saves the order to
   `data/orders.txt`.
4. Choose `3` to quit.

## Files

- `main.py` - the main program with the menu.
- `menu_item.py` - the MenuItem class (one food item).
- `menu.py` - the Menu class (the list of items, reads the CSV file).
- `customer.py` - the Customer class (name and phone).
- `order.py` - the Order class (items, total, receipt, saving).
- `data/menu.csv` - the food menu.

## Dataset

The menu follows the idea of the public *Restaurant Menu Items* dataset
on Kaggle:
https://www.kaggle.com/datasets/graphquest/restaurant-menu-items
