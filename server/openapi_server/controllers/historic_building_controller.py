import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import HISTORICBUILDING_TYPE_NAME, HISTORICBUILDING_TYPE_URI

from openapi_server.models.historic_building import HistoricBuilding  # noqa: E501
from openapi_server import util

def historicbuildings_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of HistoricBuilding

    Gets a list of all instances of HistoricBuilding (more information in http://dbpedia.org/ontology/HistoricBuilding) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[HistoricBuilding]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=HISTORICBUILDING_TYPE_URI,
        rdf_type_name=HISTORICBUILDING_TYPE_NAME, 
        kls=HistoricBuilding)

def historicbuildings_id_get(id):  # noqa: E501
    """Get a single HistoricBuilding by its id

    Gets the details of a given HistoricBuilding (more information in http://dbpedia.org/ontology/HistoricBuilding) # noqa: E501

    :param id: The ID of the HistoricBuilding to be retrieved
    :type id: str

    :rtype: HistoricBuilding
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=HISTORICBUILDING_TYPE_URI,
        rdf_type_name=HISTORICBUILDING_TYPE_NAME, 
        kls=HistoricBuilding)
