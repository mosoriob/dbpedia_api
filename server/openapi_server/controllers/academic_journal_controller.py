import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ACADEMICJOURNAL_TYPE_NAME, ACADEMICJOURNAL_TYPE_URI

from openapi_server.models.academic_journal import AcademicJournal  # noqa: E501
from openapi_server import util

def academicjournals_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of AcademicJournal

    Gets a list of all instances of AcademicJournal (more information in http://dbpedia.org/ontology/AcademicJournal) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[AcademicJournal]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ACADEMICJOURNAL_TYPE_URI,
        rdf_type_name=ACADEMICJOURNAL_TYPE_NAME, 
        kls=AcademicJournal)

def academicjournals_id_get(id):  # noqa: E501
    """Get a single AcademicJournal by its id

    Gets the details of a given AcademicJournal (more information in http://dbpedia.org/ontology/AcademicJournal) # noqa: E501

    :param id: The ID of the AcademicJournal to be retrieved
    :type id: str

    :rtype: AcademicJournal
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ACADEMICJOURNAL_TYPE_URI,
        rdf_type_name=ACADEMICJOURNAL_TYPE_NAME, 
        kls=AcademicJournal)
