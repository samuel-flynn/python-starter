import logging
import os
import json
import logging.config

__VERSION__ = '1.0.0'

resources_dir = os.path.join(os.path.dirname(__file__), 'resources')

with open(os.path.join(resources_dir, 'logging-config.json'), 'r') as fp:
    logging_config = json.load(fp)
    logging.config.dictConfig(logging_config)

logging.getLogger().info('Logging initialized')