import pytest

from til.application.repositories import interfaces


def test_learning_repository_mandatory_save():
    class FakeLearning(interfaces.LearningRepository):
        pass

    with pytest.raises(TypeError):
        FakeLearning()
