import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MUSEUM_TYPE_NAME, MUSEUM_TYPE_URI

from openapi_server.models.museum import Museum  # noqa: E501
from openapi_server import util

def museums_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Museum

    Gets a list of all instances of Museum (more information in http://dbpedia.org/ontology/Museum) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Museum]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MUSEUM_TYPE_URI,
        rdf_type_name=MUSEUM_TYPE_NAME, 
        kls=Museum)

def museums_id_get(id):  # noqa: E501
    """Get a single Museum by its id

    Gets the details of a given Museum (more information in http://dbpedia.org/ontology/Museum) # noqa: E501

    :param id: The ID of the Museum to be retrieved
    :type id: str

    :rtype: Museum
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MUSEUM_TYPE_URI,
        rdf_type_name=MUSEUM_TYPE_NAME, 
        kls=Museum)
