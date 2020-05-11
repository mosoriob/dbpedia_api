import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PERSON_TYPE_NAME, PERSON_TYPE_URI

from openapi_server.models.person import Person  # noqa: E501
from openapi_server import util

def persons_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Person

    Gets a list of all instances of Person (more information in http://dbpedia.org/ontology/Person) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Person]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PERSON_TYPE_URI,
        rdf_type_name=PERSON_TYPE_NAME, 
        kls=Person)

def persons_id_get(id):  # noqa: E501
    """Get a single Person by its id

    Gets the details of a given Person (more information in http://dbpedia.org/ontology/Person) # noqa: E501

    :param id: The ID of the Person to be retrieved
    :type id: str

    :rtype: Person
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PERSON_TYPE_URI,
        rdf_type_name=PERSON_TYPE_NAME, 
        kls=Person)
