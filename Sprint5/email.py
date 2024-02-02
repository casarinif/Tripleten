import jsonschema
# noinspection PyUnresolvedReferences
import email.message

# Define the schema for the email body
schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'age': {'type': 'integer'}
    }
}

# Parse the email message
message = email.message.Message.from_bytes(b'...')

# Validate the email body against the schema
try:
    jsonschema.validate(message.get_body(decode=True), schema)
except jsonschema.ValidationError as e:
    # Handle the validation error
    print(e)

from my_module import email_check

email_check('stewie@family.guy')