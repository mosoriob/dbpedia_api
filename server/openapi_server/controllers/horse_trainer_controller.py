import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import HORSETRAINER_TYPE_NAME, HORSETRAINER_TYPE_URI

from openapi_server.models.horse_trainer import HorseTrainer  # noqa: E501
from openapi_server import util

def horsetrainers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of HorseTrainer

    Gets a list of all instances of HorseTrainer (more information in http://dbpedia.org/ontology/HorseTrainer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[HorseTrainer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=HORSETRAINER_TYPE_URI,
        rdf_type_name=HORSETRAINER_TYPE_NAME, 
        kls=HorseTrainer)

def horsetrainers_id_get(id):  # noqa: E501
    """Get a single HorseTrainer by its id

    Gets the details of a given HorseTrainer (more information in http://dbpedia.org/ontology/HorseTrainer) # noqa: E501

    :param id: The ID of the HorseTrainer to be retrieved
    :type id: str

    :rtype: HorseTrainer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=HORSETRAINER_TYPE_URI,
        rdf_type_name=HORSETRAINER_TYPE_NAME, 
        kls=HorseTrainer)
