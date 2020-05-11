import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import RELIGIOUSBUILDING_TYPE_NAME, RELIGIOUSBUILDING_TYPE_URI

from openapi_server.models.religious_building import ReligiousBuilding  # noqa: E501
from openapi_server import util

def religiousbuildings_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of ReligiousBuilding

    Gets a list of all instances of ReligiousBuilding (more information in http://dbpedia.org/ontology/ReligiousBuilding) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[ReligiousBuilding]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=RELIGIOUSBUILDING_TYPE_URI,
        rdf_type_name=RELIGIOUSBUILDING_TYPE_NAME, 
        kls=ReligiousBuilding)

def religiousbuildings_id_get(id):  # noqa: E501
    """Get a single ReligiousBuilding by its id

    Gets the details of a given ReligiousBuilding (more information in http://dbpedia.org/ontology/ReligiousBuilding) # noqa: E501

    :param id: The ID of the ReligiousBuilding to be retrieved
    :type id: str

    :rtype: ReligiousBuilding
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=RELIGIOUSBUILDING_TYPE_URI,
        rdf_type_name=RELIGIOUSBUILDING_TYPE_NAME, 
        kls=ReligiousBuilding)
