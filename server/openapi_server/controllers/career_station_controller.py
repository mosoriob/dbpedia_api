import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CAREERSTATION_TYPE_NAME, CAREERSTATION_TYPE_URI

from openapi_server.models.career_station import CareerStation  # noqa: E501
from openapi_server import util

def careerstations_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of CareerStation

    Gets a list of all instances of CareerStation (more information in http://dbpedia.org/ontology/CareerStation) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[CareerStation]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CAREERSTATION_TYPE_URI,
        rdf_type_name=CAREERSTATION_TYPE_NAME, 
        kls=CareerStation)

def careerstations_id_get(id):  # noqa: E501
    """Get a single CareerStation by its id

    Gets the details of a given CareerStation (more information in http://dbpedia.org/ontology/CareerStation) # noqa: E501

    :param id: The ID of the CareerStation to be retrieved
    :type id: str

    :rtype: CareerStation
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CAREERSTATION_TYPE_URI,
        rdf_type_name=CAREERSTATION_TYPE_NAME, 
        kls=CareerStation)
