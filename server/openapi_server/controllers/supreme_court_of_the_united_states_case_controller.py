import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SUPREMECOURTOFTHEUNITEDSTATESCASE_TYPE_NAME, SUPREMECOURTOFTHEUNITEDSTATESCASE_TYPE_URI

from openapi_server.models.supreme_court_of_the_united_states_case import SupremeCourtOfTheUnitedStatesCase  # noqa: E501
from openapi_server import util

def supremecourtoftheunitedstatescases_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SupremeCourtOfTheUnitedStatesCase

    Gets a list of all instances of SupremeCourtOfTheUnitedStatesCase (more information in http://dbpedia.org/ontology/SupremeCourtOfTheUnitedStatesCase) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SupremeCourtOfTheUnitedStatesCase]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SUPREMECOURTOFTHEUNITEDSTATESCASE_TYPE_URI,
        rdf_type_name=SUPREMECOURTOFTHEUNITEDSTATESCASE_TYPE_NAME, 
        kls=SupremeCourtOfTheUnitedStatesCase)

def supremecourtoftheunitedstatescases_id_get(id):  # noqa: E501
    """Get a single SupremeCourtOfTheUnitedStatesCase by its id

    Gets the details of a given SupremeCourtOfTheUnitedStatesCase (more information in http://dbpedia.org/ontology/SupremeCourtOfTheUnitedStatesCase) # noqa: E501

    :param id: The ID of the SupremeCourtOfTheUnitedStatesCase to be retrieved
    :type id: str

    :rtype: SupremeCourtOfTheUnitedStatesCase
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SUPREMECOURTOFTHEUNITEDSTATESCASE_TYPE_URI,
        rdf_type_name=SUPREMECOURTOFTHEUNITEDSTATESCASE_TYPE_NAME, 
        kls=SupremeCourtOfTheUnitedStatesCase)
