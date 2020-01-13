import os
import pathlib
import uuid

import git

from til.application.repositories.interfaces import LearningRepository as ILearningRepo


class LearningRepository(ILearningRepo):

    def _generate_file_id(self):
        return uuid.uuid4()

    def _get_learning_base_path(self, learning):
        """Generates the base path from the learning timestamp."""

        base_path = self.settings.REPOSITORIES.LOCAL.DATA_PATH
        return pathlib.Path(os.path.join(
            base_path,
            str(learning.timestamp.year),
            str(learning.timestamp.month),
            str(learning.timestamp.day)
        ))

    def _get_learning_final_path(self, learning_base_path, learning_id):
        return pathlib.Path(os.path.join(
            learning_base_path,
            f"{learning_id}.{self.settings.REPOSITORIES.LOCAL.FILE_EXTENSION}"
        ))

    def _write(self, learning, learning_path):

        with open(learning_path, 'w') as f:
            f.write(learning.description)

    def _commit(self, learning, learning_base_path, learning_final_path):
        if not learning_final_path.exists():
            raise RuntimeError

        # TODO: move the cwd stuff to a proper context manager
        # with chdir(path):
        #     ...
        cwd = pathlib.Path.cwd()
        os.chdir(learning_base_path)

        _git = git.Git()
        _git.add(learning_final_path)
        commit_message = " ".join(part.lower() for part in learning.title.split())
        _git.commit(f"-m {commit_message}")

        os.chdir(cwd)

    def save(self, learning):

        learning_base_path = self._get_learning_base_path(learning)
        if not learning_base_path.exists():
            learning_base_path.mkdir(parents=True)

        learning_final_path = self._get_learning_final_path(
            learning_base_path,
            self._generate_file_id()
        )
        if learning_final_path.exists():
            raise RuntimeError

        self._write(learning, learning_final_path)

        self._commit(learning, learning_base_path, learning_final_path)

        return learning_final_path
