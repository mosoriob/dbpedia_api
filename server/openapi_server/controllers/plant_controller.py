import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PLANT_TYPE_NAME, PLANT_TYPE_URI

from openapi_server.models.plant import Plant  # noqa: E501
from openapi_server import util

def plants_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Plant

    Gets a list of all instances of Plant (more information in http://dbpedia.org/ontology/Plant) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Plant]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PLANT_TYPE_URI,
        rdf_type_name=PLANT_TYPE_NAME, 
        kls=Plant)

def plants_id_get(id):  # noqa: E501
    """Get a single Plant by its id

    Gets the details of a given Plant (more information in http://dbpedia.org/ontology/Plant) # noqa: E501

    :param id: The ID of the Plant to be retrieved
    :type id: str

    :rtype: Plant
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PLANT_TYPE_URI,
        rdf_type_name=PLANT_TYPE_NAME, 
        kls=Plant)
