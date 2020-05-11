import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CRICKETGROUND_TYPE_NAME, CRICKETGROUND_TYPE_URI

from openapi_server.models.cricket_ground import CricketGround  # noqa: E501
from openapi_server import util

def cricketgrounds_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of CricketGround

    Gets a list of all instances of CricketGround (more information in http://dbpedia.org/ontology/CricketGround) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[CricketGround]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CRICKETGROUND_TYPE_URI,
        rdf_type_name=CRICKETGROUND_TYPE_NAME, 
        kls=CricketGround)

def cricketgrounds_id_get(id):  # noqa: E501
    """Get a single CricketGround by its id

    Gets the details of a given CricketGround (more information in http://dbpedia.org/ontology/CricketGround) # noqa: E501

    :param id: The ID of the CricketGround to be retrieved
    :type id: str

    :rtype: CricketGround
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CRICKETGROUND_TYPE_URI,
        rdf_type_name=CRICKETGROUND_TYPE_NAME, 
        kls=CricketGround)
