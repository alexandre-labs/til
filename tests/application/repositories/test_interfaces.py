import pytest

from til.application.repositories import interfaces


def test_learning_repository_mandatory_ping():

    class FakeLearning(interfaces.LearningRepository):
        def save(self, learning):
            pass

    with pytest.raises(TypeError):
        FakeLearning()


def test_learning_repository_mandatory_save():

    class FakeLearning(interfaces.LearningRepository):
        def ping(self):
            pass

    with pytest.raises(TypeError):
        FakeLearning()
