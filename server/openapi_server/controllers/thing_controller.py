import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import THING_TYPE_NAME, THING_TYPE_URI

from openapi_server.models.thing import Thing  # noqa: E501
from openapi_server import util

def things_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Thing

    Gets a list of all instances of Thing (more information in http://dbpedia.org/ontology/Thing) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Thing]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=THING_TYPE_URI,
        rdf_type_name=THING_TYPE_NAME, 
        kls=Thing)

def things_id_get(id):  # noqa: E501
    """Get a single Thing by its id

    Gets the details of a given Thing (more information in http://dbpedia.org/ontology/Thing) # noqa: E501

    :param id: The ID of the Thing to be retrieved
    :type id: str

    :rtype: Thing
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=THING_TYPE_URI,
        rdf_type_name=THING_TYPE_NAME, 
        kls=Thing)
