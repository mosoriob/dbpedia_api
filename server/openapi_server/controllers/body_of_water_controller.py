import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BODYOFWATER_TYPE_NAME, BODYOFWATER_TYPE_URI

from openapi_server.models.body_of_water import BodyOfWater  # noqa: E501
from openapi_server import util

def bodyofwaters_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of BodyOfWater

    Gets a list of all instances of BodyOfWater (more information in http://dbpedia.org/ontology/BodyOfWater) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[BodyOfWater]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BODYOFWATER_TYPE_URI,
        rdf_type_name=BODYOFWATER_TYPE_NAME, 
        kls=BodyOfWater)

def bodyofwaters_id_get(id):  # noqa: E501
    """Get a single BodyOfWater by its id

    Gets the details of a given BodyOfWater (more information in http://dbpedia.org/ontology/BodyOfWater) # noqa: E501

    :param id: The ID of the BodyOfWater to be retrieved
    :type id: str

    :rtype: BodyOfWater
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BODYOFWATER_TYPE_URI,
        rdf_type_name=BODYOFWATER_TYPE_NAME, 
        kls=BodyOfWater)
