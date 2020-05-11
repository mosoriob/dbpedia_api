import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import HORSERIDER_TYPE_NAME, HORSERIDER_TYPE_URI

from openapi_server.models.horse_rider import HorseRider  # noqa: E501
from openapi_server import util

def horseriders_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of HorseRider

    Gets a list of all instances of HorseRider (more information in http://dbpedia.org/ontology/HorseRider) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[HorseRider]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=HORSERIDER_TYPE_URI,
        rdf_type_name=HORSERIDER_TYPE_NAME, 
        kls=HorseRider)

def horseriders_id_get(id):  # noqa: E501
    """Get a single HorseRider by its id

    Gets the details of a given HorseRider (more information in http://dbpedia.org/ontology/HorseRider) # noqa: E501

    :param id: The ID of the HorseRider to be retrieved
    :type id: str

    :rtype: HorseRider
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=HORSERIDER_TYPE_URI,
        rdf_type_name=HORSERIDER_TYPE_NAME, 
        kls=HorseRider)
