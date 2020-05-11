import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ARCHITECTURALSTRUCTURE_TYPE_NAME, ARCHITECTURALSTRUCTURE_TYPE_URI

from openapi_server.models.architectural_structure import ArchitecturalStructure  # noqa: E501
from openapi_server import util

def architecturalstructures_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of ArchitecturalStructure

    Gets a list of all instances of ArchitecturalStructure (more information in http://dbpedia.org/ontology/ArchitecturalStructure) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[ArchitecturalStructure]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ARCHITECTURALSTRUCTURE_TYPE_URI,
        rdf_type_name=ARCHITECTURALSTRUCTURE_TYPE_NAME, 
        kls=ArchitecturalStructure)

def architecturalstructures_id_get(id):  # noqa: E501
    """Get a single ArchitecturalStructure by its id

    Gets the details of a given ArchitecturalStructure (more information in http://dbpedia.org/ontology/ArchitecturalStructure) # noqa: E501

    :param id: The ID of the ArchitecturalStructure to be retrieved
    :type id: str

    :rtype: ArchitecturalStructure
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ARCHITECTURALSTRUCTURE_TYPE_URI,
        rdf_type_name=ARCHITECTURALSTRUCTURE_TYPE_NAME, 
        kls=ArchitecturalStructure)
