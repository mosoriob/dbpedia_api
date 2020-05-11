import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MICROREGION_TYPE_NAME, MICROREGION_TYPE_URI

from openapi_server.models.micro_region import MicroRegion  # noqa: E501
from openapi_server import util

def microregions_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of MicroRegion

    Gets a list of all instances of MicroRegion (more information in http://dbpedia.org/ontology/MicroRegion) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[MicroRegion]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MICROREGION_TYPE_URI,
        rdf_type_name=MICROREGION_TYPE_NAME, 
        kls=MicroRegion)

def microregions_id_get(id):  # noqa: E501
    """Get a single MicroRegion by its id

    Gets the details of a given MicroRegion (more information in http://dbpedia.org/ontology/MicroRegion) # noqa: E501

    :param id: The ID of the MicroRegion to be retrieved
    :type id: str

    :rtype: MicroRegion
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MICROREGION_TYPE_URI,
        rdf_type_name=MICROREGION_TYPE_NAME, 
        kls=MicroRegion)
