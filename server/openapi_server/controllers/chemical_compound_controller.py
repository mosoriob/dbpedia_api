import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CHEMICALCOMPOUND_TYPE_NAME, CHEMICALCOMPOUND_TYPE_URI

from openapi_server.models.chemical_compound import ChemicalCompound  # noqa: E501
from openapi_server import util

def chemicalcompounds_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of ChemicalCompound

    Gets a list of all instances of ChemicalCompound (more information in http://dbpedia.org/ontology/ChemicalCompound) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[ChemicalCompound]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CHEMICALCOMPOUND_TYPE_URI,
        rdf_type_name=CHEMICALCOMPOUND_TYPE_NAME, 
        kls=ChemicalCompound)

def chemicalcompounds_id_get(id):  # noqa: E501
    """Get a single ChemicalCompound by its id

    Gets the details of a given ChemicalCompound (more information in http://dbpedia.org/ontology/ChemicalCompound) # noqa: E501

    :param id: The ID of the ChemicalCompound to be retrieved
    :type id: str

    :rtype: ChemicalCompound
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CHEMICALCOMPOUND_TYPE_URI,
        rdf_type_name=CHEMICALCOMPOUND_TYPE_NAME, 
        kls=ChemicalCompound)
