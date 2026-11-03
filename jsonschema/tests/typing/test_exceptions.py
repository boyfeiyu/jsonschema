"""
Errors from false schemas have no failed keyword.
"""

from typing import assert_type

from jsonschema.exceptions import ErrorTree, SchemaError, ValidationError

error = ValidationError("False schema does not allow 12", validator=None)
assert_type(error.validator, str | None)
assert_type(SchemaError("a message", validator=None).validator, str | None)
keyword_error = ValidationError("a message", validator="type")
assert_type(keyword_error.validator, str | None)

# None keys must be accepted without making the mapping or its values Any.
tree = ErrorTree([error, keyword_error])
assert_type(tree.errors[None], ValidationError)
assert_type(tree.errors["type"], ValidationError)
