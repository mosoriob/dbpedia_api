import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import OLYMPICRESULT_TYPE_NAME, OLYMPICRESULT_TYPE_URI

from openapi_server.models.olympic_result import OlympicResult  # noqa: E501
from openapi_server import util

def olympicresults_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of OlympicResult

    Gets a list of all instances of OlympicResult (more information in http://dbpedia.org/ontology/OlympicResult) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[OlympicResult]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=OLYMPICRESULT_TYPE_URI,
        rdf_type_name=OLYMPICRESULT_TYPE_NAME, 
        kls=OlympicResult)

def olympicresults_id_get(id):  # noqa: E501
    """Get a single OlympicResult by its id

    Gets the details of a given OlympicResult (more information in http://dbpedia.org/ontology/OlympicResult) # noqa: E501

    :param id: The ID of the OlympicResult to be retrieved
    :type id: str

    :rtype: OlympicResult
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=OLYMPICRESULT_TYPE_URI,
        rdf_type_name=OLYMPICRESULT_TYPE_NAME, 
        kls=OlympicResult)
