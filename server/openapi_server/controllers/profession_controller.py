import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PROFESSION_TYPE_NAME, PROFESSION_TYPE_URI

from openapi_server.models.profession import Profession  # noqa: E501
from openapi_server import util

def professions_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Profession

    Gets a list of all instances of Profession (more information in http://dbpedia.org/ontology/Profession) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Profession]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PROFESSION_TYPE_URI,
        rdf_type_name=PROFESSION_TYPE_NAME, 
        kls=Profession)

def professions_id_get(id):  # noqa: E501
    """Get a single Profession by its id

    Gets the details of a given Profession (more information in http://dbpedia.org/ontology/Profession) # noqa: E501

    :param id: The ID of the Profession to be retrieved
    :type id: str

    :rtype: Profession
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PROFESSION_TYPE_URI,
        rdf_type_name=PROFESSION_TYPE_NAME, 
        kls=Profession)
