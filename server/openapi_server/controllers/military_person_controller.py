import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MILITARYPERSON_TYPE_NAME, MILITARYPERSON_TYPE_URI

from openapi_server.models.military_person import MilitaryPerson  # noqa: E501
from openapi_server import util

def militarypersons_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of MilitaryPerson

    Gets a list of all instances of MilitaryPerson (more information in http://dbpedia.org/ontology/MilitaryPerson) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[MilitaryPerson]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MILITARYPERSON_TYPE_URI,
        rdf_type_name=MILITARYPERSON_TYPE_NAME, 
        kls=MilitaryPerson)

def militarypersons_id_get(id):  # noqa: E501
    """Get a single MilitaryPerson by its id

    Gets the details of a given MilitaryPerson (more information in http://dbpedia.org/ontology/MilitaryPerson) # noqa: E501

    :param id: The ID of the MilitaryPerson to be retrieved
    :type id: str

    :rtype: MilitaryPerson
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MILITARYPERSON_TYPE_URI,
        rdf_type_name=MILITARYPERSON_TYPE_NAME, 
        kls=MilitaryPerson)
