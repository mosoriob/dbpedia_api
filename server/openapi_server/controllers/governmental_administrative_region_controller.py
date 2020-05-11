import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GOVERNMENTALADMINISTRATIVEREGION_TYPE_NAME, GOVERNMENTALADMINISTRATIVEREGION_TYPE_URI

from openapi_server.models.governmental_administrative_region import GovernmentalAdministrativeRegion  # noqa: E501
from openapi_server import util

def governmentaladministrativeregions_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of GovernmentalAdministrativeRegion

    Gets a list of all instances of GovernmentalAdministrativeRegion (more information in http://dbpedia.org/ontology/GovernmentalAdministrativeRegion) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[GovernmentalAdministrativeRegion]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GOVERNMENTALADMINISTRATIVEREGION_TYPE_URI,
        rdf_type_name=GOVERNMENTALADMINISTRATIVEREGION_TYPE_NAME, 
        kls=GovernmentalAdministrativeRegion)

def governmentaladministrativeregions_id_get(id):  # noqa: E501
    """Get a single GovernmentalAdministrativeRegion by its id

    Gets the details of a given GovernmentalAdministrativeRegion (more information in http://dbpedia.org/ontology/GovernmentalAdministrativeRegion) # noqa: E501

    :param id: The ID of the GovernmentalAdministrativeRegion to be retrieved
    :type id: str

    :rtype: GovernmentalAdministrativeRegion
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GOVERNMENTALADMINISTRATIVEREGION_TYPE_URI,
        rdf_type_name=GOVERNMENTALADMINISTRATIVEREGION_TYPE_NAME, 
        kls=GovernmentalAdministrativeRegion)
