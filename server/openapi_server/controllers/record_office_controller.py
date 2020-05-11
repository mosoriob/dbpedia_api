import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import RECORDOFFICE_TYPE_NAME, RECORDOFFICE_TYPE_URI

from openapi_server.models.record_office import RecordOffice  # noqa: E501
from openapi_server import util

def recordoffices_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of RecordOffice

    Gets a list of all instances of RecordOffice (more information in http://dbpedia.org/ontology/RecordOffice) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[RecordOffice]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=RECORDOFFICE_TYPE_URI,
        rdf_type_name=RECORDOFFICE_TYPE_NAME, 
        kls=RecordOffice)

def recordoffices_id_get(id):  # noqa: E501
    """Get a single RecordOffice by its id

    Gets the details of a given RecordOffice (more information in http://dbpedia.org/ontology/RecordOffice) # noqa: E501

    :param id: The ID of the RecordOffice to be retrieved
    :type id: str

    :rtype: RecordOffice
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=RECORDOFFICE_TYPE_URI,
        rdf_type_name=RECORDOFFICE_TYPE_NAME, 
        kls=RecordOffice)
