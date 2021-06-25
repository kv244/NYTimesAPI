# coding: utf-8

"""
    Article Search

    Use the Article Search API to look up articles by keyword.  You can refine your search using filters and facets.  ``` /articlesearch.json?q={query}&fq={filter} ```  ## Example Call ``` https://api.nytimes.com/svc/search/v2/articlesearch.json?q=election&api-key=yourkey ```  ## FILTERING YOUR SEARCH Use filters to narrow the scope of your search. You can specify the fields and the values that your query will be filtered on. The Article Search API uses [Elasticsearch](https://www.elastic.co/), so the filter query uses standard [Lucene syntax](http://www.lucenetutorial.com/lucene-query-syntax.html). Separate the filter field name and value with a colon, and surround multiple values with parentheses.  ``` field-name:(\"value1\" \"value2\" ... \"value n\") ```  The default connector for values in parentheses is OR. If you declare an explicit boolean value, it must be capitalized.  You can filter on multiple values and fields.  ``` field-name-1:(\"value1\") AND field-name-2:(\"value2\" \"value3\") ```  For a list of all fields you can filter on, see the Filter Query Fields table below.  ### Pagination The Article Search API returns a max of 10 results at a time. The meta node in the response contains the total number of matches (\"hits\") and the current offset. Use the page query parameter to paginate thru results (page=0 for results 1-10, page=1 for 11-20, ...). You can paginate thru up to 100 pages (1,000 results). If you get too many results try filtering by date range.  ### Filter Query Examples Restrict your search to articles with The New York Times as the source:  ``` fq=source:(\"The New York Times\") ```  Restrict your search to articles from either the Sports or Foreign desk:  ``` fq=news_desk:(\"Sports\" \"Foreign\") ```  Restrict your search to articles that are about New York City and from the Sports desk:  ``` fq=news_desk:(\"Sports\") AND glocations:(\"NEW YORK CITY\") ```  If you do not specify a field, the scope of the filter query will look for matches in the body, headline and byline. The example below will restrict your search to articles with The New York Times in the body, headline or byline:  ``` fq=The New York Times ```  ### Filter Query Fields Field                     | Behavior ------------------------- | --------------- body                      | Multiple tokens body.search               | Left-edge n-grams creative_works            | Single token creative_works.contains   | Multiple tokens day_of_week               | Single token document_type             | Case-sensitive exact match glocations                | Single token glocations.contains       | Multiple tokens headline                  | Multiple tokens headline.search           | Left-edge n-grams kicker                    | Single token kicker.contains           | Multiple tokens news_desk                 | Single token news_desk.contains        | Multiple tokens organizations             | Single token organizations.contains    | Multiple tokens persons                   | Single token persons.contains          | Multiple tokens pub_date                  | Timestamp (YYYY-MM-DD) pub_year                  | Integer secpg                     | Multiple tokens source                    | Single token source.contains           | Multiple tokens subject                   | Single token subject.contains          | Multiple tokens section_name              | Single token section_name.contains     | Multiple tokens type_of_material          | Single token type_of_material.contains | Multiple tokens web_url                   | Single token (case-sensitive) word_count                | Integer  #### News Desk Values * Adventure Sports * Arts & Leisure * Arts * Automobiles * Blogs * Books * Booming * Business Day * Business * Cars * Circuits * Classifieds * Connecticut * Crosswords & Games * Culture * DealBook * Dining * Editorial * Education * Energy * Entrepreneurs * Environment * Escapes * Fashion & Style * Fashion * Favorites * Financial * Flight * Food * Foreign * Generations * Giving * Global Home * Health & Fitness * Health * Home & Garden * Home * Jobs * Key * Letters * Long Island * Magazine * Market Place * Media * Men's Health * Metro * Metropolitan * Movies * Museums * National * Nesting * Obits * Obituaries * Obituary * OpEd * Opinion * Outlook * Personal Investing * Personal Tech * Play * Politics * Regionals * Retail * Retirement * Science * Small Business * Society * Sports * Style * Sunday Business * Sunday Review * Sunday Styles * T Magazine * T Style * Technology * Teens * Television * The Arts * The Business of Green * The City Desk * The City * The Marathon * The Millennium * The Natural World * The Upshot * The Weekend * The Year in Pictures * Theater * Then & Now * Thursday Styles * Times Topics * Travel * U.S. * Universal * Upshot * UrbanEye * Vacation * Washington * Wealth * Weather * Week in Review * Week * Weekend * Westchester * Wireless Living * Women's Health * Working * Workplace * World * Your Money  #### Section Name Values * Arts * Automobiles * Autos * Blogs * Books * Booming * Business * Business Day * Corrections * Crosswords & Games * Crosswords/Games * Dining & Wine * Dining and Wine * Editors' Notes * Education * Fashion & Style * Food * Front Page * Giving * Global Home * Great Homes & Destinations * Great Homes and Destinations * Health * Home & Garden * Home and Garden * International Home * Job Market * Learning * Magazine * Movies * Multimedia * Multimedia/Photos * N.Y. / Region * N.Y./Region * NYRegion * NYT Now * National * New York * New York and Region * Obituaries * Olympics * Open * Opinion * Paid Death Notices * Public Editor * Real Estate * Science * Sports * Style * Sunday Magazine * Sunday Review * T Magazine * T:Style * Technology * The Public Editor * The Upshot * Theater * Times Topics * TimesMachine * Today's Headlines * Topics * Travel * U.S. * Universal * UrbanEye * Washington * Week in Review * World * Your Money  #### Type of Material Values * Addendum * An Analysis * An Appraisal * Archives * Article * Banner * Biography * Birth Notice * Blog * Brief * Caption * Chronology * Column * Correction * Economic Analysis * Editorial * Editorial Cartoon * Editors' Note * First Chapter * Front Page * Glossary * Interactive Feature * Interactive Graphic * Interview * Letter * List * Marriage Announcement * Military Analysis * News * News Analysis * Newsletter * Obituary * Obituary (Obit) * Op-Ed * Paid Death Notice * Postscript * Premium * Question * Quote * Recipe * Review * Schedule * SectionFront * Series * Slideshow * Special Report * Statistics * Summary * Text * Video * Web Log  ## USING FACETS Use facets to view the relative importance of certain fields to a search term, and gain insight about how to best refine your queries and filter your search results.  The following fields can be used as facet fields: day_of_week, document_type, ingredients, news_desk, pub_month, pub_year, section_name, source, subsection_name, and type_of_material.  Specify facets using the facet_fields parameter. Set facet=true and the response will contain an array with a count for the five terms that have the highest count for each facet. For example, including the following in your request will add a facet array with a count for the top five days of the week to the response.  ``` facet_fields=day_of_week&facet=true ```  By default, facet counts ignore all filters and return the count for all results of a query. For the following queries, the facet count in each response will be identical, even though the results returned in one set is restricted to articles published in 2012.  ``` q=obama&facet_fields=source&facet=true&begin_date=20120101&end_date=20121231 ```  You can force facet counts to respect filters by setting facet_filter=true. Facet counts will be restricted based on any filters you have specified (this includes both explicit filter queries set using the fq parameter and implicit filters like begin_date).  Here is the facet array response to the query. ```javascript \"facets\": {   \"source\": {     \"_type\": \"terms\",     \"missing\": 524,     \"total\": 83121,     \"other\": 317,     \"terms\": [       {         \"term\": \"The New York Times\",         \"count\": 68530       },       {         \"term\": \"AP\",         \"count\": 7705       },       {         \"term\": \"Reuters\",         \"count\": 4969       },       {         \"term\": \"International Herald Tribune\",         \"count\": 1464       },       {         \"term\": \"\",         \"count\": 136       }     ]   } } ``` If you set facet_filter to true the facet array will only count facet occurences in 2012. ```javascript facets\": {   \"source\": {     \"_type\": \"terms\",     \"missing\": 192,     \"total\": 22596,     \"other\": 139,     \"terms\": [       {         \"term\": \"The New York Times\",         \"count\": 14812       },       ... ``` ### Examples Requests Search for documents containing 'new york times' and return results 20-29 with results sorted oldest first.  ``` https://api.nytimes.com/svc/search/v2/articlesearch.json?q=new+york+times&page=2&sort=oldest&api-key=your-api-key ``` Search for all documents published on January 1, 2012 containing 'romney'.  Facet count will be returned for 'day_of_week' and will be reflective of all documents (i.e., the date range filter and filter query do not affect facet counts).  ``` https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=romney&facet_field=day_of_week&facet=true&begin_date=20120101&end_date=20120101&api-key=your-api-key ```  ### Example Response Here is an partial example response.  ```javascript {   \"response\": {     \"meta\": {       \"hits\": 25,       \"time\": 332,       \"offset\": 0     },     \"docs\": [       {         \"web_url\": \"http://thecaucus.blogs.nytimes.com/2012/01/01/virginia-attorney-general-backs-off-ballot-proposal/\",         \"snippet\": \"Virginia's attorney general on Sunday backed off of a proposal to loosen the state's ballot access rules to allow more Republican presidential candidates to qualify.\",         \"lead_paragraph\": \"DES MOINES -- Virginia's attorney general on Sunday backed off of a proposal to loosen the state's ballot access rules to allow more Republican presidential candidates to qualify.\",         ...       }     ],     \"facets\": {         \"day_of_week\": {             \"_type\": \"terms\",             \"missing\": 1871790,             \"total\": 13098462,             \"other\": 3005891,             \"terms\": [               {                 \"term\": \"Sunday\",                 \"count\": 3122347               },               ... ```  ### Limit Fields in Response You can limit the number fields returned in the response with the fl parameter. ``` fl=web_url ```   # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class SearchApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def articlesearch_json_get(self, **kwargs):  # noqa: E501
        """Returns an array of articles.  # noqa: E501

        Search for NYT articles by keywords, filters and facets.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.articlesearch_json_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str begin_date: Begin date (e.g. 20120101)
        :param str end_date: End date (e.g. 20121231)
        :param str facet: Whether to show facet counts
        :param str facet_fields: Facets
        :param str facet_filter: Have facet counts use filters
        :param str fl: Field list
        :param str fq: Filter query
        :param int page: Page number (0, 1, ...)
        :param str q: Query
        :param str sort: Sort order
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.articlesearch_json_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.articlesearch_json_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def articlesearch_json_get_with_http_info(self, **kwargs):  # noqa: E501
        """Returns an array of articles.  # noqa: E501

        Search for NYT articles by keywords, filters and facets.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.articlesearch_json_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str begin_date: Begin date (e.g. 20120101)
        :param str end_date: End date (e.g. 20121231)
        :param str facet: Whether to show facet counts
        :param str facet_fields: Facets
        :param str facet_filter: Have facet counts use filters
        :param str fl: Field list
        :param str fq: Filter query
        :param int page: Page number (0, 1, ...)
        :param str q: Query
        :param str sort: Sort order
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['begin_date', 'end_date', 'facet', 'facet_fields', 'facet_filter', 'fl', 'fq', 'page', 'q', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method articlesearch_json_get" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('begin_date' in params and not re.search(r'^\\d{8}$', params['begin_date'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `begin_date` when calling `articlesearch_json_get`, must conform to the pattern `/^\\d{8}$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('end_date' in params and not re.search(r'^\\d{8}$', params['end_date'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `end_date` when calling `articlesearch_json_get`, must conform to the pattern `/^\\d{8}$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('page' in params and params['page'] > 100):  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `articlesearch_json_get`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and ('page' in params and params['page'] < 0):  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `articlesearch_json_get`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'begin_date' in params:
            query_params.append(('begin_date', params['begin_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('end_date', params['end_date']))  # noqa: E501
        if 'facet' in params:
            query_params.append(('facet', params['facet']))  # noqa: E501
        if 'facet_fields' in params:
            query_params.append(('facet_fields', params['facet_fields']))  # noqa: E501
        if 'facet_filter' in params:
            query_params.append(('facet_filter', params['facet_filter']))  # noqa: E501
        if 'fl' in params:
            query_params.append(('fl', params['fl']))  # noqa: E501
        if 'fq' in params:
            query_params.append(('fq', params['fq']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikey']  # noqa: E501

        return self.api_client.call_api(
            '/articlesearch.json', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
