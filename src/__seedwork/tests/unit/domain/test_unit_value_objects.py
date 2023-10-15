from dataclasses import is_dataclass
import unittest
from unittest.mock import patch
import uuid
from __seedwork.domain.exceptions import InvalidUuidException

from __seedwork.domain.value_objects import UniqueEntityId


class TestUniqueEntityIdUnit(unittest.TestCase):
  
  def test_if_is_a_dataclass(self):
    self.assertTrue(is_dataclass(UniqueEntityId))

  def test_throw_exception_when_uuid_is_invalid(self):
    with patch.object(
        UniqueEntityId,
        '_UniqueEntityId__validate',
        autospec=True,
        side_effect=UniqueEntityId._UniqueEntityId__validate
      ) as mock_validade:
      with self.assertRaises(InvalidUuidException) as assert_error:
        UniqueEntityId('fake_id')
      mock_validade.assert_called_once()
      self.assertEqual(assert_error.exception.args[0], 'ID must be a valid UUID')

  def test_accept_uuid_passed_in_constructor(self):
    with patch.object(
        UniqueEntityId,
        '_UniqueEntityId__validate',
        autospec=True,
        side_effect=UniqueEntityId._UniqueEntityId__validate
      ) as mock_validade:
      value_object = UniqueEntityId('8f0738f5-5d47-465c-9f8f-9bdfec3d3fba')
      mock_validade.assert_called_once()
      self.assertEqual(value_object.id, '8f0738f5-5d47-465c-9f8f-9bdfec3d3fba')

    uuid_value = uuid.uuid4()
    value_object = UniqueEntityId(uuid_value)
    self.assertEqual(value_object.id, str(uuid_value))

  def test_generate_id_when_no_passed_id_in_constructor(self):
    with patch.object(
        UniqueEntityId,
        '_UniqueEntityId__validate',
        autospec=True,
        side_effect=UniqueEntityId._UniqueEntityId__validate
      ) as mock_validade:
      value_object = UniqueEntityId()
      uuid.UUID(value_object.id)
      mock_validade.assert_called_once()
