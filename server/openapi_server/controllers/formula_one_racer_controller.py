import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import FORMULAONERACER_TYPE_NAME, FORMULAONERACER_TYPE_URI

from openapi_server.models.formula_one_racer import FormulaOneRacer  # noqa: E501
from openapi_server import util

def formulaoneracers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of FormulaOneRacer

    Gets a list of all instances of FormulaOneRacer (more information in http://dbpedia.org/ontology/FormulaOneRacer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[FormulaOneRacer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=FORMULAONERACER_TYPE_URI,
        rdf_type_name=FORMULAONERACER_TYPE_NAME, 
        kls=FormulaOneRacer)

def formulaoneracers_id_get(id):  # noqa: E501
    """Get a single FormulaOneRacer by its id

    Gets the details of a given FormulaOneRacer (more information in http://dbpedia.org/ontology/FormulaOneRacer) # noqa: E501

    :param id: The ID of the FormulaOneRacer to be retrieved
    :type id: str

    :rtype: FormulaOneRacer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=FORMULAONERACER_TYPE_URI,
        rdf_type_name=FORMULAONERACER_TYPE_NAME, 
        kls=FormulaOneRacer)
