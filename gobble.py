import tkinter as tk
import time

cookie_count = 0
click_power = 1
auto_click_cost = 50
auto_click_power = 0
auto_click_interval = 1000  # 1 second in milliseconds

def update_count():
    global cookie_count
    cookie_count += click_power
    cookie_count += auto_click_power
    count_label.config(text=f"{cookie_count} cookies")
    
def buy_click_upgrade():
    global cookie_count, click_power
    cost = 10 * click_power
    if cookie_count >= cost:
        click_power += 1
        cookie_count -= cost
        power_label.config(text=f"Click power: {click_power}")
        count_label.config(text=f"{cookie_count} cookies")
        upgrade_button.config(text=f"Buy click upgrade (cost: {10*click_power} cookies)")
        status_label.config(text="Click upgrade purchased.")
    else:
        status_label.config(text="Not enough cookies to buy click upgrade.")
        
def buy_auto_click():
    global cookie_count, auto_click_cost, auto_click_power, auto_click_interval
    if cookie_count >= auto_click_cost:
        auto_click_power += 1
        cookie_count -= auto_click_cost
        count_label.config(text=f"{cookie_count} cookies")
        auto_click_cost = int(auto_click_cost * 1.5) # increase cost by 50%
        auto_click_button.config(text=f"Buy auto-click (cost: {auto_click_cost} cookies, power: {auto_click_power})")
        status_label.config(text="Auto-click purchased.")
        auto_click()
    else:
        status_label.config(text="Not enough cookies to buy auto-click.")
        
def auto_click():
    update_count()  # auto-click also counts as a click
    root.after(auto_click_interval, auto_click)  # call auto_click() again after interval
    
def quit_game():
    root.destroy()

root = tk.Tk()
root.title("Cookie Clicker")

count_label = tk.Label(root, text=f"{cookie_count} cookies")
count_label.pack()

click_button = tk.Button(root, text="Click me!", command=update_count)
click_button.pack()

power_label = tk.Label(root, text=f"Click power: {click_power}")
power_label.pack()

upgrade_button = tk.Button(root, text=f"Buy click upgrade (cost: {10*click_power} cookies)", command=buy_click_upgrade)
upgrade_button.pack()

auto_click_button = tk.Button(root, text=f"Buy auto-click (cost: {auto_click_cost} cookies, power: {auto_click_power})", command=buy_auto_click)
auto_click_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

quit_button = tk.Button(root, text="Quit", command=quit_game)
quit_button.pack()

auto_click()  # start auto-clicking

root.mainloop()
