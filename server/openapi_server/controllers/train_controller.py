import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import TRAIN_TYPE_NAME, TRAIN_TYPE_URI

from openapi_server.models.train import Train  # noqa: E501
from openapi_server import util

def trains_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Train

    Gets a list of all instances of Train (more information in http://dbpedia.org/ontology/Train) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Train]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=TRAIN_TYPE_URI,
        rdf_type_name=TRAIN_TYPE_NAME, 
        kls=Train)

def trains_id_get(id):  # noqa: E501
    """Get a single Train by its id

    Gets the details of a given Train (more information in http://dbpedia.org/ontology/Train) # noqa: E501

    :param id: The ID of the Train to be retrieved
    :type id: str

    :rtype: Train
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=TRAIN_TYPE_URI,
        rdf_type_name=TRAIN_TYPE_NAME, 
        kls=Train)
