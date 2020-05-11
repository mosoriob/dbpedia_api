import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import AMUSEMENTPARKATTRACTION_TYPE_NAME, AMUSEMENTPARKATTRACTION_TYPE_URI

from openapi_server.models.amusement_park_attraction import AmusementParkAttraction  # noqa: E501
from openapi_server import util

def amusementparkattractions_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of AmusementParkAttraction

    Gets a list of all instances of AmusementParkAttraction (more information in http://dbpedia.org/ontology/AmusementParkAttraction) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[AmusementParkAttraction]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=AMUSEMENTPARKATTRACTION_TYPE_URI,
        rdf_type_name=AMUSEMENTPARKATTRACTION_TYPE_NAME, 
        kls=AmusementParkAttraction)

def amusementparkattractions_id_get(id):  # noqa: E501
    """Get a single AmusementParkAttraction by its id

    Gets the details of a given AmusementParkAttraction (more information in http://dbpedia.org/ontology/AmusementParkAttraction) # noqa: E501

    :param id: The ID of the AmusementParkAttraction to be retrieved
    :type id: str

    :rtype: AmusementParkAttraction
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=AMUSEMENTPARKATTRACTION_TYPE_URI,
        rdf_type_name=AMUSEMENTPARKATTRACTION_TYPE_NAME, 
        kls=AmusementParkAttraction)
