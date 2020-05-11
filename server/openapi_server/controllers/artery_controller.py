import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ARTERY_TYPE_NAME, ARTERY_TYPE_URI

from openapi_server.models.artery import Artery  # noqa: E501
from openapi_server import util

def arterys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Artery

    Gets a list of all instances of Artery (more information in http://dbpedia.org/ontology/Artery) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Artery]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ARTERY_TYPE_URI,
        rdf_type_name=ARTERY_TYPE_NAME, 
        kls=Artery)

def arterys_id_get(id):  # noqa: E501
    """Get a single Artery by its id

    Gets the details of a given Artery (more information in http://dbpedia.org/ontology/Artery) # noqa: E501

    :param id: The ID of the Artery to be retrieved
    :type id: str

    :rtype: Artery
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ARTERY_TYPE_URI,
        rdf_type_name=ARTERY_TYPE_NAME, 
        kls=Artery)
