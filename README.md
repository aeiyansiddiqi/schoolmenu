# 🍽️ Campus Eats

**Campus Eats** is a utility tool that scrapes the daily menu from the **University of Guelph's dining services** website and enriches it by generating relevant **food images** alongside each item.

> Half the time, I don’t even know what the menu item means — so this tool helps visualize the meal and shows dining hall hours, too.

---

## 📌 Features

- 🔍 **Scrapes menu data** from University of Guelph's campus dining page
- 🖼️ **Generates AI-powered images** based on each food item name
- 🕒 **Displays meal times and availability** for each dining location
- ⚡ Fast, automated updates for each day’s meals

---

## 💡 Why It Exists

Menus are often vague or unfamiliar. If you're tired of seeing names like *"Chicken Provençal"* or *"Root Vegetable Tagine"* and wondering what on earth that means — Campus Eats gives you a quick visual and context before you decide.

---

## 🛠️ Tech Stack

| Tech         | Purpose                            |
|--------------|------------------------------------|
| Python       | Core language                      |
| BeautifulSoup / Requests | Web scraping the menu     |
| Google API   | Image generation for menu items |
| HTML/CSS/JavaScript     | Output formatting (if UI used)     |

---

## 🚀 How to Run

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/campus-eats.git
cd campus-eats
