from fake_data_maker import FakeDataMake
from postgresql_helper import PostgreDBHelper

# _fake_data_maker = FakeDataMake()
# _fake_data_maker.make_fake_data()

_db_helper = PostgreDBHelper()
_db_helper.add_fake_passager()
