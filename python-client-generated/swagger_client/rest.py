# coding: utf-8

"""
    Article Search

    Use the Article Search API to look up articles by keyword.  You can refine your search using filters and facets.  ``` /articlesearch.json?q={query}&fq={filter} ```  ## Example Call ``` https://api.nytimes.com/svc/search/v2/articlesearch.json?q=election&api-key=yourkey ```  ## FILTERING YOUR SEARCH Use filters to narrow the scope of your search. You can specify the fields and the values that your query will be filtered on. The Article Search API uses [Elasticsearch](https://www.elastic.co/), so the filter query uses standard [Lucene syntax](http://www.lucenetutorial.com/lucene-query-syntax.html). Separate the filter field name and value with a colon, and surround multiple values with parentheses.  ``` field-name:(\"value1\" \"value2\" ... \"value n\") ```  The default connector for values in parentheses is OR. If you declare an explicit boolean value, it must be capitalized.  You can filter on multiple values and fields.  ``` field-name-1:(\"value1\") AND field-name-2:(\"value2\" \"value3\") ```  For a list of all fields you can filter on, see the Filter Query Fields table below.  ### Pagination The Article Search API returns a max of 10 results at a time. The meta node in the response contains the total number of matches (\"hits\") and the current offset. Use the page query parameter to paginate thru results (page=0 for results 1-10, page=1 for 11-20, ...). You can paginate thru up to 100 pages (1,000 results). If you get too many results try filtering by date range.  ### Filter Query Examples Restrict your search to articles with The New York Times as the source:  ``` fq=source:(\"The New York Times\") ```  Restrict your search to articles from either the Sports or Foreign desk:  ``` fq=news_desk:(\"Sports\" \"Foreign\") ```  Restrict your search to articles that are about New York City and from the Sports desk:  ``` fq=news_desk:(\"Sports\") AND glocations:(\"NEW YORK CITY\") ```  If you do not specify a field, the scope of the filter query will look for matches in the body, headline and byline. The example below will restrict your search to articles with The New York Times in the body, headline or byline:  ``` fq=The New York Times ```  ### Filter Query Fields Field                     | Behavior ------------------------- | --------------- body                      | Multiple tokens body.search               | Left-edge n-grams creative_works            | Single token creative_works.contains   | Multiple tokens day_of_week               | Single token document_type             | Case-sensitive exact match glocations                | Single token glocations.contains       | Multiple tokens headline                  | Multiple tokens headline.search           | Left-edge n-grams kicker                    | Single token kicker.contains           | Multiple tokens news_desk                 | Single token news_desk.contains        | Multiple tokens organizations             | Single token organizations.contains    | Multiple tokens persons                   | Single token persons.contains          | Multiple tokens pub_date                  | Timestamp (YYYY-MM-DD) pub_year                  | Integer secpg                     | Multiple tokens source                    | Single token source.contains           | Multiple tokens subject                   | Single token subject.contains          | Multiple tokens section_name              | Single token section_name.contains     | Multiple tokens type_of_material          | Single token type_of_material.contains | Multiple tokens web_url                   | Single token (case-sensitive) word_count                | Integer  #### News Desk Values * Adventure Sports * Arts & Leisure * Arts * Automobiles * Blogs * Books * Booming * Business Day * Business * Cars * Circuits * Classifieds * Connecticut * Crosswords & Games * Culture * DealBook * Dining * Editorial * Education * Energy * Entrepreneurs * Environment * Escapes * Fashion & Style * Fashion * Favorites * Financial * Flight * Food * Foreign * Generations * Giving * Global Home * Health & Fitness * Health * Home & Garden * Home * Jobs * Key * Letters * Long Island * Magazine * Market Place * Media * Men's Health * Metro * Metropolitan * Movies * Museums * National * Nesting * Obits * Obituaries * Obituary * OpEd * Opinion * Outlook * Personal Investing * Personal Tech * Play * Politics * Regionals * Retail * Retirement * Science * Small Business * Society * Sports * Style * Sunday Business * Sunday Review * Sunday Styles * T Magazine * T Style * Technology * Teens * Television * The Arts * The Business of Green * The City Desk * The City * The Marathon * The Millennium * The Natural World * The Upshot * The Weekend * The Year in Pictures * Theater * Then & Now * Thursday Styles * Times Topics * Travel * U.S. * Universal * Upshot * UrbanEye * Vacation * Washington * Wealth * Weather * Week in Review * Week * Weekend * Westchester * Wireless Living * Women's Health * Working * Workplace * World * Your Money  #### Section Name Values * Arts * Automobiles * Autos * Blogs * Books * Booming * Business * Business Day * Corrections * Crosswords & Games * Crosswords/Games * Dining & Wine * Dining and Wine * Editors' Notes * Education * Fashion & Style * Food * Front Page * Giving * Global Home * Great Homes & Destinations * Great Homes and Destinations * Health * Home & Garden * Home and Garden * International Home * Job Market * Learning * Magazine * Movies * Multimedia * Multimedia/Photos * N.Y. / Region * N.Y./Region * NYRegion * NYT Now * National * New York * New York and Region * Obituaries * Olympics * Open * Opinion * Paid Death Notices * Public Editor * Real Estate * Science * Sports * Style * Sunday Magazine * Sunday Review * T Magazine * T:Style * Technology * The Public Editor * The Upshot * Theater * Times Topics * TimesMachine * Today's Headlines * Topics * Travel * U.S. * Universal * UrbanEye * Washington * Week in Review * World * Your Money  #### Type of Material Values * Addendum * An Analysis * An Appraisal * Archives * Article * Banner * Biography * Birth Notice * Blog * Brief * Caption * Chronology * Column * Correction * Economic Analysis * Editorial * Editorial Cartoon * Editors' Note * First Chapter * Front Page * Glossary * Interactive Feature * Interactive Graphic * Interview * Letter * List * Marriage Announcement * Military Analysis * News * News Analysis * Newsletter * Obituary * Obituary (Obit) * Op-Ed * Paid Death Notice * Postscript * Premium * Question * Quote * Recipe * Review * Schedule * SectionFront * Series * Slideshow * Special Report * Statistics * Summary * Text * Video * Web Log  ## USING FACETS Use facets to view the relative importance of certain fields to a search term, and gain insight about how to best refine your queries and filter your search results.  The following fields can be used as facet fields: day_of_week, document_type, ingredients, news_desk, pub_month, pub_year, section_name, source, subsection_name, and type_of_material.  Specify facets using the facet_fields parameter. Set facet=true and the response will contain an array with a count for the five terms that have the highest count for each facet. For example, including the following in your request will add a facet array with a count for the top five days of the week to the response.  ``` facet_fields=day_of_week&facet=true ```  By default, facet counts ignore all filters and return the count for all results of a query. For the following queries, the facet count in each response will be identical, even though the results returned in one set is restricted to articles published in 2012.  ``` q=obama&facet_fields=source&facet=true&begin_date=20120101&end_date=20121231 ```  You can force facet counts to respect filters by setting facet_filter=true. Facet counts will be restricted based on any filters you have specified (this includes both explicit filter queries set using the fq parameter and implicit filters like begin_date).  Here is the facet array response to the query. ```javascript \"facets\": {   \"source\": {     \"_type\": \"terms\",     \"missing\": 524,     \"total\": 83121,     \"other\": 317,     \"terms\": [       {         \"term\": \"The New York Times\",         \"count\": 68530       },       {         \"term\": \"AP\",         \"count\": 7705       },       {         \"term\": \"Reuters\",         \"count\": 4969       },       {         \"term\": \"International Herald Tribune\",         \"count\": 1464       },       {         \"term\": \"\",         \"count\": 136       }     ]   } } ``` If you set facet_filter to true the facet array will only count facet occurences in 2012. ```javascript facets\": {   \"source\": {     \"_type\": \"terms\",     \"missing\": 192,     \"total\": 22596,     \"other\": 139,     \"terms\": [       {         \"term\": \"The New York Times\",         \"count\": 14812       },       ... ``` ### Examples Requests Search for documents containing 'new york times' and return results 20-29 with results sorted oldest first.  ``` https://api.nytimes.com/svc/search/v2/articlesearch.json?q=new+york+times&page=2&sort=oldest&api-key=your-api-key ``` Search for all documents published on January 1, 2012 containing 'romney'.  Facet count will be returned for 'day_of_week' and will be reflective of all documents (i.e., the date range filter and filter query do not affect facet counts).  ``` https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=romney&facet_field=day_of_week&facet=true&begin_date=20120101&end_date=20120101&api-key=your-api-key ```  ### Example Response Here is an partial example response.  ```javascript {   \"response\": {     \"meta\": {       \"hits\": 25,       \"time\": 332,       \"offset\": 0     },     \"docs\": [       {         \"web_url\": \"http://thecaucus.blogs.nytimes.com/2012/01/01/virginia-attorney-general-backs-off-ballot-proposal/\",         \"snippet\": \"Virginia's attorney general on Sunday backed off of a proposal to loosen the state's ballot access rules to allow more Republican presidential candidates to qualify.\",         \"lead_paragraph\": \"DES MOINES -- Virginia's attorney general on Sunday backed off of a proposal to loosen the state's ballot access rules to allow more Republican presidential candidates to qualify.\",         ...       }     ],     \"facets\": {         \"day_of_week\": {             \"_type\": \"terms\",             \"missing\": 1871790,             \"total\": 13098462,             \"other\": 3005891,             \"terms\": [               {                 \"term\": \"Sunday\",                 \"count\": 3122347               },               ... ```  ### Limit Fields in Response You can limit the number fields returned in the response with the fl parameter. ``` fl=web_url ```   # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import io
import json
import logging
import re
import ssl

import certifi
# python 2 and python 3 compatibility library
import six
from six.moves.urllib.parse import urlencode

try:
    import urllib3
except ImportError:
    raise ImportError('Swagger python client requires urllib3.')


logger = logging.getLogger(__name__)


class RESTResponse(io.IOBase):

    def __init__(self, resp):
        self.urllib3_response = resp
        self.status = resp.status
        self.reason = resp.reason
        self.data = resp.data

    def getheaders(self):
        """Returns a dictionary of the response headers."""
        return self.urllib3_response.getheaders()

    def getheader(self, name, default=None):
        """Returns a given response header."""
        return self.urllib3_response.getheader(name, default)


class RESTClientObject(object):

    def __init__(self, configuration, pools_size=4, maxsize=None):
        # urllib3.PoolManager will pass all kw parameters to connectionpool
        # https://github.com/shazow/urllib3/blob/f9409436f83aeb79fbaf090181cd81b784f1b8ce/urllib3/poolmanager.py#L75  # noqa: E501
        # https://github.com/shazow/urllib3/blob/f9409436f83aeb79fbaf090181cd81b784f1b8ce/urllib3/connectionpool.py#L680  # noqa: E501
        # maxsize is the number of requests to host that are allowed in parallel  # noqa: E501
        # Custom SSL certificates and client certificates: http://urllib3.readthedocs.io/en/latest/advanced-usage.html  # noqa: E501

        # cert_reqs
        if configuration.verify_ssl:
            cert_reqs = ssl.CERT_REQUIRED
        else:
            cert_reqs = ssl.CERT_NONE

        # ca_certs
        if configuration.ssl_ca_cert:
            ca_certs = configuration.ssl_ca_cert
        else:
            # if not set certificate file, use Mozilla's root certificates.
            ca_certs = certifi.where()

        addition_pool_args = {}
        if configuration.assert_hostname is not None:
            addition_pool_args['assert_hostname'] = configuration.assert_hostname  # noqa: E501

        if maxsize is None:
            if configuration.connection_pool_maxsize is not None:
                maxsize = configuration.connection_pool_maxsize
            else:
                maxsize = 4

        # https pool manager
        if configuration.proxy:
            self.pool_manager = urllib3.ProxyManager(
                num_pools=pools_size,
                maxsize=maxsize,
                cert_reqs=cert_reqs,
                ca_certs=ca_certs,
                cert_file=configuration.cert_file,
                key_file=configuration.key_file,
                proxy_url=configuration.proxy,
                **addition_pool_args
            )
        else:
            self.pool_manager = urllib3.PoolManager(
                num_pools=pools_size,
                maxsize=maxsize,
                cert_reqs=cert_reqs,
                ca_certs=ca_certs,
                cert_file=configuration.cert_file,
                key_file=configuration.key_file,
                **addition_pool_args
            )

    def request(self, method, url, query_params=None, headers=None,
                body=None, post_params=None, _preload_content=True,
                _request_timeout=None):
        """Perform requests.

        :param method: http request method
        :param url: http request url
        :param query_params: query parameters in the url
        :param headers: http request headers
        :param body: request json body, for `application/json`
        :param post_params: request post parameters,
                            `application/x-www-form-urlencoded`
                            and `multipart/form-data`
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        """
        method = method.upper()
        assert method in ['GET', 'HEAD', 'DELETE', 'POST', 'PUT',
                          'PATCH', 'OPTIONS']

        if post_params and body:
            raise ValueError(
                "body parameter cannot be used with post_params parameter."
            )

        post_params = post_params or {}
        headers = headers or {}

        timeout = None
        if _request_timeout:
            if isinstance(_request_timeout, (int, ) if six.PY3 else (int, long)):  # noqa: E501,F821
                timeout = urllib3.Timeout(total=_request_timeout)
            elif (isinstance(_request_timeout, tuple) and
                  len(_request_timeout) == 2):
                timeout = urllib3.Timeout(
                    connect=_request_timeout[0], read=_request_timeout[1])

        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'

        try:
            # For `POST`, `PUT`, `PATCH`, `OPTIONS`, `DELETE`
            if method in ['POST', 'PUT', 'PATCH', 'OPTIONS', 'DELETE']:
                if query_params:
                    url += '?' + urlencode(query_params)
                if re.search('json', headers['Content-Type'], re.IGNORECASE):
                    request_body = '{}'
                    if body is not None:
                        request_body = json.dumps(body)
                    r = self.pool_manager.request(
                        method, url,
                        body=request_body,
                        preload_content=_preload_content,
                        timeout=timeout,
                        headers=headers)
                elif headers['Content-Type'] == 'application/x-www-form-urlencoded':  # noqa: E501
                    r = self.pool_manager.request(
                        method, url,
                        fields=post_params,
                        encode_multipart=False,
                        preload_content=_preload_content,
                        timeout=timeout,
                        headers=headers)
                elif headers['Content-Type'] == 'multipart/form-data':
                    # must del headers['Content-Type'], or the correct
                    # Content-Type which generated by urllib3 will be
                    # overwritten.
                    del headers['Content-Type']
                    r = self.pool_manager.request(
                        method, url,
                        fields=post_params,
                        encode_multipart=True,
                        preload_content=_preload_content,
                        timeout=timeout,
                        headers=headers)
                # Pass a `string` parameter directly in the body to support
                # other content types than Json when `body` argument is
                # provided in serialized form
                elif isinstance(body, str):
                    request_body = body
                    r = self.pool_manager.request(
                        method, url,
                        body=request_body,
                        preload_content=_preload_content,
                        timeout=timeout,
                        headers=headers)
                else:
                    # Cannot generate the request from given parameters
                    msg = """Cannot prepare a request message for provided
                             arguments. Please check that your arguments match
                             declared content type."""
                    raise ApiException(status=0, reason=msg)
            # For `GET`, `HEAD`
            else:
                r = self.pool_manager.request(method, url,
                                              fields=query_params,
                                              preload_content=_preload_content,
                                              timeout=timeout,
                                              headers=headers)
        except urllib3.exceptions.SSLError as e:
            msg = "{0}\n{1}".format(type(e).__name__, str(e))
            raise ApiException(status=0, reason=msg)

        if _preload_content:
            r = RESTResponse(r)

            # In the python 3, the response.data is bytes.
            # we need to decode it to string.
            if six.PY3:
                r.data = r.data.decode('utf8')

            # log response body
            logger.debug("response body: %s", r.data)

        if not 200 <= r.status <= 299:
            raise ApiException(http_resp=r)

        return r

    def GET(self, url, headers=None, query_params=None, _preload_content=True,
            _request_timeout=None):
        return self.request("GET", url,
                            headers=headers,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            query_params=query_params)

    def HEAD(self, url, headers=None, query_params=None, _preload_content=True,
             _request_timeout=None):
        return self.request("HEAD", url,
                            headers=headers,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            query_params=query_params)

    def OPTIONS(self, url, headers=None, query_params=None, post_params=None,
                body=None, _preload_content=True, _request_timeout=None):
        return self.request("OPTIONS", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def DELETE(self, url, headers=None, query_params=None, body=None,
               _preload_content=True, _request_timeout=None):
        return self.request("DELETE", url,
                            headers=headers,
                            query_params=query_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def POST(self, url, headers=None, query_params=None, post_params=None,
             body=None, _preload_content=True, _request_timeout=None):
        return self.request("POST", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def PUT(self, url, headers=None, query_params=None, post_params=None,
            body=None, _preload_content=True, _request_timeout=None):
        return self.request("PUT", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def PATCH(self, url, headers=None, query_params=None, post_params=None,
              body=None, _preload_content=True, _request_timeout=None):
        return self.request("PATCH", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)


class ApiException(Exception):

    def __init__(self, status=None, reason=None, http_resp=None):
        if http_resp:
            self.status = http_resp.status
            self.reason = http_resp.reason
            self.body = http_resp.data
            self.headers = http_resp.getheaders()
        else:
            self.status = status
            self.reason = reason
            self.body = None
            self.headers = None

    def __str__(self):
        """Custom error messages for exception"""
        error_message = "({0})\n"\
                        "Reason: {1}\n".format(self.status, self.reason)
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(
                self.headers)

        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)

        return error_message
