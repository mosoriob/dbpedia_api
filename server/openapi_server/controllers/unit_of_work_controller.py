import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import UNITOFWORK_TYPE_NAME, UNITOFWORK_TYPE_URI

from openapi_server.models.unit_of_work import UnitOfWork  # noqa: E501
from openapi_server import util

def unitofworks_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of UnitOfWork

    Gets a list of all instances of UnitOfWork (more information in http://dbpedia.org/ontology/UnitOfWork) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[UnitOfWork]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=UNITOFWORK_TYPE_URI,
        rdf_type_name=UNITOFWORK_TYPE_NAME, 
        kls=UnitOfWork)

def unitofworks_id_get(id):  # noqa: E501
    """Get a single UnitOfWork by its id

    Gets the details of a given UnitOfWork (more information in http://dbpedia.org/ontology/UnitOfWork) # noqa: E501

    :param id: The ID of the UnitOfWork to be retrieved
    :type id: str

    :rtype: UnitOfWork
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=UNITOFWORK_TYPE_URI,
        rdf_type_name=UNITOFWORK_TYPE_NAME, 
        kls=UnitOfWork)
