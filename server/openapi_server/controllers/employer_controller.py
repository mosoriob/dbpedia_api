import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import EMPLOYER_TYPE_NAME, EMPLOYER_TYPE_URI

from openapi_server.models.employer import Employer  # noqa: E501
from openapi_server import util

def employers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Employer

    Gets a list of all instances of Employer (more information in http://dbpedia.org/ontology/Employer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Employer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=EMPLOYER_TYPE_URI,
        rdf_type_name=EMPLOYER_TYPE_NAME, 
        kls=Employer)

def employers_id_get(id):  # noqa: E501
    """Get a single Employer by its id

    Gets the details of a given Employer (more information in http://dbpedia.org/ontology/Employer) # noqa: E501

    :param id: The ID of the Employer to be retrieved
    :type id: str

    :rtype: Employer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=EMPLOYER_TYPE_URI,
        rdf_type_name=EMPLOYER_TYPE_NAME, 
        kls=Employer)
