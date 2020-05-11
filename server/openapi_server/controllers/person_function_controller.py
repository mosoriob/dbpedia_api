import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PERSONFUNCTION_TYPE_NAME, PERSONFUNCTION_TYPE_URI

from openapi_server.models.person_function import PersonFunction  # noqa: E501
from openapi_server import util

def personfunctions_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of PersonFunction

    Gets a list of all instances of PersonFunction (more information in http://dbpedia.org/ontology/PersonFunction) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[PersonFunction]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PERSONFUNCTION_TYPE_URI,
        rdf_type_name=PERSONFUNCTION_TYPE_NAME, 
        kls=PersonFunction)

def personfunctions_id_get(id):  # noqa: E501
    """Get a single PersonFunction by its id

    Gets the details of a given PersonFunction (more information in http://dbpedia.org/ontology/PersonFunction) # noqa: E501

    :param id: The ID of the PersonFunction to be retrieved
    :type id: str

    :rtype: PersonFunction
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PERSONFUNCTION_TYPE_URI,
        rdf_type_name=PERSONFUNCTION_TYPE_NAME, 
        kls=PersonFunction)
