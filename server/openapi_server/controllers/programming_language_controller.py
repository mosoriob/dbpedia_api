import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PROGRAMMINGLANGUAGE_TYPE_NAME, PROGRAMMINGLANGUAGE_TYPE_URI

from openapi_server.models.programming_language import ProgrammingLanguage  # noqa: E501
from openapi_server import util

def programminglanguages_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of ProgrammingLanguage

    Gets a list of all instances of ProgrammingLanguage (more information in http://dbpedia.org/ontology/ProgrammingLanguage) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[ProgrammingLanguage]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PROGRAMMINGLANGUAGE_TYPE_URI,
        rdf_type_name=PROGRAMMINGLANGUAGE_TYPE_NAME, 
        kls=ProgrammingLanguage)

def programminglanguages_id_get(id):  # noqa: E501
    """Get a single ProgrammingLanguage by its id

    Gets the details of a given ProgrammingLanguage (more information in http://dbpedia.org/ontology/ProgrammingLanguage) # noqa: E501

    :param id: The ID of the ProgrammingLanguage to be retrieved
    :type id: str

    :rtype: ProgrammingLanguage
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PROGRAMMINGLANGUAGE_TYPE_URI,
        rdf_type_name=PROGRAMMINGLANGUAGE_TYPE_NAME, 
        kls=ProgrammingLanguage)
