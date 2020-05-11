import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ROMANEMPEROR_TYPE_NAME, ROMANEMPEROR_TYPE_URI

from openapi_server.models.roman_emperor import RomanEmperor  # noqa: E501
from openapi_server import util

def romanemperors_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of RomanEmperor

    Gets a list of all instances of RomanEmperor (more information in http://dbpedia.org/ontology/RomanEmperor) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[RomanEmperor]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ROMANEMPEROR_TYPE_URI,
        rdf_type_name=ROMANEMPEROR_TYPE_NAME, 
        kls=RomanEmperor)

def romanemperors_id_get(id):  # noqa: E501
    """Get a single RomanEmperor by its id

    Gets the details of a given RomanEmperor (more information in http://dbpedia.org/ontology/RomanEmperor) # noqa: E501

    :param id: The ID of the RomanEmperor to be retrieved
    :type id: str

    :rtype: RomanEmperor
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ROMANEMPEROR_TYPE_URI,
        rdf_type_name=ROMANEMPEROR_TYPE_NAME, 
        kls=RomanEmperor)
