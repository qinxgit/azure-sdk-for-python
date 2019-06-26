# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .search_results_answer import SearchResultsAnswer


class Images(SearchResultsAnswer):
    """Defines an image answer.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param _type: Required. Constant filled by server.
    :type _type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar read_link: The URL that returns this resource.
    :vartype read_link: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    :ivar total_estimated_matches: The estimated number of webpages that are
     relevant to the query. Use this number along with the count and offset
     query parameters to page the results.
    :vartype total_estimated_matches: long
    :ivar next_offset: Used as part of deduping. Tells client the next offset
     that client should use in the next pagination request
    :vartype next_offset: int
    :param value: Required. A list of image objects that are relevant to the
     query. If there are no results, the List is empty.
    :type value:
     list[~azure.cognitiveservices.search.imagesearch.models.ImageObject]
    :ivar query_expansions: A list of expanded queries that narrows the
     original query. For example, if the query was Microsoft Surface, the
     expanded queries might be: Microsoft Surface Pro 3, Microsoft Surface RT,
     Microsoft Surface Phone, and Microsoft Surface Hub.
    :vartype query_expansions:
     list[~azure.cognitiveservices.search.imagesearch.models.Query]
    :ivar pivot_suggestions: A list of segments in the original query. For
     example, if the query was Red Flowers, Bing might segment the query into
     Red and Flowers. The Flowers pivot may contain query suggestions such as
     Red Peonies and Red Daisies, and the Red pivot may contain query
     suggestions such as Green Flowers and Yellow Flowers.
    :vartype pivot_suggestions:
     list[~azure.cognitiveservices.search.imagesearch.models.PivotSuggestions]
    :ivar similar_terms: A list of terms that are similar in meaning to the
     user's query term.
    :vartype similar_terms:
     list[~azure.cognitiveservices.search.imagesearch.models.Query]
    """

    _validation = {
        '_type': {'required': True},
        'id': {'readonly': True},
        'read_link': {'readonly': True},
        'web_search_url': {'readonly': True},
        'total_estimated_matches': {'readonly': True},
        'next_offset': {'readonly': True},
        'value': {'required': True},
        'query_expansions': {'readonly': True},
        'pivot_suggestions': {'readonly': True},
        'similar_terms': {'readonly': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'read_link': {'key': 'readLink', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'total_estimated_matches': {'key': 'totalEstimatedMatches', 'type': 'long'},
        'next_offset': {'key': 'nextOffset', 'type': 'int'},
        'value': {'key': 'value', 'type': '[ImageObject]'},
        'query_expansions': {'key': 'queryExpansions', 'type': '[Query]'},
        'pivot_suggestions': {'key': 'pivotSuggestions', 'type': '[PivotSuggestions]'},
        'similar_terms': {'key': 'similarTerms', 'type': '[Query]'},
    }

    def __init__(self, *, value, **kwargs) -> None:
        super(Images, self).__init__(**kwargs)
        self.next_offset = None
        self.value = value
        self.query_expansions = None
        self.pivot_suggestions = None
        self.similar_terms = None
        self._type = 'Images'