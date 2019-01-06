Welcome to Tradenity Python SDK!
=====================

## Installation

Install it using pip tool:

    `pip install tradenity`

Or Add this line to your application's requirements.txt:

```python
tradenity==0.1.1
```

And then execute:

    `pip install -r requirements.txt`



## Usage

### Initialise the library with your store api key and framework:

`Tradenity.API_KEY = 'sk_1234567'`
`Tradenity.TOKEN_HOLDER = FlaskAuthTokenHolder`

### Invoke the required method, for example to get a list of all the categories for that store:

`Category.find_all()`


Detailed documentation can be found on our [knowledge base site](http://docs.tradenity.com/kb/sdk/python/).




## Contributing

1. Fork it ( https://github.com/tradenity/tradenity-python-sdk/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request
