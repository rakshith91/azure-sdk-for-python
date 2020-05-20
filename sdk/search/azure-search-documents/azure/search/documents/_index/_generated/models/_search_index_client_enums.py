# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6257, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class IndexActionType(str, Enum):
    """The operation to perform on a document in an indexing batch.
    """

    upload = "upload"  #: Inserts the document into the index if it is new and updates it if it exists. All fields are replaced in the update case.
    merge = "merge"  #: Merges the specified field values with an existing document. If the document does not exist, the merge will fail. Any field you specify in a merge will replace the existing field in the document. This also applies to collections of primitive and complex types.
    merge_or_upload = "mergeOrUpload"  #: Behaves like merge if a document with the given key already exists in the index. If the document does not exist, it behaves like upload with a new document.
    delete = "delete"  #: Removes the specified document from the index. Any field you specify in a delete operation other than the key field will be ignored. If you want to remove an individual field from a document, use merge instead and set the field explicitly to null.

class QueryType(str, Enum):

    simple = "simple"  #: Uses the simple query syntax for searches. Search text is interpreted using a simple query language that allows for symbols such as +, * and "". Queries are evaluated across all searchable fields by default, unless the searchFields parameter is specified.
    full = "full"  #: Uses the full Lucene query syntax for searches. Search text is interpreted using the Lucene query language which allows field-specific and weighted searches, as well as other advanced features.

class SearchMode(str, Enum):

    any = "any"  #: Any of the search terms must be matched in order to count the document as a match.
    all = "all"  #: All of the search terms must be matched in order to count the document as a match.

class AutocompleteMode(str, Enum):

    one_term = "oneTerm"  #: Only one term is suggested. If the query has two terms, only the last term is completed. For example, if the input is 'washington medic', the suggested terms could include 'medicaid', 'medicare', and 'medicine'.
    two_terms = "twoTerms"  #: Matching two-term phrases in the index will be suggested. For example, if the input is 'medic', the suggested terms could include 'medicare coverage' and 'medical assistant'.
    one_term_with_context = "oneTermWithContext"  #: Completes the last term in a query with two or more terms, where the last two terms are a phrase that exists in the index. For example, if the input is 'washington medic', the suggested terms could include 'washington medicaid' and 'washington medical'.
