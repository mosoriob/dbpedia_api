import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ADMINISTRATIVEREGION_TYPE_NAME, ADMINISTRATIVEREGION_TYPE_URI

from openapi_server.models.administrative_region import AdministrativeRegion  # noqa: E501
from openapi_server import util

def administrativeregions_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of AdministrativeRegion

    Gets a list of all instances of AdministrativeRegion (more information in http://dbpedia.org/ontology/AdministrativeRegion) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[AdministrativeRegion]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ADMINISTRATIVEREGION_TYPE_URI,
        rdf_type_name=ADMINISTRATIVEREGION_TYPE_NAME, 
        kls=AdministrativeRegion)

def administrativeregions_id_get(id):  # noqa: E501
    """Get a single AdministrativeRegion by its id

    Gets the details of a given AdministrativeRegion (more information in http://dbpedia.org/ontology/AdministrativeRegion) # noqa: E501

    :param id: The ID of the AdministrativeRegion to be retrieved
    :type id: str

    :rtype: AdministrativeRegion
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ADMINISTRATIVEREGION_TYPE_URI,
        rdf_type_name=ADMINISTRATIVEREGION_TYPE_NAME, 
        kls=AdministrativeRegion)
