import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SUMOWRESTLER_TYPE_NAME, SUMOWRESTLER_TYPE_URI

from openapi_server.models.sumo_wrestler import SumoWrestler  # noqa: E501
from openapi_server import util

def sumowrestlers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SumoWrestler

    Gets a list of all instances of SumoWrestler (more information in http://dbpedia.org/ontology/SumoWrestler) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SumoWrestler]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SUMOWRESTLER_TYPE_URI,
        rdf_type_name=SUMOWRESTLER_TYPE_NAME, 
        kls=SumoWrestler)

def sumowrestlers_id_get(id):  # noqa: E501
    """Get a single SumoWrestler by its id

    Gets the details of a given SumoWrestler (more information in http://dbpedia.org/ontology/SumoWrestler) # noqa: E501

    :param id: The ID of the SumoWrestler to be retrieved
    :type id: str

    :rtype: SumoWrestler
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SUMOWRESTLER_TYPE_URI,
        rdf_type_name=SUMOWRESTLER_TYPE_NAME, 
        kls=SumoWrestler)
