import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SCULPTOR_TYPE_NAME, SCULPTOR_TYPE_URI

from openapi_server.models.sculptor import Sculptor  # noqa: E501
from openapi_server import util

def sculptors_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Sculptor

    Gets a list of all instances of Sculptor (more information in http://dbpedia.org/ontology/Sculptor) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Sculptor]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SCULPTOR_TYPE_URI,
        rdf_type_name=SCULPTOR_TYPE_NAME, 
        kls=Sculptor)

def sculptors_id_get(id):  # noqa: E501
    """Get a single Sculptor by its id

    Gets the details of a given Sculptor (more information in http://dbpedia.org/ontology/Sculptor) # noqa: E501

    :param id: The ID of the Sculptor to be retrieved
    :type id: str

    :rtype: Sculptor
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SCULPTOR_TYPE_URI,
        rdf_type_name=SCULPTOR_TYPE_NAME, 
        kls=Sculptor)
