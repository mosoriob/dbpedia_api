import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CONTROLLEDDESIGNATIONOFORIGINWINE_TYPE_NAME, CONTROLLEDDESIGNATIONOFORIGINWINE_TYPE_URI

from openapi_server.models.controlled_designation_of_origin_wine import ControlledDesignationOfOriginWine  # noqa: E501
from openapi_server import util

def controlleddesignationoforiginwines_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of ControlledDesignationOfOriginWine

    Gets a list of all instances of ControlledDesignationOfOriginWine (more information in http://dbpedia.org/ontology/ControlledDesignationOfOriginWine) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[ControlledDesignationOfOriginWine]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CONTROLLEDDESIGNATIONOFORIGINWINE_TYPE_URI,
        rdf_type_name=CONTROLLEDDESIGNATIONOFORIGINWINE_TYPE_NAME, 
        kls=ControlledDesignationOfOriginWine)

def controlleddesignationoforiginwines_id_get(id):  # noqa: E501
    """Get a single ControlledDesignationOfOriginWine by its id

    Gets the details of a given ControlledDesignationOfOriginWine (more information in http://dbpedia.org/ontology/ControlledDesignationOfOriginWine) # noqa: E501

    :param id: The ID of the ControlledDesignationOfOriginWine to be retrieved
    :type id: str

    :rtype: ControlledDesignationOfOriginWine
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CONTROLLEDDESIGNATIONOFORIGINWINE_TYPE_URI,
        rdf_type_name=CONTROLLEDDESIGNATIONOFORIGINWINE_TYPE_NAME, 
        kls=ControlledDesignationOfOriginWine)
