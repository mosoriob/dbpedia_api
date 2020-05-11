import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import HORSERIDING_TYPE_NAME, HORSERIDING_TYPE_URI

from openapi_server.models.horse_riding import HorseRiding  # noqa: E501
from openapi_server import util

def horseridings_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of HorseRiding

    Gets a list of all instances of HorseRiding (more information in http://dbpedia.org/ontology/HorseRiding) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[HorseRiding]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=HORSERIDING_TYPE_URI,
        rdf_type_name=HORSERIDING_TYPE_NAME, 
        kls=HorseRiding)

def horseridings_id_get(id):  # noqa: E501
    """Get a single HorseRiding by its id

    Gets the details of a given HorseRiding (more information in http://dbpedia.org/ontology/HorseRiding) # noqa: E501

    :param id: The ID of the HorseRiding to be retrieved
    :type id: str

    :rtype: HorseRiding
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=HORSERIDING_TYPE_URI,
        rdf_type_name=HORSERIDING_TYPE_NAME, 
        kls=HorseRiding)
