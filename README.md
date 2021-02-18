# AWS Lambda Headless Chrome with Selenium
Up-to-date AWS Lambda layers of headless chrome binary with chrome driver and selenium python package that work out-of-box.

## How to use 
1. Create zip files of each layer. For example, `layers/selenium/python/lib/..` after unzipping should be `python/lib/...`
2. In __AWS Lambda__ go to `Additional resources` -> `Layers` and create layers with any name, upload `.zip` layers, and choose __Python 3.7__ runtime. Due to the size of the binaries, the Chrome layer would require uploading of it through __AWS S3__.
3. To create a function, `Functions` -> `Create function` -> `Author from scratch` and choose `Python 3.7` runtime. In addition, create a new default execution role or use an existing one.
4. Add layers by going in the created function to `Add layer` -> `Custom layers`. Each layer should have the same `Python 3.7` runtime. Even the Chrome one since a layer's runtime requires to be the same as the function.

For testing, import `index.py` in the function with replacing bucket name `your-bucket-name-here`. Be sure, that the role, that is assigned to the function, has access to the bucket.
