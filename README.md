# AWS Lambda Headless Chrome with Selenium
Up-to-date AWS Lambda layers of Headless Chrome binary with Chrome driver and Selenium Python package that work out-of-box and make work with Selenium on AWS Lambda more transparent.

## How to use 
1. Create zip files of each layer. So, if you'd unzip `layers/selenium/python/lib/..` back it should be `python/lib/...`, and `layers/chrome/chrome/...` should be `chrome/...`.
2. In __AWS Lambda__ go to `Additional resources` -> `Layers` and create layers with any name. Upload zip file of a layer and select __Python 3.7__ runtime. Due to the Chrome layer binaries size, it would require uploading it through __AWS S3__.
3. To create a function, `Functions` -> `Create function` -> `Author from scratch` and select `Python 3.7` runtime. In addition, remember create a new default execution role or use an existing one.
4. Add layers to the function by going to `Add layer` -> `Custom layers`. Each layer should have the same `Python 3.7` runtime. Even the Chrome one since a layer's runtime requires to be the same as the function's.

For testing, import `index.py` to the function and replace bucket name `your-bucket-name-here` in the code. Be sure, that the role, that is assigned to the function, has access to the bucket.
