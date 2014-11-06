import os
import simplefeedapp
import unittest
import tempfile

class SimpleFeedTestCase(unittest.TestCase):

    def setUp(self):
        # self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        # flaskr.app.config['TESTING'] = True
        self.app = simplefeedapp.app.test_client()
        #flaskr.init_db()
        pass

    def tearDown(self):
        #os.close(self.db_fd)
        #os.unlink(flaskr.app.config['DATABASE'])
        pass

    def test_index(self):
        rv = self.app.get('/')
        assert 'Hello' in rv.data


if __name__ == '__main__':
    unittest.main()
