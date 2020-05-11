import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MODEL_TYPE_NAME, MODEL_TYPE_URI

from openapi_server.models.model import Model  # noqa: E501
from openapi_server import util

def models_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Model

    Gets a list of all instances of Model (more information in http://dbpedia.org/ontology/Model) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Model]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MODEL_TYPE_URI,
        rdf_type_name=MODEL_TYPE_NAME, 
        kls=Model)

def models_id_get(id):  # noqa: E501
    """Get a single Model by its id

    Gets the details of a given Model (more information in http://dbpedia.org/ontology/Model) # noqa: E501

    :param id: The ID of the Model to be retrieved
    :type id: str

    :rtype: Model
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MODEL_TYPE_URI,
        rdf_type_name=MODEL_TYPE_NAME, 
        kls=Model)
