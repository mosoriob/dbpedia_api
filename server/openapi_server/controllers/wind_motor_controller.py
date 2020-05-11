import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import WINDMOTOR_TYPE_NAME, WINDMOTOR_TYPE_URI

from openapi_server.models.wind_motor import WindMotor  # noqa: E501
from openapi_server import util

def windmotors_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of WindMotor

    Gets a list of all instances of WindMotor (more information in http://dbpedia.org/ontology/WindMotor) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[WindMotor]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=WINDMOTOR_TYPE_URI,
        rdf_type_name=WINDMOTOR_TYPE_NAME, 
        kls=WindMotor)

def windmotors_id_get(id):  # noqa: E501
    """Get a single WindMotor by its id

    Gets the details of a given WindMotor (more information in http://dbpedia.org/ontology/WindMotor) # noqa: E501

    :param id: The ID of the WindMotor to be retrieved
    :type id: str

    :rtype: WindMotor
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=WINDMOTOR_TYPE_URI,
        rdf_type_name=WINDMOTOR_TYPE_NAME, 
        kls=WindMotor)
