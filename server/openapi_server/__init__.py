from obasparql import QueryManager
from openapi_server.settings import *
import logging

try:
    logging.config.fileConfig(logging_file)
except:
    logging.error("Logging config file does not exist {}".format(logging_file))
    exit(0)

logger = logging.getLogger(__name__)

query_manager = QueryManager(queries_dir=QUERY_DIRECTORY,
                             context_dir=CONTEXT_DIRECTORY,
                             queries_types=QUERIES_TYPES,
                             endpoint=ENDPOINT,
                             endpoint_username=ENDPOINT_USERNAME,
                             endpoint_password=ENDPOINT_PASSWORD,
                             graph_base=ENDPOINT_GRAPH_BASE,
                             prefix=ENDPOINT_RESOURCE_PREFIX)



