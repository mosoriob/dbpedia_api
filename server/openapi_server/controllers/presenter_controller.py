import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PRESENTER_TYPE_NAME, PRESENTER_TYPE_URI

from openapi_server.models.presenter import Presenter  # noqa: E501
from openapi_server import util

def presenters_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Presenter

    Gets a list of all instances of Presenter (more information in http://dbpedia.org/ontology/Presenter) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Presenter]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PRESENTER_TYPE_URI,
        rdf_type_name=PRESENTER_TYPE_NAME, 
        kls=Presenter)

def presenters_id_get(id):  # noqa: E501
    """Get a single Presenter by its id

    Gets the details of a given Presenter (more information in http://dbpedia.org/ontology/Presenter) # noqa: E501

    :param id: The ID of the Presenter to be retrieved
    :type id: str

    :rtype: Presenter
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PRESENTER_TYPE_URI,
        rdf_type_name=PRESENTER_TYPE_NAME, 
        kls=Presenter)
