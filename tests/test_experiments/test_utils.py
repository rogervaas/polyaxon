import os

import pytest

from factories.factory_experiments import ExperimentFactory
from libs.paths.experiments import (
    create_experiment_outputs_path,
    delete_experiment_logs,
    delete_experiment_outputs,
    get_experiment_logs_path,
    get_experiment_outputs_path
)
from tests.utils import BaseTest


@pytest.mark.experiments_mark
class TestExperimentUtils(BaseTest):
    DISABLE_RUNNER = True

    def setUp(self):
        super().setUp()
        self.experiment = ExperimentFactory()

    def test_experiment_logs_path_creation_deletion(self):
        experiment_logs_path = get_experiment_logs_path(self.experiment.unique_name)
        filepath = get_experiment_logs_path(self.experiment.unique_name)
        open(filepath, '+w')
        # Should be true, created by the signal
        assert os.path.exists(experiment_logs_path) is True
        assert os.path.exists(filepath) is True
        delete_experiment_logs(self.experiment.unique_name)
        assert os.path.exists(filepath) is False

    def test_experiment_outputs_path_creation_deletion(self):
        experiment_outputs_path = get_experiment_outputs_path(self.experiment.unique_name)
        assert os.path.exists(experiment_outputs_path) is False
        create_experiment_outputs_path(self.experiment.unique_name)
        assert os.path.exists(experiment_outputs_path) is True
        delete_experiment_outputs(self.experiment.unique_name)
        assert os.path.exists(experiment_outputs_path) is False
