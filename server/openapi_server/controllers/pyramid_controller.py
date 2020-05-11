import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PYRAMID_TYPE_NAME, PYRAMID_TYPE_URI

from openapi_server.models.pyramid import Pyramid  # noqa: E501
from openapi_server import util

def pyramids_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Pyramid

    Gets a list of all instances of Pyramid (more information in http://dbpedia.org/ontology/Pyramid) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Pyramid]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PYRAMID_TYPE_URI,
        rdf_type_name=PYRAMID_TYPE_NAME, 
        kls=Pyramid)

def pyramids_id_get(id):  # noqa: E501
    """Get a single Pyramid by its id

    Gets the details of a given Pyramid (more information in http://dbpedia.org/ontology/Pyramid) # noqa: E501

    :param id: The ID of the Pyramid to be retrieved
    :type id: str

    :rtype: Pyramid
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PYRAMID_TYPE_URI,
        rdf_type_name=PYRAMID_TYPE_NAME, 
        kls=Pyramid)
