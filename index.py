import boto3
from selenium import webdriver

def handler(event, context):
    chrome_options = webdriver.ChromeOptions()
    required_args = ["--no-sandbox", "--headless", "--disable-gpu", "--disable-dev-shm-usage", "--single-process",
                     "--remote-debugging-port=9222"]
    optional_args = ["--window-size=1280x1696", "--hide-scrollbars", "--enable-logging", "--log-level=0"]

    for arg in required_args + optional_args:
        chrome_options.add_argument(arg)

    chrome_options.binary_location = "/opt/chrome/headless-chromium"
    driver = webdriver.Chrome("/opt/chrome/chromedriver", options=chrome_options)

    driver.get("https://github.com/")

    screenshot_filename = "screenshot.png"
    screenshot_path = "/tmp/" + screenshot_filename
    driver.save_screenshot(screenshot_path)
    s3 = boto3.client("s3")
    s3.put_object(Bucket="your-bucket-name-here", Key=screenshot_filename, Body=open(screenshot_path, "rb"))
    
    driver.quit()
    return 1