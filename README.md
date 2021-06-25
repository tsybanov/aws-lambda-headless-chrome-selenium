# AWS Lambda Headless Chrome with Selenium
AWS Lambda layers of Headless Chrome binary with Chrome driver and Selenium Python package that work out-of-box and make work with Selenium on AWS Lambda more transparent.

## How to use 
1. Create two zip archieves. The first archive should have content of `layers/selenium/python/`, so on unzipping it has to be `python/lib/...`, and the second archive should have content of `layers/chrome/chrome/`, so on unzipping it has to be `chrome/...` (second chrome folder).
2. In __AWS Lambda__ go to `Additional resources` -> `Layers` and create two layers with arbitrary names.
3. Upload zip archives to each layer accordingly and select __Python 3.7__ runtime. The Chrome layer binaries size requires uploading it through __AWS S3__.
4. To create a function, go to `Functions` -> `Create function` -> `Author from scratch` and select `Python 3.7` runtime. In addition, remember create a new default execution role or use an existing one.
5. Add layers to the function by going to `Add layer` -> `Custom layers`. Each layer, including the `Chrome` one, should have the same runtime, `Python 3.7` runtime, since a layer's runtime requires to be the same as with a function.

For testing, import `index.py` to the function and replace bucket name `your-bucket-name-here` in the code. Be sure that the role that is assigned to the function has access to the bucket for screenshots uploading.
