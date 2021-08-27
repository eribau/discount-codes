# Discount codes

This is a simple application demonstrating an API for creating and getting discount codes.

## Installing and running
The application has been developed and tested on Python 3.9.5

Install necessary packages:

`pip install -r requirements.txt`

Run application:

`uvicorn main:app`

This starts a uvicorn server on  http://127.0.0.1:8000

You can access documentation for the API by going to http://127.0.0.1:8000/docs, where you can also try it out

The get and post methods require a brandname to be specified in the URI, to which the discount codes are related. A brand called ´shoez´ already exists in the application, but new ones can be added by simply entering a brandname when sending a post to request new discount codes. 