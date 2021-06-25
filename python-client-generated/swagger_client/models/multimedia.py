# coding: utf-8

"""
    Article Search

    Use the Article Search API to look up articles by keyword.  You can refine your search using filters and facets.  ``` /articlesearch.json?q={query}&fq={filter} ```  ## Example Call ``` https://api.nytimes.com/svc/search/v2/articlesearch.json?q=election&api-key=yourkey ```  ## FILTERING YOUR SEARCH Use filters to narrow the scope of your search. You can specify the fields and the values that your query will be filtered on. The Article Search API uses [Elasticsearch](https://www.elastic.co/), so the filter query uses standard [Lucene syntax](http://www.lucenetutorial.com/lucene-query-syntax.html). Separate the filter field name and value with a colon, and surround multiple values with parentheses.  ``` field-name:(\"value1\" \"value2\" ... \"value n\") ```  The default connector for values in parentheses is OR. If you declare an explicit boolean value, it must be capitalized.  You can filter on multiple values and fields.  ``` field-name-1:(\"value1\") AND field-name-2:(\"value2\" \"value3\") ```  For a list of all fields you can filter on, see the Filter Query Fields table below.  ### Pagination The Article Search API returns a max of 10 results at a time. The meta node in the response contains the total number of matches (\"hits\") and the current offset. Use the page query parameter to paginate thru results (page=0 for results 1-10, page=1 for 11-20, ...). You can paginate thru up to 100 pages (1,000 results). If you get too many results try filtering by date range.  ### Filter Query Examples Restrict your search to articles with The New York Times as the source:  ``` fq=source:(\"The New York Times\") ```  Restrict your search to articles from either the Sports or Foreign desk:  ``` fq=news_desk:(\"Sports\" \"Foreign\") ```  Restrict your search to articles that are about New York City and from the Sports desk:  ``` fq=news_desk:(\"Sports\") AND glocations:(\"NEW YORK CITY\") ```  If you do not specify a field, the scope of the filter query will look for matches in the body, headline and byline. The example below will restrict your search to articles with The New York Times in the body, headline or byline:  ``` fq=The New York Times ```  ### Filter Query Fields Field                     | Behavior ------------------------- | --------------- body                      | Multiple tokens body.search               | Left-edge n-grams creative_works            | Single token creative_works.contains   | Multiple tokens day_of_week               | Single token document_type             | Case-sensitive exact match glocations                | Single token glocations.contains       | Multiple tokens headline                  | Multiple tokens headline.search           | Left-edge n-grams kicker                    | Single token kicker.contains           | Multiple tokens news_desk                 | Single token news_desk.contains        | Multiple tokens organizations             | Single token organizations.contains    | Multiple tokens persons                   | Single token persons.contains          | Multiple tokens pub_date                  | Timestamp (YYYY-MM-DD) pub_year                  | Integer secpg                     | Multiple tokens source                    | Single token source.contains           | Multiple tokens subject                   | Single token subject.contains          | Multiple tokens section_name              | Single token section_name.contains     | Multiple tokens type_of_material          | Single token type_of_material.contains | Multiple tokens web_url                   | Single token (case-sensitive) word_count                | Integer  #### News Desk Values * Adventure Sports * Arts & Leisure * Arts * Automobiles * Blogs * Books * Booming * Business Day * Business * Cars * Circuits * Classifieds * Connecticut * Crosswords & Games * Culture * DealBook * Dining * Editorial * Education * Energy * Entrepreneurs * Environment * Escapes * Fashion & Style * Fashion * Favorites * Financial * Flight * Food * Foreign * Generations * Giving * Global Home * Health & Fitness * Health * Home & Garden * Home * Jobs * Key * Letters * Long Island * Magazine * Market Place * Media * Men's Health * Metro * Metropolitan * Movies * Museums * National * Nesting * Obits * Obituaries * Obituary * OpEd * Opinion * Outlook * Personal Investing * Personal Tech * Play * Politics * Regionals * Retail * Retirement * Science * Small Business * Society * Sports * Style * Sunday Business * Sunday Review * Sunday Styles * T Magazine * T Style * Technology * Teens * Television * The Arts * The Business of Green * The City Desk * The City * The Marathon * The Millennium * The Natural World * The Upshot * The Weekend * The Year in Pictures * Theater * Then & Now * Thursday Styles * Times Topics * Travel * U.S. * Universal * Upshot * UrbanEye * Vacation * Washington * Wealth * Weather * Week in Review * Week * Weekend * Westchester * Wireless Living * Women's Health * Working * Workplace * World * Your Money  #### Section Name Values * Arts * Automobiles * Autos * Blogs * Books * Booming * Business * Business Day * Corrections * Crosswords & Games * Crosswords/Games * Dining & Wine * Dining and Wine * Editors' Notes * Education * Fashion & Style * Food * Front Page * Giving * Global Home * Great Homes & Destinations * Great Homes and Destinations * Health * Home & Garden * Home and Garden * International Home * Job Market * Learning * Magazine * Movies * Multimedia * Multimedia/Photos * N.Y. / Region * N.Y./Region * NYRegion * NYT Now * National * New York * New York and Region * Obituaries * Olympics * Open * Opinion * Paid Death Notices * Public Editor * Real Estate * Science * Sports * Style * Sunday Magazine * Sunday Review * T Magazine * T:Style * Technology * The Public Editor * The Upshot * Theater * Times Topics * TimesMachine * Today's Headlines * Topics * Travel * U.S. * Universal * UrbanEye * Washington * Week in Review * World * Your Money  #### Type of Material Values * Addendum * An Analysis * An Appraisal * Archives * Article * Banner * Biography * Birth Notice * Blog * Brief * Caption * Chronology * Column * Correction * Economic Analysis * Editorial * Editorial Cartoon * Editors' Note * First Chapter * Front Page * Glossary * Interactive Feature * Interactive Graphic * Interview * Letter * List * Marriage Announcement * Military Analysis * News * News Analysis * Newsletter * Obituary * Obituary (Obit) * Op-Ed * Paid Death Notice * Postscript * Premium * Question * Quote * Recipe * Review * Schedule * SectionFront * Series * Slideshow * Special Report * Statistics * Summary * Text * Video * Web Log  ## USING FACETS Use facets to view the relative importance of certain fields to a search term, and gain insight about how to best refine your queries and filter your search results.  The following fields can be used as facet fields: day_of_week, document_type, ingredients, news_desk, pub_month, pub_year, section_name, source, subsection_name, and type_of_material.  Specify facets using the facet_fields parameter. Set facet=true and the response will contain an array with a count for the five terms that have the highest count for each facet. For example, including the following in your request will add a facet array with a count for the top five days of the week to the response.  ``` facet_fields=day_of_week&facet=true ```  By default, facet counts ignore all filters and return the count for all results of a query. For the following queries, the facet count in each response will be identical, even though the results returned in one set is restricted to articles published in 2012.  ``` q=obama&facet_fields=source&facet=true&begin_date=20120101&end_date=20121231 ```  You can force facet counts to respect filters by setting facet_filter=true. Facet counts will be restricted based on any filters you have specified (this includes both explicit filter queries set using the fq parameter and implicit filters like begin_date).  Here is the facet array response to the query. ```javascript \"facets\": {   \"source\": {     \"_type\": \"terms\",     \"missing\": 524,     \"total\": 83121,     \"other\": 317,     \"terms\": [       {         \"term\": \"The New York Times\",         \"count\": 68530       },       {         \"term\": \"AP\",         \"count\": 7705       },       {         \"term\": \"Reuters\",         \"count\": 4969       },       {         \"term\": \"International Herald Tribune\",         \"count\": 1464       },       {         \"term\": \"\",         \"count\": 136       }     ]   } } ``` If you set facet_filter to true the facet array will only count facet occurences in 2012. ```javascript facets\": {   \"source\": {     \"_type\": \"terms\",     \"missing\": 192,     \"total\": 22596,     \"other\": 139,     \"terms\": [       {         \"term\": \"The New York Times\",         \"count\": 14812       },       ... ``` ### Examples Requests Search for documents containing 'new york times' and return results 20-29 with results sorted oldest first.  ``` https://api.nytimes.com/svc/search/v2/articlesearch.json?q=new+york+times&page=2&sort=oldest&api-key=your-api-key ``` Search for all documents published on January 1, 2012 containing 'romney'.  Facet count will be returned for 'day_of_week' and will be reflective of all documents (i.e., the date range filter and filter query do not affect facet counts).  ``` https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=romney&facet_field=day_of_week&facet=true&begin_date=20120101&end_date=20120101&api-key=your-api-key ```  ### Example Response Here is an partial example response.  ```javascript {   \"response\": {     \"meta\": {       \"hits\": 25,       \"time\": 332,       \"offset\": 0     },     \"docs\": [       {         \"web_url\": \"http://thecaucus.blogs.nytimes.com/2012/01/01/virginia-attorney-general-backs-off-ballot-proposal/\",         \"snippet\": \"Virginia's attorney general on Sunday backed off of a proposal to loosen the state's ballot access rules to allow more Republican presidential candidates to qualify.\",         \"lead_paragraph\": \"DES MOINES -- Virginia's attorney general on Sunday backed off of a proposal to loosen the state's ballot access rules to allow more Republican presidential candidates to qualify.\",         ...       }     ],     \"facets\": {         \"day_of_week\": {             \"_type\": \"terms\",             \"missing\": 1871790,             \"total\": 13098462,             \"other\": 3005891,             \"terms\": [               {                 \"term\": \"Sunday\",                 \"count\": 3122347               },               ... ```  ### Limit Fields in Response You can limit the number fields returned in the response with the fl parameter. ``` fl=web_url ```   # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class Multimedia(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'rank': 'int',
        'subtype': 'str',
        'caption': 'str',
        'credit': 'str',
        'type': 'str',
        'url': 'str',
        'height': 'int',
        'width': 'int',
        'legacy': 'object',
        'crop_name': 'str'
    }

    attribute_map = {
        'rank': 'rank',
        'subtype': 'subtype',
        'caption': 'caption',
        'credit': 'credit',
        'type': 'type',
        'url': 'url',
        'height': 'height',
        'width': 'width',
        'legacy': 'legacy',
        'crop_name': 'crop_name'
    }

    def __init__(self, rank=None, subtype=None, caption=None, credit=None, type=None, url=None, height=None, width=None, legacy=None, crop_name=None, _configuration=None):  # noqa: E501
        """Multimedia - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._rank = None
        self._subtype = None
        self._caption = None
        self._credit = None
        self._type = None
        self._url = None
        self._height = None
        self._width = None
        self._legacy = None
        self._crop_name = None
        self.discriminator = None

        if rank is not None:
            self.rank = rank
        if subtype is not None:
            self.subtype = subtype
        if caption is not None:
            self.caption = caption
        if credit is not None:
            self.credit = credit
        if type is not None:
            self.type = type
        if url is not None:
            self.url = url
        if height is not None:
            self.height = height
        if width is not None:
            self.width = width
        if legacy is not None:
            self.legacy = legacy
        if crop_name is not None:
            self.crop_name = crop_name

    @property
    def rank(self):
        """Gets the rank of this Multimedia.  # noqa: E501


        :return: The rank of this Multimedia.  # noqa: E501
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this Multimedia.


        :param rank: The rank of this Multimedia.  # noqa: E501
        :type: int
        """

        self._rank = rank

    @property
    def subtype(self):
        """Gets the subtype of this Multimedia.  # noqa: E501


        :return: The subtype of this Multimedia.  # noqa: E501
        :rtype: str
        """
        return self._subtype

    @subtype.setter
    def subtype(self, subtype):
        """Sets the subtype of this Multimedia.


        :param subtype: The subtype of this Multimedia.  # noqa: E501
        :type: str
        """

        self._subtype = subtype

    @property
    def caption(self):
        """Gets the caption of this Multimedia.  # noqa: E501


        :return: The caption of this Multimedia.  # noqa: E501
        :rtype: str
        """
        return self._caption

    @caption.setter
    def caption(self, caption):
        """Sets the caption of this Multimedia.


        :param caption: The caption of this Multimedia.  # noqa: E501
        :type: str
        """

        self._caption = caption

    @property
    def credit(self):
        """Gets the credit of this Multimedia.  # noqa: E501


        :return: The credit of this Multimedia.  # noqa: E501
        :rtype: str
        """
        return self._credit

    @credit.setter
    def credit(self, credit):
        """Sets the credit of this Multimedia.


        :param credit: The credit of this Multimedia.  # noqa: E501
        :type: str
        """

        self._credit = credit

    @property
    def type(self):
        """Gets the type of this Multimedia.  # noqa: E501


        :return: The type of this Multimedia.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Multimedia.


        :param type: The type of this Multimedia.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def url(self):
        """Gets the url of this Multimedia.  # noqa: E501


        :return: The url of this Multimedia.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Multimedia.


        :param url: The url of this Multimedia.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def height(self):
        """Gets the height of this Multimedia.  # noqa: E501


        :return: The height of this Multimedia.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Multimedia.


        :param height: The height of this Multimedia.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def width(self):
        """Gets the width of this Multimedia.  # noqa: E501


        :return: The width of this Multimedia.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Multimedia.


        :param width: The width of this Multimedia.  # noqa: E501
        :type: int
        """

        self._width = width

    @property
    def legacy(self):
        """Gets the legacy of this Multimedia.  # noqa: E501


        :return: The legacy of this Multimedia.  # noqa: E501
        :rtype: object
        """
        return self._legacy

    @legacy.setter
    def legacy(self, legacy):
        """Sets the legacy of this Multimedia.


        :param legacy: The legacy of this Multimedia.  # noqa: E501
        :type: object
        """

        self._legacy = legacy

    @property
    def crop_name(self):
        """Gets the crop_name of this Multimedia.  # noqa: E501


        :return: The crop_name of this Multimedia.  # noqa: E501
        :rtype: str
        """
        return self._crop_name

    @crop_name.setter
    def crop_name(self, crop_name):
        """Sets the crop_name of this Multimedia.


        :param crop_name: The crop_name of this Multimedia.  # noqa: E501
        :type: str
        """

        self._crop_name = crop_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Multimedia, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Multimedia):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Multimedia):
            return True

        return self.to_dict() != other.to_dict()
