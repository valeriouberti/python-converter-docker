# Python Currency Converter
## Running the project

Run it by using docker.
First of all you have to install docker on your system.


Installation example
```sh
$ docker build -t converter-docker .
$ docker run -d -p 5000:5000 converter-docker
```

## Conventions / Glossary 

- reference date for the exchange rate, in YYYY-MM-DD format
- ISO currency code for the destination currency to convert (e.g. EUR,
USD, GBP).
-  ISO currency code for the source currency to convert (e.g. EUR,
USD, GBP).
- the amount to convert (e.g. 12.35) in floating point

## Endpoints
### API
- the endpoint 
`GET http://0.0.0.0:5000/convert/<reference_date>/<float:current_amount>/<src_currency>/<dest_currency>` 
will return a JSON object like this:
```
{
“amount”: 20.23,
“currency”: ”EUR”,
}
```

Example:
`$ curl http://0.0.0.0:5000/convert/2019-10-16/12.0/GBP/CHF`
