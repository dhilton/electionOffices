# What is this?

This Scrapy project, scrapes the list of local authorities who are responsible
for organising elections at a local level. It generates a set of items which
can be exported to csv / json / xml via scrapy for further processing.

## Why do this?

Annoyed at the lack of a single polling station dataset, I thought this may
help find the way to building a better dataset. This will be hard however
as this data lacks any sense of sensible identifiers for matching a textual address
to a local authority. However, we may be able to match on a combination of
website domain and postcode, with some exception handling for those that fail
those heuristics.

The aim is to `LA -> website -> polling station dataset` with a view to building
another scrapy project to parse the various councils ways of publishing polling
station data via some sort of plugin/driver architecture (for example, Bristol publishes
  this data via ArcGIS and Warrington has published it in a pdf generated from some
  election software).  

## How to install & return

1. Create a new virtualenv
2. Activate and `pip install -r requirements.txt`
3. cd ./election_offices/election_offices/
4. Run the scrapy crawler: `scrapy runspider ./spiders/list_of_election_offices.py -o offices.json`

This will output a simple (but a bit dirty) json document containing 331 local authorities - which
seems to be at odds with http://opendatacommunities.org/data/local-authorities which reports 327.
