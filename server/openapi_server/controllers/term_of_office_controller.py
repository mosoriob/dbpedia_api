import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import TERMOFOFFICE_TYPE_NAME, TERMOFOFFICE_TYPE_URI

from openapi_server.models.term_of_office import TermOfOffice  # noqa: E501
from openapi_server import util

def termofoffices_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of TermOfOffice

    Gets a list of all instances of TermOfOffice (more information in http://dbpedia.org/ontology/TermOfOffice) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[TermOfOffice]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=TERMOFOFFICE_TYPE_URI,
        rdf_type_name=TERMOFOFFICE_TYPE_NAME, 
        kls=TermOfOffice)

def termofoffices_id_get(id):  # noqa: E501
    """Get a single TermOfOffice by its id

    Gets the details of a given TermOfOffice (more information in http://dbpedia.org/ontology/TermOfOffice) # noqa: E501

    :param id: The ID of the TermOfOffice to be retrieved
    :type id: str

    :rtype: TermOfOffice
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=TERMOFOFFICE_TYPE_URI,
        rdf_type_name=TERMOFOFFICE_TYPE_NAME, 
        kls=TermOfOffice)
