# 🪙 how_much_BTC 🕒

This small Python project fetches the **real-time price of Bitcoin (BTC)** in USD using the **CoinMarketCap** public API.

---

## 🚀 What is this project about?

This script uses Python libraries such as `requests`, `json`, and `datetime` to:
- Connect to the CoinMarketCap API
- Request the current Bitcoin price in USD
- Display the price along with the **current date and time**

Example output:
```
The price of Bitcoin on date 2025-05-12 and time 14:01:32 is: ** 104303.4319 $ **
```

---

## ❗ Challenges I faced

🌐 **Working with APIs** was a new experience. These were the main challenges:
- Learning how to **authenticate** and use API keys
- Understanding how to **structure requests and parameters**
- Navigating through **JSON responses** to extract the required data
- Handling errors like `ConnectionError`, `Timeout`, and `TooManyRedirects`

🔑 I also had to register for a **free API key** from CoinMarketCap and read their documentation to understand:
- How to structure the URL
- What headers and parameters are required
- How the data is formatted

---

## 📚 What I learned

📌 Each API service (like CoinMarketCap) provides its own **documentation** for:
- How to send requests
- What data is returned
- What endpoints and query parameters are allowed

📎 I learned how to:
- Use `requests` and `Session` to send API calls
- Parse nested JSON data
- Format timestamps and show clean output
- Work with exceptions to make my code more stable

---

## 🛠 Technologies Used
- Python 🐍
- `requests` for HTTP requests
- `json` for parsing data
- `datetime` for timestamp formatting
- CoinMarketCap Public API

---

## 📝 How to run this project

1. Clone the repo or copy the script to your local machine
    ```bash
    git clone https://github.com/4mirhoseinhasani/how_much_BTC.git
    cd how_much_BTC
2. Create a virtual environment (optional but recommended)
    ```bash
    python -m venv venv
3. Activate the virtual environment
    #On Windows:
    ```bash
    venv\Scripts\activate
    ```
    #On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```
4. Install required dependencies
    ```bash
    pip install -r requirements.txt
    ```
5. Replace the `X-CMC_PRO_API_KEY` value with your own key from [CoinMarketCap](https://coinmarketcap.com/api/)
5. Run the Python script:
    ```bash
   python main.py
    ```

---
🗺️ Location
📍 Region: Zanjan, Iran

🔐 Don't forget:
Get your free API key from CoinMarketCap to make this script work. It's fast and easy!

📫 Feel free to **fork** or **star** if this was helpful!
