import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import EMBRYOLOGY_TYPE_NAME, EMBRYOLOGY_TYPE_URI

from openapi_server.models.embryology import Embryology  # noqa: E501
from openapi_server import util

def embryologys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Embryology

    Gets a list of all instances of Embryology (more information in http://dbpedia.org/ontology/Embryology) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Embryology]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=EMBRYOLOGY_TYPE_URI,
        rdf_type_name=EMBRYOLOGY_TYPE_NAME, 
        kls=Embryology)

def embryologys_id_get(id):  # noqa: E501
    """Get a single Embryology by its id

    Gets the details of a given Embryology (more information in http://dbpedia.org/ontology/Embryology) # noqa: E501

    :param id: The ID of the Embryology to be retrieved
    :type id: str

    :rtype: Embryology
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=EMBRYOLOGY_TYPE_URI,
        rdf_type_name=EMBRYOLOGY_TYPE_NAME, 
        kls=Embryology)
