import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import FORMULAONETEAM_TYPE_NAME, FORMULAONETEAM_TYPE_URI

from openapi_server.models.formula_one_team import FormulaOneTeam  # noqa: E501
from openapi_server import util

def formulaoneteams_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of FormulaOneTeam

    Gets a list of all instances of FormulaOneTeam (more information in http://dbpedia.org/ontology/FormulaOneTeam) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[FormulaOneTeam]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=FORMULAONETEAM_TYPE_URI,
        rdf_type_name=FORMULAONETEAM_TYPE_NAME, 
        kls=FormulaOneTeam)

def formulaoneteams_id_get(id):  # noqa: E501
    """Get a single FormulaOneTeam by its id

    Gets the details of a given FormulaOneTeam (more information in http://dbpedia.org/ontology/FormulaOneTeam) # noqa: E501

    :param id: The ID of the FormulaOneTeam to be retrieved
    :type id: str

    :rtype: FormulaOneTeam
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=FORMULAONETEAM_TYPE_URI,
        rdf_type_name=FORMULAONETEAM_TYPE_NAME, 
        kls=FormulaOneTeam)
