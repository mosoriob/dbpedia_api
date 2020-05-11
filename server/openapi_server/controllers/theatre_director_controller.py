import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import THEATREDIRECTOR_TYPE_NAME, THEATREDIRECTOR_TYPE_URI

from openapi_server.models.theatre_director import TheatreDirector  # noqa: E501
from openapi_server import util

def theatredirectors_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of TheatreDirector

    Gets a list of all instances of TheatreDirector (more information in http://dbpedia.org/ontology/TheatreDirector) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[TheatreDirector]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=THEATREDIRECTOR_TYPE_URI,
        rdf_type_name=THEATREDIRECTOR_TYPE_NAME, 
        kls=TheatreDirector)

def theatredirectors_id_get(id):  # noqa: E501
    """Get a single TheatreDirector by its id

    Gets the details of a given TheatreDirector (more information in http://dbpedia.org/ontology/TheatreDirector) # noqa: E501

    :param id: The ID of the TheatreDirector to be retrieved
    :type id: str

    :rtype: TheatreDirector
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=THEATREDIRECTOR_TYPE_URI,
        rdf_type_name=THEATREDIRECTOR_TYPE_NAME, 
        kls=TheatreDirector)
