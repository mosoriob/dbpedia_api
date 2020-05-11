import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BODYBUILDER_TYPE_NAME, BODYBUILDER_TYPE_URI

from openapi_server.models.bodybuilder import Bodybuilder  # noqa: E501
from openapi_server import util

def bodybuilders_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Bodybuilder

    Gets a list of all instances of Bodybuilder (more information in http://dbpedia.org/ontology/Bodybuilder) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Bodybuilder]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BODYBUILDER_TYPE_URI,
        rdf_type_name=BODYBUILDER_TYPE_NAME, 
        kls=Bodybuilder)

def bodybuilders_id_get(id):  # noqa: E501
    """Get a single Bodybuilder by its id

    Gets the details of a given Bodybuilder (more information in http://dbpedia.org/ontology/Bodybuilder) # noqa: E501

    :param id: The ID of the Bodybuilder to be retrieved
    :type id: str

    :rtype: Bodybuilder
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BODYBUILDER_TYPE_URI,
        rdf_type_name=BODYBUILDER_TYPE_NAME, 
        kls=Bodybuilder)
