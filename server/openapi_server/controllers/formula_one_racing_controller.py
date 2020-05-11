import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import FORMULAONERACING_TYPE_NAME, FORMULAONERACING_TYPE_URI

from openapi_server.models.formula_one_racing import FormulaOneRacing  # noqa: E501
from openapi_server import util

def formulaoneracings_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of FormulaOneRacing

    Gets a list of all instances of FormulaOneRacing (more information in http://dbpedia.org/ontology/FormulaOneRacing) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[FormulaOneRacing]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=FORMULAONERACING_TYPE_URI,
        rdf_type_name=FORMULAONERACING_TYPE_NAME, 
        kls=FormulaOneRacing)

def formulaoneracings_id_get(id):  # noqa: E501
    """Get a single FormulaOneRacing by its id

    Gets the details of a given FormulaOneRacing (more information in http://dbpedia.org/ontology/FormulaOneRacing) # noqa: E501

    :param id: The ID of the FormulaOneRacing to be retrieved
    :type id: str

    :rtype: FormulaOneRacing
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=FORMULAONERACING_TYPE_URI,
        rdf_type_name=FORMULAONERACING_TYPE_NAME, 
        kls=FormulaOneRacing)
