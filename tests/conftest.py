from __future__ import annotations

import argparse
from unittest import mock

import pytest


@pytest.fixture(autouse=True)
def _mock_argparse():
    with mock.patch(
        "argparse.ArgumentParser.parse_args",
        return_value=argparse.Namespace(
            port=8000,
            hostname="localhost",
        ),
    ):
        yield


@pytest.fixture(autouse=True)
def _mock_flip():
    with mock.patch("pygame.display.flip"):
        yield


@pytest.fixture(autouse=True)
def _mock_event():
    with mock.patch("pygame.event.get", return_value=[]):
        yield


@pytest.fixture(autouse=True)
def _mock_mixer():
    with mock.patch("pygame.mixer"):
        yield


# @pytest.fixture(autouse=True)
# def _mock_panda():
#     with mock.patch("panda_py.Panda") as patch_panda:
#         patch_panda.return_value.get_orientation.return_value = np.array([0, 0, 0, 1])
#         patch_panda.return_value.get_position.return_value = np.zeros(3)
#         patch_panda.return_value.get_state.return_value = mock.MagicMock(
#             O_F_ext_hat_K=np.zeros(6),
#             q=np.zeros(7),
#             dq=np.zeros(7),
#             tau_ext_hat_filtered=np.zeros(7),
#         )
#         yield


# @pytest.fixture(autouse=True)
# def _mock_gripper():
#     with mock.patch("panda_py.libfranka.Gripper"):
#         yield


# @pytest.fixture(autouse=True)
# def _mock_environ():
#     with mock.patch.dict(
#         "os.environ",
#         {
#             "PANDA_LEFT": "garmi-left",
#             "PANDA_RIGHT": "garmi-right",
#             "PANDA": "panda",
#         },
#     ):
#         yield
