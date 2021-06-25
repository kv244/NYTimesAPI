# coding: utf-8

"""
    Article Search

    Use the Article Search API to look up articles by keyword.  You can refine your search using filters and facets.  ``` /articlesearch.json?q={query}&fq={filter} ```  ## Example Call ``` https://api.nytimes.com/svc/search/v2/articlesearch.json?q=election&api-key=yourkey ```  ## FILTERING YOUR SEARCH Use filters to narrow the scope of your search. You can specify the fields and the values that your query will be filtered on. The Article Search API uses [Elasticsearch](https://www.elastic.co/), so the filter query uses standard [Lucene syntax](http://www.lucenetutorial.com/lucene-query-syntax.html). Separate the filter field name and value with a colon, and surround multiple values with parentheses.  ``` field-name:(\"value1\" \"value2\" ... \"value n\") ```  The default connector for values in parentheses is OR. If you declare an explicit boolean value, it must be capitalized.  You can filter on multiple values and fields.  ``` field-name-1:(\"value1\") AND field-name-2:(\"value2\" \"value3\") ```  For a list of all fields you can filter on, see the Filter Query Fields table below.  ### Pagination The Article Search API returns a max of 10 results at a time. The meta node in the response contains the total number of matches (\"hits\") and the current offset. Use the page query parameter to paginate thru results (page=0 for results 1-10, page=1 for 11-20, ...). You can paginate thru up to 100 pages (1,000 results). If you get too many results try filtering by date range.  ### Filter Query Examples Restrict your search to articles with The New York Times as the source:  ``` fq=source:(\"The New York Times\") ```  Restrict your search to articles from either the Sports or Foreign desk:  ``` fq=news_desk:(\"Sports\" \"Foreign\") ```  Restrict your search to articles that are about New York City and from the Sports desk:  ``` fq=news_desk:(\"Sports\") AND glocations:(\"NEW YORK CITY\") ```  If you do not specify a field, the scope of the filter query will look for matches in the body, headline and byline. The example below will restrict your search to articles with The New York Times in the body, headline or byline:  ``` fq=The New York Times ```  ### Filter Query Fields Field                     | Behavior ------------------------- | --------------- body                      | Multiple tokens body.search               | Left-edge n-grams creative_works            | Single token creative_works.contains   | Multiple tokens day_of_week               | Single token document_type             | Case-sensitive exact match glocations                | Single token glocations.contains       | Multiple tokens headline                  | Multiple tokens headline.search           | Left-edge n-grams kicker                    | Single token kicker.contains           | Multiple tokens news_desk                 | Single token news_desk.contains        | Multiple tokens organizations             | Single token organizations.contains    | Multiple tokens persons                   | Single token persons.contains          | Multiple tokens pub_date                  | Timestamp (YYYY-MM-DD) pub_year                  | Integer secpg                     | Multiple tokens source                    | Single token source.contains           | Multiple tokens subject                   | Single token subject.contains          | Multiple tokens section_name              | Single token section_name.contains     | Multiple tokens type_of_material          | Single token type_of_material.contains | Multiple tokens web_url                   | Single token (case-sensitive) word_count                | Integer  #### News Desk Values * Adventure Sports * Arts & Leisure * Arts * Automobiles * Blogs * Books * Booming * Business Day * Business * Cars * Circuits * Classifieds * Connecticut * Crosswords & Games * Culture * DealBook * Dining * Editorial * Education * Energy * Entrepreneurs * Environment * Escapes * Fashion & Style * Fashion * Favorites * Financial * Flight * Food * Foreign * Generations * Giving * Global Home * Health & Fitness * Health * Home & Garden * Home * Jobs * Key * Letters * Long Island * Magazine * Market Place * Media * Men's Health * Metro * Metropolitan * Movies * Museums * National * Nesting * Obits * Obituaries * Obituary * OpEd * Opinion * Outlook * Personal Investing * Personal Tech * Play * Politics * Regionals * Retail * Retirement * Science * Small Business * Society * Sports * Style * Sunday Business * Sunday Review * Sunday Styles * T Magazine * T Style * Technology * Teens * Television * The Arts * The Business of Green * The City Desk * The City * The Marathon * The Millennium * The Natural World * The Upshot * The Weekend * The Year in Pictures * Theater * Then & Now * Thursday Styles * Times Topics * Travel * U.S. * Universal * Upshot * UrbanEye * Vacation * Washington * Wealth * Weather * Week in Review * Week * Weekend * Westchester * Wireless Living * Women's Health * Working * Workplace * World * Your Money  #### Section Name Values * Arts * Automobiles * Autos * Blogs * Books * Booming * Business * Business Day * Corrections * Crosswords & Games * Crosswords/Games * Dining & Wine * Dining and Wine * Editors' Notes * Education * Fashion & Style * Food * Front Page * Giving * Global Home * Great Homes & Destinations * Great Homes and Destinations * Health * Home & Garden * Home and Garden * International Home * Job Market * Learning * Magazine * Movies * Multimedia * Multimedia/Photos * N.Y. / Region * N.Y./Region * NYRegion * NYT Now * National * New York * New York and Region * Obituaries * Olympics * Open * Opinion * Paid Death Notices * Public Editor * Real Estate * Science * Sports * Style * Sunday Magazine * Sunday Review * T Magazine * T:Style * Technology * The Public Editor * The Upshot * Theater * Times Topics * TimesMachine * Today's Headlines * Topics * Travel * U.S. * Universal * UrbanEye * Washington * Week in Review * World * Your Money  #### Type of Material Values * Addendum * An Analysis * An Appraisal * Archives * Article * Banner * Biography * Birth Notice * Blog * Brief * Caption * Chronology * Column * Correction * Economic Analysis * Editorial * Editorial Cartoon * Editors' Note * First Chapter * Front Page * Glossary * Interactive Feature * Interactive Graphic * Interview * Letter * List * Marriage Announcement * Military Analysis * News * News Analysis * Newsletter * Obituary * Obituary (Obit) * Op-Ed * Paid Death Notice * Postscript * Premium * Question * Quote * Recipe * Review * Schedule * SectionFront * Series * Slideshow * Special Report * Statistics * Summary * Text * Video * Web Log  ## USING FACETS Use facets to view the relative importance of certain fields to a search term, and gain insight about how to best refine your queries and filter your search results.  The following fields can be used as facet fields: day_of_week, document_type, ingredients, news_desk, pub_month, pub_year, section_name, source, subsection_name, and type_of_material.  Specify facets using the facet_fields parameter. Set facet=true and the response will contain an array with a count for the five terms that have the highest count for each facet. For example, including the following in your request will add a facet array with a count for the top five days of the week to the response.  ``` facet_fields=day_of_week&facet=true ```  By default, facet counts ignore all filters and return the count for all results of a query. For the following queries, the facet count in each response will be identical, even though the results returned in one set is restricted to articles published in 2012.  ``` q=obama&facet_fields=source&facet=true&begin_date=20120101&end_date=20121231 ```  You can force facet counts to respect filters by setting facet_filter=true. Facet counts will be restricted based on any filters you have specified (this includes both explicit filter queries set using the fq parameter and implicit filters like begin_date).  Here is the facet array response to the query. ```javascript \"facets\": {   \"source\": {     \"_type\": \"terms\",     \"missing\": 524,     \"total\": 83121,     \"other\": 317,     \"terms\": [       {         \"term\": \"The New York Times\",         \"count\": 68530       },       {         \"term\": \"AP\",         \"count\": 7705       },       {         \"term\": \"Reuters\",         \"count\": 4969       },       {         \"term\": \"International Herald Tribune\",         \"count\": 1464       },       {         \"term\": \"\",         \"count\": 136       }     ]   } } ``` If you set facet_filter to true the facet array will only count facet occurences in 2012. ```javascript facets\": {   \"source\": {     \"_type\": \"terms\",     \"missing\": 192,     \"total\": 22596,     \"other\": 139,     \"terms\": [       {         \"term\": \"The New York Times\",         \"count\": 14812       },       ... ``` ### Examples Requests Search for documents containing 'new york times' and return results 20-29 with results sorted oldest first.  ``` https://api.nytimes.com/svc/search/v2/articlesearch.json?q=new+york+times&page=2&sort=oldest&api-key=your-api-key ``` Search for all documents published on January 1, 2012 containing 'romney'.  Facet count will be returned for 'day_of_week' and will be reflective of all documents (i.e., the date range filter and filter query do not affect facet counts).  ``` https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=romney&facet_field=day_of_week&facet=true&begin_date=20120101&end_date=20120101&api-key=your-api-key ```  ### Example Response Here is an partial example response.  ```javascript {   \"response\": {     \"meta\": {       \"hits\": 25,       \"time\": 332,       \"offset\": 0     },     \"docs\": [       {         \"web_url\": \"http://thecaucus.blogs.nytimes.com/2012/01/01/virginia-attorney-general-backs-off-ballot-proposal/\",         \"snippet\": \"Virginia's attorney general on Sunday backed off of a proposal to loosen the state's ballot access rules to allow more Republican presidential candidates to qualify.\",         \"lead_paragraph\": \"DES MOINES -- Virginia's attorney general on Sunday backed off of a proposal to loosen the state's ballot access rules to allow more Republican presidential candidates to qualify.\",         ...       }     ],     \"facets\": {         \"day_of_week\": {             \"_type\": \"terms\",             \"missing\": 1871790,             \"total\": 13098462,             \"other\": 3005891,             \"terms\": [               {                 \"term\": \"Sunday\",                 \"count\": 3122347               },               ... ```  ### Limit Fields in Response You can limit the number fields returned in the response with the fl parameter. ``` fl=web_url ```   # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import copy
import logging
import multiprocessing
import sys
import urllib3

import six
from six.moves import http_client as httplib


class Configuration(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Ref: https://github.com/swagger-api/swagger-codegen
    Do not edit the class manually.
    """

    _default = None

    def __init__(self):
        """Constructor"""
        if self._default:
            for key in self._default.__dict__.keys():
                self.__dict__[key] = copy.copy(self._default.__dict__[key])
            return

        # Default Base url
        self.host = "https://api.nytimes.com/svc/search/v2"
        # Temp file folder for downloading files
        self.temp_folder_path = None

        # Authentication Settings
        # dict to store API key(s)
        self.api_key = {}
        # dict to store API prefix (e.g. Bearer)
        self.api_key_prefix = {}
        # function to refresh API key if expired
        self.refresh_api_key_hook = None
        # Username for HTTP basic authentication
        self.username = ""
        # Password for HTTP basic authentication
        self.password = ""

        # Logging Settings
        self.logger = {}
        self.logger["package_logger"] = logging.getLogger("swagger_client")
        self.logger["urllib3_logger"] = logging.getLogger("urllib3")
        # Log format
        self.logger_format = '%(asctime)s %(levelname)s %(message)s'
        # Log stream handler
        self.logger_stream_handler = None
        # Log file handler
        self.logger_file_handler = None
        # Debug file location
        self.logger_file = None
        # Debug switch
        self.debug = False

        # SSL/TLS verification
        # Set this to false to skip verifying SSL certificate when calling API
        # from https server.
        self.verify_ssl = True
        # Set this to customize the certificate file to verify the peer.
        self.ssl_ca_cert = None
        # client certificate file
        self.cert_file = None
        # client key file
        self.key_file = None
        # Set this to True/False to enable/disable SSL hostname verification.
        self.assert_hostname = None

        # urllib3 connection pool's maximum number of connections saved
        # per pool. urllib3 uses 1 connection as default value, but this is
        # not the best value when you are making a lot of possibly parallel
        # requests to the same host, which is often the case here.
        # cpu_count * 5 is used as default value to increase performance.
        self.connection_pool_maxsize = multiprocessing.cpu_count() * 5

        # Proxy URL
        self.proxy = None
        # Safe chars for path_param
        self.safe_chars_for_path_param = ''

        # Disable client side validation
        self.client_side_validation = True

    @classmethod
    def set_default(cls, default):
        cls._default = default

    @property
    def logger_file(self):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        self.__logger_file = value
        if self.__logger_file:
            # If set logging file,
            # then add file handler and remove stream handler.
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in six.iteritems(self.logger):
                logger.addHandler(self.logger_file_handler)
                if self.logger_stream_handler:
                    logger.removeHandler(self.logger_stream_handler)
        else:
            # If not set logging file,
            # then add stream handler and remove file handler.
            self.logger_stream_handler = logging.StreamHandler()
            self.logger_stream_handler.setFormatter(self.logger_formatter)
            for _, logger in six.iteritems(self.logger):
                logger.addHandler(self.logger_stream_handler)
                if self.logger_file_handler:
                    logger.removeHandler(self.logger_file_handler)

    @property
    def debug(self):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        return self.__debug

    @debug.setter
    def debug(self, value):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        self.__debug = value
        if self.__debug:
            # if debug status is True, turn on debug logging
            for _, logger in six.iteritems(self.logger):
                logger.setLevel(logging.DEBUG)
            # turn on httplib debug
            httplib.HTTPConnection.debuglevel = 1
        else:
            # if debug status is False, turn off debug logging,
            # setting log level to default `logging.WARNING`
            for _, logger in six.iteritems(self.logger):
                logger.setLevel(logging.WARNING)
            # turn off httplib debug
            httplib.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def get_api_key_with_prefix(self, identifier):
        """Gets API key (with prefix if set).

        :param identifier: The identifier of apiKey.
        :return: The token for api key authentication.
        """

        if self.refresh_api_key_hook:
            self.refresh_api_key_hook(self)

        key = self.api_key.get(identifier)
        if key:
            prefix = self.api_key_prefix.get(identifier)
            if prefix:
                return "%s %s" % (prefix, key)
            else:
                return key

    def get_basic_auth_token(self):
        """Gets HTTP basic authentication header (string).

        :return: The token for basic HTTP authentication.
        """
        return urllib3.util.make_headers(
            basic_auth=self.username + ':' + self.password
        ).get('authorization')

    def auth_settings(self):
        """Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        """
        return {
            'apikey':
                {
                    'type': 'api_key',
                    'in': 'query',
                    'key': 'api-key',
                    'value': self.get_api_key_with_prefix('api-key')
                },

        }

    def to_debug_report(self):
        """Gets the essential information for debugging.

        :return: The report for debugging.
        """
        return "Python SDK Debug Report:\n"\
               "OS: {env}\n"\
               "Python Version: {pyversion}\n"\
               "Version of the API: 2.0.0\n"\
               "SDK Package Version: 1.0.0".\
               format(env=sys.platform, pyversion=sys.version)
