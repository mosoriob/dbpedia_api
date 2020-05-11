import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import HISTORICPLACE_TYPE_NAME, HISTORICPLACE_TYPE_URI

from openapi_server.models.historic_place import HistoricPlace  # noqa: E501
from openapi_server import util

def historicplaces_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of HistoricPlace

    Gets a list of all instances of HistoricPlace (more information in http://dbpedia.org/ontology/HistoricPlace) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[HistoricPlace]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=HISTORICPLACE_TYPE_URI,
        rdf_type_name=HISTORICPLACE_TYPE_NAME, 
        kls=HistoricPlace)

def historicplaces_id_get(id):  # noqa: E501
    """Get a single HistoricPlace by its id

    Gets the details of a given HistoricPlace (more information in http://dbpedia.org/ontology/HistoricPlace) # noqa: E501

    :param id: The ID of the HistoricPlace to be retrieved
    :type id: str

    :rtype: HistoricPlace
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=HISTORICPLACE_TYPE_URI,
        rdf_type_name=HISTORICPLACE_TYPE_NAME, 
        kls=HistoricPlace)
