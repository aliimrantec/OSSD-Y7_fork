
import csv
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def save_to_csv(data, filename):

    with open(filename, mode='w', newline='', encoding='utf-8') as file:

        writer = csv.writer(file)

        writer.writerow(["Car Name", "Price"])

        for item in data:

            writer.writerow([item['name'], item['price']])


def get_car_data(car):

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/123.0.0.0 Safari/537.36"
        )
    }

    url = f"https://www.pakwheels.com/new-cars/pricelist/{car}"

    response = requests.get(url, headers=headers)

    car_data = []

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')

        tables = soup.find_all('table')

        for table in tables:

            rows = table.find_all('tr')

            for row in rows:

                cols = row.find_all('td')

                if len(cols) >= 2:

                    name = cols[0].get_text(strip=True)

                    price = cols[1].get_text(strip=True)

                    car_data.append({
                        'name': name,
                        'price': price
                    })

    else:

        messagebox.showerror(
            "Error",
            "Website not responding"
        )

    return car_data


def display_data():

    selected_car = dropdown.get()

    if selected_car == "Select Manufacturer":

        messagebox.showwarning(
            "Warning",
            "Please select a manufacturer"
        )

        return

    car = selected_car.lower()

    data = get_car_data(car)

    text_area.delete(1.0, tk.END)

    if len(data) == 0:

        text_area.insert(
            tk.END,
            "No Data Found"
        )

        return

    for item in data:

        text_area.insert(
            tk.END,
            f"Car Name : {item['name']}\n"
            f"Price     : {item['price']}\n"
            f"{'-'*50}\n"
        )


def save_data():

    selected_car = dropdown.get()

    if selected_car == "Select Manufacturer":

        messagebox.showwarning(
            "Warning",
            "Please select a manufacturer"
        )

        return

    car = selected_car.lower()

    data = get_car_data(car)

    filename = f"{car}_prices.csv"

    save_to_csv(data, filename)

    messagebox.showinfo(
        "Saved",
        f"{filename} saved successfully"
    )


root = tk.Tk()

root.title("Car Price Scraper Pro")

root.geometry("900x650")

root.config(bg="#0f172a")


title = tk.Label(
    root,
    text="Car Price Scraper",
    font=("Segoe UI", 26, "bold"),
    bg="#0f172a",
    fg="white"
)

title.pack(pady=20)


main_frame = tk.Frame(
    root,
    bg="#1e293b",
    bd=0
)

main_frame.pack(
    padx=25,
    pady=10,
    fill="both",
    expand=True
)


top_frame = tk.Frame(
    main_frame,
    bg="#1e293b"
)

top_frame.pack(pady=20)


style = ttk.Style()

style.theme_use("clam")

style.configure(
    "TCombobox",
    fieldbackground="#334155",
    background="#334155",
    foreground="white",
    padding=8
)


cars = [
    "Select Manufacturer",
    "kia",
    "honda",
    "toyota",
    "suzuki",
    "hyundai"
]

dropdown = ttk.Combobox(
    top_frame,
    values=cars,
    font=("Segoe UI", 12),
    width=28,
    state="readonly"
)

dropdown.current(0)

dropdown.grid(
    row=0,
    column=0,
    padx=10
)


find_btn = tk.Button(
    top_frame,
    text="Find Prices",
    command=display_data,
    bg="#22c55e",
    fg="white",
    activebackground="#16a34a",
    activeforeground="white",
    font=("Segoe UI", 11, "bold"),
    relief="flat",
    cursor="hand2",
    padx=20,
    pady=10
)

find_btn.grid(
    row=0,
    column=1,
    padx=10
)


save_btn = tk.Button(
    top_frame,
    text="Save CSV",
    command=save_data,
    bg="#3b82f6",
    fg="white",
    activebackground="#2563eb",
    activeforeground="white",
    font=("Segoe UI", 11, "bold"),
    relief="flat",
    cursor="hand2",
    padx=20,
    pady=10
)

save_btn.grid(
    row=0,
    column=2,
    padx=10
)


text_frame = tk.Frame(
    main_frame,
    bg="#1e293b"
)

text_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)


scrollbar = tk.Scrollbar(text_frame)

scrollbar.pack(
    side="right",
    fill="y"
)


text_area = tk.Text(
    text_frame,
    bg="#0f172a",
    fg="white",
    insertbackground="white",
    font=("Consolas", 11),
    relief="flat",
    padx=15,
    pady=15,
    yscrollcommand=scrollbar.set
)

text_area.pack(
    fill="both",
    expand=True
)

scrollbar.config(command=text_area.yview)


footer = tk.Label(
    root,
    text="Powered by PakWheels Scraper",
    font=("Segoe UI", 9),
    bg="#0f172a",
    fg="#94a3b8"
)

footer.pack(pady=8)


root.mainloop()
