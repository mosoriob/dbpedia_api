import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SKIRESORT_TYPE_NAME, SKIRESORT_TYPE_URI

from openapi_server.models.ski_resort import SkiResort  # noqa: E501
from openapi_server import util

def skiresorts_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SkiResort

    Gets a list of all instances of SkiResort (more information in http://dbpedia.org/ontology/SkiResort) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SkiResort]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SKIRESORT_TYPE_URI,
        rdf_type_name=SKIRESORT_TYPE_NAME, 
        kls=SkiResort)

def skiresorts_id_get(id):  # noqa: E501
    """Get a single SkiResort by its id

    Gets the details of a given SkiResort (more information in http://dbpedia.org/ontology/SkiResort) # noqa: E501

    :param id: The ID of the SkiResort to be retrieved
    :type id: str

    :rtype: SkiResort
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SKIRESORT_TYPE_URI,
        rdf_type_name=SKIRESORT_TYPE_NAME, 
        kls=SkiResort)
