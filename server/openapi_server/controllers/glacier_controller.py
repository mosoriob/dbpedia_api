import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GLACIER_TYPE_NAME, GLACIER_TYPE_URI

from openapi_server.models.glacier import Glacier  # noqa: E501
from openapi_server import util

def glaciers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Glacier

    Gets a list of all instances of Glacier (more information in http://dbpedia.org/ontology/Glacier) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Glacier]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GLACIER_TYPE_URI,
        rdf_type_name=GLACIER_TYPE_NAME, 
        kls=Glacier)

def glaciers_id_get(id):  # noqa: E501
    """Get a single Glacier by its id

    Gets the details of a given Glacier (more information in http://dbpedia.org/ontology/Glacier) # noqa: E501

    :param id: The ID of the Glacier to be retrieved
    :type id: str

    :rtype: Glacier
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GLACIER_TYPE_URI,
        rdf_type_name=GLACIER_TYPE_NAME, 
        kls=Glacier)
