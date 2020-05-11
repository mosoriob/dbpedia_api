import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ARTIFICIALSATELLITE_TYPE_NAME, ARTIFICIALSATELLITE_TYPE_URI

from openapi_server.models.artificial_satellite import ArtificialSatellite  # noqa: E501
from openapi_server import util

def artificialsatellites_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of ArtificialSatellite

    Gets a list of all instances of ArtificialSatellite (more information in http://dbpedia.org/ontology/ArtificialSatellite) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[ArtificialSatellite]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ARTIFICIALSATELLITE_TYPE_URI,
        rdf_type_name=ARTIFICIALSATELLITE_TYPE_NAME, 
        kls=ArtificialSatellite)

def artificialsatellites_id_get(id):  # noqa: E501
    """Get a single ArtificialSatellite by its id

    Gets the details of a given ArtificialSatellite (more information in http://dbpedia.org/ontology/ArtificialSatellite) # noqa: E501

    :param id: The ID of the ArtificialSatellite to be retrieved
    :type id: str

    :rtype: ArtificialSatellite
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ARTIFICIALSATELLITE_TYPE_URI,
        rdf_type_name=ARTIFICIALSATELLITE_TYPE_NAME, 
        kls=ArtificialSatellite)
