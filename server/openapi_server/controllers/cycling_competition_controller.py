import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CYCLINGCOMPETITION_TYPE_NAME, CYCLINGCOMPETITION_TYPE_URI

from openapi_server.models.cycling_competition import CyclingCompetition  # noqa: E501
from openapi_server import util

def cyclingcompetitions_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of CyclingCompetition

    Gets a list of all instances of CyclingCompetition (more information in http://dbpedia.org/ontology/CyclingCompetition) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[CyclingCompetition]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CYCLINGCOMPETITION_TYPE_URI,
        rdf_type_name=CYCLINGCOMPETITION_TYPE_NAME, 
        kls=CyclingCompetition)

def cyclingcompetitions_id_get(id):  # noqa: E501
    """Get a single CyclingCompetition by its id

    Gets the details of a given CyclingCompetition (more information in http://dbpedia.org/ontology/CyclingCompetition) # noqa: E501

    :param id: The ID of the CyclingCompetition to be retrieved
    :type id: str

    :rtype: CyclingCompetition
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CYCLINGCOMPETITION_TYPE_URI,
        rdf_type_name=CYCLINGCOMPETITION_TYPE_NAME, 
        kls=CyclingCompetition)
