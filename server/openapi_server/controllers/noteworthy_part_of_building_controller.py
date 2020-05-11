import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import NOTEWORTHYPARTOFBUILDING_TYPE_NAME, NOTEWORTHYPARTOFBUILDING_TYPE_URI

from openapi_server.models.noteworthy_part_of_building import NoteworthyPartOfBuilding  # noqa: E501
from openapi_server import util

def noteworthypartofbuildings_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of NoteworthyPartOfBuilding

    Gets a list of all instances of NoteworthyPartOfBuilding (more information in http://dbpedia.org/ontology/NoteworthyPartOfBuilding) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[NoteworthyPartOfBuilding]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=NOTEWORTHYPARTOFBUILDING_TYPE_URI,
        rdf_type_name=NOTEWORTHYPARTOFBUILDING_TYPE_NAME, 
        kls=NoteworthyPartOfBuilding)

def noteworthypartofbuildings_id_get(id):  # noqa: E501
    """Get a single NoteworthyPartOfBuilding by its id

    Gets the details of a given NoteworthyPartOfBuilding (more information in http://dbpedia.org/ontology/NoteworthyPartOfBuilding) # noqa: E501

    :param id: The ID of the NoteworthyPartOfBuilding to be retrieved
    :type id: str

    :rtype: NoteworthyPartOfBuilding
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=NOTEWORTHYPARTOFBUILDING_TYPE_URI,
        rdf_type_name=NOTEWORTHYPARTOFBUILDING_TYPE_NAME, 
        kls=NoteworthyPartOfBuilding)
