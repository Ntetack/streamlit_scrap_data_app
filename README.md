# Streamlit Scraping App – Version 0.0

Welcome to **Streamlit Scraping App**, a simple and intuitive application that allows you to:

* **Scrape** data from multiple categories (e.g., clothes, shoes, etc.)
* **Visualize interactive charts**
* **Store scraping history** in a SQLite database
* **Download the results**
* **Provide feedback** via Google Form or KoboToolbox

This is **version 0.0**, the first public and functional version of the app.



## Main Features

### Scraping

* Dynamic web scraping of selected pages
* Unique **UUID** for each scraping session
* Automatic storage in SQLite (`scraped_data.db`)

### Dashboard & Visualization

* Matplotlib charts integrated into Streamlit
* Top products, top locations, most expensive products, etc.
* Automatic data cleaning (price formatting, duplicates removed)

### Scraping History

* View previous scraping sessions
* Filter by scraping ID
* Download datasets from any session

### Evaluation Page

* Choice between:

  * Google Form
  * KoboToolbox
* Immediate redirection via buttons



## Installation

### 1. Clone the GitHub repository

```bash
git clone https://github.com/your-username/streamlit_scrap_data_app.git
cd streamlit_scrap_data_app
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
streamlit run apps/app_2/app.py
```

> The main script is located at:
> **apps/app_2/app.py**



## Project Structure

```
streamlit_scrap_data_app/
│── apps/
│   └── app_2/
│       └── app.py
│
│── media/
│── template/
│── scraped_data.db
│── requirements.txt
│── README.md
```



## SQLite Database

The app automatically creates the database:

```
scraped_data.db
```

Containing a table:

```
products
```


## Deployment


All dependencies are listed in:

```
requirements.txt
```



## Contributions

Contributions are welcome to:

* Add new scraping sources
* Improve visualizations
* Optimize performance

Open an *issue* or *pull request*.



## License

Open-source project under the MIT License.

---

## Credits

* Developed by **Ntetack**
* Thank you to **pradofernando** [https://github.com/microsoft/Streamlit_UI_Template](https://github.com/microsoft/Streamlit_UI_Template) for the CSS template


**Install the necessary libraries**
** We advise to create an environment
```
pip install -r requirements.txt  
```

**Navigate to either the /app_2**


Navigation to /app_2:
```
cd apps/app_2
```

**Run the streamlit application**

```
streamlit run home.py
```

Command for app_2:
```
