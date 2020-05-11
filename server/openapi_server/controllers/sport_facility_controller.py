import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SPORTFACILITY_TYPE_NAME, SPORTFACILITY_TYPE_URI

from openapi_server.models.sport_facility import SportFacility  # noqa: E501
from openapi_server import util

def sportfacilitys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SportFacility

    Gets a list of all instances of SportFacility (more information in http://dbpedia.org/ontology/SportFacility) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SportFacility]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SPORTFACILITY_TYPE_URI,
        rdf_type_name=SPORTFACILITY_TYPE_NAME, 
        kls=SportFacility)

def sportfacilitys_id_get(id):  # noqa: E501
    """Get a single SportFacility by its id

    Gets the details of a given SportFacility (more information in http://dbpedia.org/ontology/SportFacility) # noqa: E501

    :param id: The ID of the SportFacility to be retrieved
    :type id: str

    :rtype: SportFacility
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SPORTFACILITY_TYPE_URI,
        rdf_type_name=SPORTFACILITY_TYPE_NAME, 
        kls=SportFacility)
