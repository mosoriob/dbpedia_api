import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ARCHEOLOGIST_TYPE_NAME, ARCHEOLOGIST_TYPE_URI

from openapi_server.models.archeologist import Archeologist  # noqa: E501
from openapi_server import util

def archeologists_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Archeologist

    Gets a list of all instances of Archeologist (more information in http://dbpedia.org/ontology/Archeologist) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Archeologist]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ARCHEOLOGIST_TYPE_URI,
        rdf_type_name=ARCHEOLOGIST_TYPE_NAME, 
        kls=Archeologist)

def archeologists_id_get(id):  # noqa: E501
    """Get a single Archeologist by its id

    Gets the details of a given Archeologist (more information in http://dbpedia.org/ontology/Archeologist) # noqa: E501

    :param id: The ID of the Archeologist to be retrieved
    :type id: str

    :rtype: Archeologist
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ARCHEOLOGIST_TYPE_URI,
        rdf_type_name=ARCHEOLOGIST_TYPE_NAME, 
        kls=Archeologist)
