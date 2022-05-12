"""database dir. existence check"""
import os


def test_database_directory():
    """database check"""
    root = os.path.dirname(os.path.abspath(__file__))
    dbdir = os.path.join(root, '../database')
    assert os.path.exists(dbdir) is True