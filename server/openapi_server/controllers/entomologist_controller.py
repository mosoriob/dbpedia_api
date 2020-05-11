import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ENTOMOLOGIST_TYPE_NAME, ENTOMOLOGIST_TYPE_URI

from openapi_server.models.entomologist import Entomologist  # noqa: E501
from openapi_server import util

def entomologists_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Entomologist

    Gets a list of all instances of Entomologist (more information in http://dbpedia.org/ontology/Entomologist) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Entomologist]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ENTOMOLOGIST_TYPE_URI,
        rdf_type_name=ENTOMOLOGIST_TYPE_NAME, 
        kls=Entomologist)

def entomologists_id_get(id):  # noqa: E501
    """Get a single Entomologist by its id

    Gets the details of a given Entomologist (more information in http://dbpedia.org/ontology/Entomologist) # noqa: E501

    :param id: The ID of the Entomologist to be retrieved
    :type id: str

    :rtype: Entomologist
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ENTOMOLOGIST_TYPE_URI,
        rdf_type_name=ENTOMOLOGIST_TYPE_NAME, 
        kls=Entomologist)
