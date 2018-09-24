Small Django app to filter alcoholic drinks by category and sort them by their `alcohol / price` ratio.

## Data source

A management command is provided, which can be used to load data from a JSON file into the database. Currently, only the data obtained from the [Systembolaget API](https://www.systembolaget.se/api/) is supported (converted to JSON with the help of [this project](https://github.com/AlexGustafsson/systembolaget-api-fetch)).

Example usage: `./manage.py update_drinks assortment.json`

Subsequent runs will update the database, that is add new drinks if any, and make sure the prices are up-to-date.
