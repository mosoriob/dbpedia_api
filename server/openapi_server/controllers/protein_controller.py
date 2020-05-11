import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PROTEIN_TYPE_NAME, PROTEIN_TYPE_URI

from openapi_server.models.protein import Protein  # noqa: E501
from openapi_server import util

def proteins_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Protein

    Gets a list of all instances of Protein (more information in http://dbpedia.org/ontology/Protein) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Protein]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PROTEIN_TYPE_URI,
        rdf_type_name=PROTEIN_TYPE_NAME, 
        kls=Protein)

def proteins_id_get(id):  # noqa: E501
    """Get a single Protein by its id

    Gets the details of a given Protein (more information in http://dbpedia.org/ontology/Protein) # noqa: E501

    :param id: The ID of the Protein to be retrieved
    :type id: str

    :rtype: Protein
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PROTEIN_TYPE_URI,
        rdf_type_name=PROTEIN_TYPE_NAME, 
        kls=Protein)
