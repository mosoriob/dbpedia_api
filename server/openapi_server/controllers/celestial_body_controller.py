import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CELESTIALBODY_TYPE_NAME, CELESTIALBODY_TYPE_URI

from openapi_server.models.celestial_body import CelestialBody  # noqa: E501
from openapi_server import util

def celestialbodys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of CelestialBody

    Gets a list of all instances of CelestialBody (more information in http://dbpedia.org/ontology/CelestialBody) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[CelestialBody]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CELESTIALBODY_TYPE_URI,
        rdf_type_name=CELESTIALBODY_TYPE_NAME, 
        kls=CelestialBody)

def celestialbodys_id_get(id):  # noqa: E501
    """Get a single CelestialBody by its id

    Gets the details of a given CelestialBody (more information in http://dbpedia.org/ontology/CelestialBody) # noqa: E501

    :param id: The ID of the CelestialBody to be retrieved
    :type id: str

    :rtype: CelestialBody
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CELESTIALBODY_TYPE_URI,
        rdf_type_name=CELESTIALBODY_TYPE_NAME, 
        kls=CelestialBody)
