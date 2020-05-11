import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MOTOCYCLERACER_TYPE_NAME, MOTOCYCLERACER_TYPE_URI

from openapi_server.models.motocycle_racer import MotocycleRacer  # noqa: E501
from openapi_server import util

def motocycleracers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of MotocycleRacer

    Gets a list of all instances of MotocycleRacer (more information in http://dbpedia.org/ontology/MotocycleRacer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[MotocycleRacer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MOTOCYCLERACER_TYPE_URI,
        rdf_type_name=MOTOCYCLERACER_TYPE_NAME, 
        kls=MotocycleRacer)

def motocycleracers_id_get(id):  # noqa: E501
    """Get a single MotocycleRacer by its id

    Gets the details of a given MotocycleRacer (more information in http://dbpedia.org/ontology/MotocycleRacer) # noqa: E501

    :param id: The ID of the MotocycleRacer to be retrieved
    :type id: str

    :rtype: MotocycleRacer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MOTOCYCLERACER_TYPE_URI,
        rdf_type_name=MOTOCYCLERACER_TYPE_NAME, 
        kls=MotocycleRacer)
