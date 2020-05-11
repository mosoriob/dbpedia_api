import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import RACECOURSE_TYPE_NAME, RACECOURSE_TYPE_URI

from openapi_server.models.racecourse import Racecourse  # noqa: E501
from openapi_server import util

def racecourses_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Racecourse

    Gets a list of all instances of Racecourse (more information in http://dbpedia.org/ontology/Racecourse) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Racecourse]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=RACECOURSE_TYPE_URI,
        rdf_type_name=RACECOURSE_TYPE_NAME, 
        kls=Racecourse)

def racecourses_id_get(id):  # noqa: E501
    """Get a single Racecourse by its id

    Gets the details of a given Racecourse (more information in http://dbpedia.org/ontology/Racecourse) # noqa: E501

    :param id: The ID of the Racecourse to be retrieved
    :type id: str

    :rtype: Racecourse
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=RACECOURSE_TYPE_URI,
        rdf_type_name=RACECOURSE_TYPE_NAME, 
        kls=Racecourse)
