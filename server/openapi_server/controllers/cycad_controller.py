import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CYCAD_TYPE_NAME, CYCAD_TYPE_URI

from openapi_server.models.cycad import Cycad  # noqa: E501
from openapi_server import util

def cycads_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Cycad

    Gets a list of all instances of Cycad (more information in http://dbpedia.org/ontology/Cycad) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Cycad]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CYCAD_TYPE_URI,
        rdf_type_name=CYCAD_TYPE_NAME, 
        kls=Cycad)

def cycads_id_get(id):  # noqa: E501
    """Get a single Cycad by its id

    Gets the details of a given Cycad (more information in http://dbpedia.org/ontology/Cycad) # noqa: E501

    :param id: The ID of the Cycad to be retrieved
    :type id: str

    :rtype: Cycad
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CYCAD_TYPE_URI,
        rdf_type_name=CYCAD_TYPE_NAME, 
        kls=Cycad)
