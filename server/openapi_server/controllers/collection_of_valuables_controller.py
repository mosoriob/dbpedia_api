import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import COLLECTIONOFVALUABLES_TYPE_NAME, COLLECTIONOFVALUABLES_TYPE_URI

from openapi_server.models.collection_of_valuables import CollectionOfValuables  # noqa: E501
from openapi_server import util

def collectionofvaluabless_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of CollectionOfValuables

    Gets a list of all instances of CollectionOfValuables (more information in http://dbpedia.org/ontology/CollectionOfValuables) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[CollectionOfValuables]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=COLLECTIONOFVALUABLES_TYPE_URI,
        rdf_type_name=COLLECTIONOFVALUABLES_TYPE_NAME, 
        kls=CollectionOfValuables)

def collectionofvaluabless_id_get(id):  # noqa: E501
    """Get a single CollectionOfValuables by its id

    Gets the details of a given CollectionOfValuables (more information in http://dbpedia.org/ontology/CollectionOfValuables) # noqa: E501

    :param id: The ID of the CollectionOfValuables to be retrieved
    :type id: str

    :rtype: CollectionOfValuables
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=COLLECTIONOFVALUABLES_TYPE_URI,
        rdf_type_name=COLLECTIONOFVALUABLES_TYPE_NAME, 
        kls=CollectionOfValuables)
