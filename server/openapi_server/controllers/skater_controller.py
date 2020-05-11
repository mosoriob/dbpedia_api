import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SKATER_TYPE_NAME, SKATER_TYPE_URI

from openapi_server.models.skater import Skater  # noqa: E501
from openapi_server import util

def skaters_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Skater

    Gets a list of all instances of Skater (more information in http://dbpedia.org/ontology/Skater) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Skater]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SKATER_TYPE_URI,
        rdf_type_name=SKATER_TYPE_NAME, 
        kls=Skater)

def skaters_id_get(id):  # noqa: E501
    """Get a single Skater by its id

    Gets the details of a given Skater (more information in http://dbpedia.org/ontology/Skater) # noqa: E501

    :param id: The ID of the Skater to be retrieved
    :type id: str

    :rtype: Skater
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SKATER_TYPE_URI,
        rdf_type_name=SKATER_TYPE_NAME, 
        kls=Skater)
