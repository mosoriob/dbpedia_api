import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CHEMICALELEMENT_TYPE_NAME, CHEMICALELEMENT_TYPE_URI

from openapi_server.models.chemical_element import ChemicalElement  # noqa: E501
from openapi_server import util

def chemicalelements_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of ChemicalElement

    Gets a list of all instances of ChemicalElement (more information in http://dbpedia.org/ontology/ChemicalElement) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[ChemicalElement]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CHEMICALELEMENT_TYPE_URI,
        rdf_type_name=CHEMICALELEMENT_TYPE_NAME, 
        kls=ChemicalElement)

def chemicalelements_id_get(id):  # noqa: E501
    """Get a single ChemicalElement by its id

    Gets the details of a given ChemicalElement (more information in http://dbpedia.org/ontology/ChemicalElement) # noqa: E501

    :param id: The ID of the ChemicalElement to be retrieved
    :type id: str

    :rtype: ChemicalElement
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CHEMICALELEMENT_TYPE_URI,
        rdf_type_name=CHEMICALELEMENT_TYPE_NAME, 
        kls=ChemicalElement)
