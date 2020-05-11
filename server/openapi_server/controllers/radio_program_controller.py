import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import RADIOPROGRAM_TYPE_NAME, RADIOPROGRAM_TYPE_URI

from openapi_server.models.radio_program import RadioProgram  # noqa: E501
from openapi_server import util

def radioprograms_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of RadioProgram

    Gets a list of all instances of RadioProgram (more information in http://dbpedia.org/ontology/RadioProgram) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[RadioProgram]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=RADIOPROGRAM_TYPE_URI,
        rdf_type_name=RADIOPROGRAM_TYPE_NAME, 
        kls=RadioProgram)

def radioprograms_id_get(id):  # noqa: E501
    """Get a single RadioProgram by its id

    Gets the details of a given RadioProgram (more information in http://dbpedia.org/ontology/RadioProgram) # noqa: E501

    :param id: The ID of the RadioProgram to be retrieved
    :type id: str

    :rtype: RadioProgram
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=RADIOPROGRAM_TYPE_URI,
        rdf_type_name=RADIOPROGRAM_TYPE_NAME, 
        kls=RadioProgram)
