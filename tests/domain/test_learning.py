import datetime
import string

from hypothesis import assume, given, strategies as st

from til.domain.learning import Learning

@given(st.from_type(Learning))
def test_learning_title_validator(learning):
    assume(learning.title and learning.description and learning.timestamp)

    assert isinstance(learning.title, str)
    assert isinstance(learning.description, str)
    assert isinstance(learning.timestamp, datetime.date)
