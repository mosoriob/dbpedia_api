import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import FLOWERINGPLANT_TYPE_NAME, FLOWERINGPLANT_TYPE_URI

from openapi_server.models.flowering_plant import FloweringPlant  # noqa: E501
from openapi_server import util

def floweringplants_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of FloweringPlant

    Gets a list of all instances of FloweringPlant (more information in http://dbpedia.org/ontology/FloweringPlant) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[FloweringPlant]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=FLOWERINGPLANT_TYPE_URI,
        rdf_type_name=FLOWERINGPLANT_TYPE_NAME, 
        kls=FloweringPlant)

def floweringplants_id_get(id):  # noqa: E501
    """Get a single FloweringPlant by its id

    Gets the details of a given FloweringPlant (more information in http://dbpedia.org/ontology/FloweringPlant) # noqa: E501

    :param id: The ID of the FloweringPlant to be retrieved
    :type id: str

    :rtype: FloweringPlant
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=FLOWERINGPLANT_TYPE_URI,
        rdf_type_name=FLOWERINGPLANT_TYPE_NAME, 
        kls=FloweringPlant)
