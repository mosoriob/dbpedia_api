import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import OVERSEASDEPARTMENT_TYPE_NAME, OVERSEASDEPARTMENT_TYPE_URI

from openapi_server.models.overseas_department import OverseasDepartment  # noqa: E501
from openapi_server import util

def overseasdepartments_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of OverseasDepartment

    Gets a list of all instances of OverseasDepartment (more information in http://dbpedia.org/ontology/OverseasDepartment) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[OverseasDepartment]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=OVERSEASDEPARTMENT_TYPE_URI,
        rdf_type_name=OVERSEASDEPARTMENT_TYPE_NAME, 
        kls=OverseasDepartment)

def overseasdepartments_id_get(id):  # noqa: E501
    """Get a single OverseasDepartment by its id

    Gets the details of a given OverseasDepartment (more information in http://dbpedia.org/ontology/OverseasDepartment) # noqa: E501

    :param id: The ID of the OverseasDepartment to be retrieved
    :type id: str

    :rtype: OverseasDepartment
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=OVERSEASDEPARTMENT_TYPE_URI,
        rdf_type_name=OVERSEASDEPARTMENT_TYPE_NAME, 
        kls=OverseasDepartment)
