from tkinter import *
import phonenumbers
from phonenumbers import carrier, geocoder
from opencage.geocoder import OpenCageGeocode
import folium
import webbrowser

# Initialize the main application window
root = Tk()
root.title("Phone Number Tracker")
root.geometry("385x594+300+200")
root.resizable(False, False)
root.configure(bg='#96BFFF')

# Replace with your OpenCage API key
API_KEY = "get your free api key from openCage website"

def track():
    """Track the phone number and display its location and carrier."""
    enter_nb = entry.get()
    number = phonenumbers.parse(enter_nb)

    # Get location and carrier information
    location = geocoder.description_for_number(number, 'en')
    country.config(text=location)

    service = carrier.name_for_number(number, 'en')
    sim.config(text=service)

    # Geocode the location to get latitude and longitude
    results = OpenCageGeocode(API_KEY).geocode(location)
    if results:
        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']

        # Create a map with a marker for the location
        myMap = folium.Map(location=[lat, lng], zoom_start=9)
        folium.Marker([lat, lng], popup=location).add_to(myMap)
        myMap.save("myLocation.html")
    else:
        country.config(text="Location not found")

def open_map():
    """Open the generated map in a web browser."""
    webbrowser.open("myLocation.html")

# Load images for the UI
logo = PhotoImage(file="logo.png")
search_icon = PhotoImage(file="search_icon.png")

# Create UI elements
Label(root, image=logo, bg="#96BFFF").place(x=135, y=40)
Label(root, image=search_icon, bg="#96BFFF").place(x=14, y=244)

heading = Label(root, text="Track Number", font='arial 20 bold', fg="#39281E", bg="#96BFFF")
heading.place(x=90, y=190)

entry = StringVar()
enter_nb = Entry(root, textvariable=entry, width=17, justify='center', bd=0, font='arial 20', bg="#2C3541", fg="white")
enter_nb.place(x=54, y=258)

btn = Button(root, image=search_icon, cursor='hand2', bg="#96BFFF", bd=0, command=track, activebackground='#ED8051')
btn.place(x=155, y=308)

country = Label(root, text="Country", bg='#96BFFF', fg='black', font='arial 14 bold')
country.place(x=55, y=370)

sim = Label(root, text="SIM", bg='#96BFFF', fg='black', font='arial 14 bold')
sim.place(x=255, y=370)

open_map_btn = Button(root, text="Location", width=10, cursor='hand2', bg="#EE8C62", bd=0, command=open_map, activebackground='#ED8051', font='arial 14 bold')
open_map_btn.place(x=125, y=430)

insta_page = Label(root, text="@pythonagham", bg='#96BFFF', fg='black', font='arial 10 bold italic')
insta_page.place(x=135, y=550)

# Start the main event loop
root.mainloop()
