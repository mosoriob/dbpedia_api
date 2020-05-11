import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GLOBULARSWARM_TYPE_NAME, GLOBULARSWARM_TYPE_URI

from openapi_server.models.globularswarm import Globularswarm  # noqa: E501
from openapi_server import util

def globularswarms_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Globularswarm

    Gets a list of all instances of Globularswarm (more information in http://dbpedia.org/ontology/Globularswarm) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Globularswarm]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GLOBULARSWARM_TYPE_URI,
        rdf_type_name=GLOBULARSWARM_TYPE_NAME, 
        kls=Globularswarm)

def globularswarms_id_get(id):  # noqa: E501
    """Get a single Globularswarm by its id

    Gets the details of a given Globularswarm (more information in http://dbpedia.org/ontology/Globularswarm) # noqa: E501

    :param id: The ID of the Globularswarm to be retrieved
    :type id: str

    :rtype: Globularswarm
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GLOBULARSWARM_TYPE_URI,
        rdf_type_name=GLOBULARSWARM_TYPE_NAME, 
        kls=Globularswarm)
