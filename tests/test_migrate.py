from .context import bitbored

from bitbored import migrate
import pytest
import os


class TestMigrate(object):
    def test_migrate(self):
        m = migrate.Migrate(os.getcwd() + '/tests/resources/bit-test.txt')
        bits = m.migrate()
        assert len(bits) == 1

    def test_migrate_bits(self):
        m = migrate.Migrate(os.getcwd() + '/tests/resources/bits-test.txt')
        bits = m.migrate()
        assert len(bits) == 2
