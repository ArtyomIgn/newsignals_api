# News Checker Script

This Python script checks for new news and probabilities from the newsignals API at regular intervals and logs any new items found. It uses the `requests` library for HTTP requests.

You can modify this script to suit your needs. The request limit is 1 per second.

example.py - example how to make 1 request (you will get the latest 10 news)
example_prod.py - your first request will retrieve the latest 10 news items, and subsequent news will appear one by one in online mode

## Requirements

- Python 3.x
- `requests` library (version 2.32.3)

## Setup Instructions

### 1. Create a Virtual Environment

To isolate the dependencies for this project, it's recommended to create a virtual environment.

#### On macOS / Linux

1. Open a terminal.
2. Run the following command to create a virtual environment:

    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:

    ```bash
    source venv/bin/activate
    ```

#### On Windows

1. Open a command prompt or PowerShell.
2. Run the following command to create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

- For Command Prompt:

    ```cmd
    venv\Scripts\activate
    ```

- For PowerShell:

    ```powershell
    venv\Scripts\Activate.ps1
    ```

### 2. Install Dependencies

With the virtual environment activated, install the required libraries by running:

```bash
pip install -r requirements.txt
```

### 3. Running the Script

```bash
python example.py
python example_prod.py > output.log 2>&1 # creating a file with news that is regularly updated online
```
### 4. Result in file 'output.txt' from python example_prod.py > output.log 2>&1 

2024-09-12 13:07:00 - INFO - New news found: {'published_primary_source': '2024-09-12 13:07:00 UTC', 'tickers': 'YGMZ', 'probability': '56'}
2024-09-12 12:31:00 - INFO - New news found: {'published_primary_source': '2024-09-12 12:31:00 UTC', 'tickers': 'FLUX', 'probability': '99'}

