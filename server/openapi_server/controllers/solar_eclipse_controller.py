import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SOLARECLIPSE_TYPE_NAME, SOLARECLIPSE_TYPE_URI

from openapi_server.models.solar_eclipse import SolarEclipse  # noqa: E501
from openapi_server import util

def solareclipses_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SolarEclipse

    Gets a list of all instances of SolarEclipse (more information in http://dbpedia.org/ontology/SolarEclipse) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SolarEclipse]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SOLARECLIPSE_TYPE_URI,
        rdf_type_name=SOLARECLIPSE_TYPE_NAME, 
        kls=SolarEclipse)

def solareclipses_id_get(id):  # noqa: E501
    """Get a single SolarEclipse by its id

    Gets the details of a given SolarEclipse (more information in http://dbpedia.org/ontology/SolarEclipse) # noqa: E501

    :param id: The ID of the SolarEclipse to be retrieved
    :type id: str

    :rtype: SolarEclipse
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SOLARECLIPSE_TYPE_URI,
        rdf_type_name=SOLARECLIPSE_TYPE_NAME, 
        kls=SolarEclipse)
