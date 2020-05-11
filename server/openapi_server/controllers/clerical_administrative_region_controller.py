import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CLERICALADMINISTRATIVEREGION_TYPE_NAME, CLERICALADMINISTRATIVEREGION_TYPE_URI

from openapi_server.models.clerical_administrative_region import ClericalAdministrativeRegion  # noqa: E501
from openapi_server import util

def clericaladministrativeregions_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of ClericalAdministrativeRegion

    Gets a list of all instances of ClericalAdministrativeRegion (more information in http://dbpedia.org/ontology/ClericalAdministrativeRegion) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[ClericalAdministrativeRegion]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CLERICALADMINISTRATIVEREGION_TYPE_URI,
        rdf_type_name=CLERICALADMINISTRATIVEREGION_TYPE_NAME, 
        kls=ClericalAdministrativeRegion)

def clericaladministrativeregions_id_get(id):  # noqa: E501
    """Get a single ClericalAdministrativeRegion by its id

    Gets the details of a given ClericalAdministrativeRegion (more information in http://dbpedia.org/ontology/ClericalAdministrativeRegion) # noqa: E501

    :param id: The ID of the ClericalAdministrativeRegion to be retrieved
    :type id: str

    :rtype: ClericalAdministrativeRegion
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CLERICALADMINISTRATIVEREGION_TYPE_URI,
        rdf_type_name=CLERICALADMINISTRATIVEREGION_TYPE_NAME, 
        kls=ClericalAdministrativeRegion)
