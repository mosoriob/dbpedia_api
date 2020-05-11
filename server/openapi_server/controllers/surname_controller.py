import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SURNAME_TYPE_NAME, SURNAME_TYPE_URI

from openapi_server.models.surname import Surname  # noqa: E501
from openapi_server import util

def surnames_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Surname

    Gets a list of all instances of Surname (more information in http://dbpedia.org/ontology/Surname) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Surname]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SURNAME_TYPE_URI,
        rdf_type_name=SURNAME_TYPE_NAME, 
        kls=Surname)

def surnames_id_get(id):  # noqa: E501
    """Get a single Surname by its id

    Gets the details of a given Surname (more information in http://dbpedia.org/ontology/Surname) # noqa: E501

    :param id: The ID of the Surname to be retrieved
    :type id: str

    :rtype: Surname
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SURNAME_TYPE_URI,
        rdf_type_name=SURNAME_TYPE_NAME, 
        kls=Surname)
