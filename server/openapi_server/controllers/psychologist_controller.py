import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PSYCHOLOGIST_TYPE_NAME, PSYCHOLOGIST_TYPE_URI

from openapi_server.models.psychologist import Psychologist  # noqa: E501
from openapi_server import util

def psychologists_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Psychologist

    Gets a list of all instances of Psychologist (more information in http://dbpedia.org/ontology/Psychologist) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Psychologist]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PSYCHOLOGIST_TYPE_URI,
        rdf_type_name=PSYCHOLOGIST_TYPE_NAME, 
        kls=Psychologist)

def psychologists_id_get(id):  # noqa: E501
    """Get a single Psychologist by its id

    Gets the details of a given Psychologist (more information in http://dbpedia.org/ontology/Psychologist) # noqa: E501

    :param id: The ID of the Psychologist to be retrieved
    :type id: str

    :rtype: Psychologist
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PSYCHOLOGIST_TYPE_URI,
        rdf_type_name=PSYCHOLOGIST_TYPE_NAME, 
        kls=Psychologist)
