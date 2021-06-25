# swagger_client.SearchApi

All URIs are relative to *https://api.nytimes.com/svc/search/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**articlesearch_json_get**](SearchApi.md#articlesearch_json_get) | **GET** /articlesearch.json | Returns an array of articles.


# **articlesearch_json_get**
> object articlesearch_json_get(begin_date=begin_date, end_date=end_date, facet=facet, facet_fields=facet_fields, facet_filter=facet_filter, fl=fl, fq=fq, page=page, q=q, sort=sort)

Returns an array of articles.

Search for NYT articles by keywords, filters and facets.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
begin_date = 'begin_date_example' # str | Begin date (e.g. 20120101) (optional)
end_date = 'end_date_example' # str | End date (e.g. 20121231) (optional)
facet = 'facet_example' # str | Whether to show facet counts (optional)
facet_fields = 'facet_fields_example' # str | Facets (optional)
facet_filter = 'facet_filter_example' # str | Have facet counts use filters (optional)
fl = 'fl_example' # str | Field list (optional)
fq = 'fq_example' # str | Filter query (optional)
page = 56 # int | Page number (0, 1, ...) (optional)
q = 'q_example' # str | Query (optional)
sort = 'sort_example' # str | Sort order (optional)

try:
    # Returns an array of articles.
    api_response = api_instance.articlesearch_json_get(begin_date=begin_date, end_date=end_date, facet=facet, facet_fields=facet_fields, facet_filter=facet_filter, fl=fl, fq=fq, page=page, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->articlesearch_json_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **begin_date** | **str**| Begin date (e.g. 20120101) | [optional] 
 **end_date** | **str**| End date (e.g. 20121231) | [optional] 
 **facet** | **str**| Whether to show facet counts | [optional] 
 **facet_fields** | **str**| Facets | [optional] 
 **facet_filter** | **str**| Have facet counts use filters | [optional] 
 **fl** | **str**| Field list | [optional] 
 **fq** | **str**| Filter query | [optional] 
 **page** | **int**| Page number (0, 1, ...) | [optional] 
 **q** | **str**| Query | [optional] 
 **sort** | **str**| Sort order | [optional] 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

