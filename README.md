Welcome to Python SDK for Tradenity ecommerce API!
=====================

This is python SDK for [Tradenity ecommerce API](https://www.tradenity.com).
This SDK makes developing and building python ecommerce application really easy. 

## Installation

Install it using pip tool:

    `pip install tradenity`

Or Add this line to your application's requirements.txt:

```python
tradenity==1.0.1
```

And then execute:

    `pip install -r requirements.txt`



## Usage

### Initialise the library with your store api key :
```python
from tradenity import Configuration

Configuration.API_KEY = 'sk_xxxxxxxxxxxxxxxxxxxxxxxx'
```

### Invoke the required method, for example to get a list of all the categories for that store:

`Category.find_all()`


Detailed documentation can be found on our [knowledge base site](http://docs.tradenity.com/kb/sdk/python/).


## Extensions for common Python frameworks

These libraries eases the integration between Tradenity SDK and the corresponding framework:

[Django framework extension library](https://github.com/tradenity/python-sdk-django-ext).

[Flask framework  extension library](https://github.com/tradenity/python-sdk-flask-ext).


## Tutorials and sample applications

We provide 2 sample applications, actually it is the same application implemented using 2 frameworks: `Django`, and `Flask`.
You can find live demo here:

[Camera store sample application live demo](http://camera-store-sample.tradenity.com/)

You can find the code at github:

[Camera store for django code](https://github.com/tradenity/camerastore-python-django-sample).

[Camera store for flask code](https://github.com/tradenity/camerastore-python-flask-sample).

We also provide a detailed explanation of the code of these sample applications in the form of a step by step tutorials:

[Camera store for django tutorial](http://docs.tradenity.com/kb/tutorials/python/django/).

[Camera store for flask tutorial](http://docs.tradenity.com/kb/tutorials/python/flask/).



## Contributing

1. Fork it ( https://github.com/tradenity/tradenity-python-sdk/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request
