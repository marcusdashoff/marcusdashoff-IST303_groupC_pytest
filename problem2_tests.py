import pytest
from problem2_code import *

@pytest.fixture
def winner_1_fixture():
    return [[0, 1, 2], [0, 1, 0],[2, 1, 0]]

def test_1_should_win(winner_1_fixture):
    result = determine_board_state(winner_1_fixture)
    assert result == 1

@pytest.mark.xfail(reason="This test is expected to fail because 1 wins")
def test_1_should_win_2_shoudl_fail(winner_1_fixture):
    result = determine_board_state(winner_1_fixture)
    assert result == 2    

@pytest.mark.xfail(reason="This test is expected to fail because 1 wins")
def test_1_should_win_0_should_fail(winner_1_fixture):
    result = determine_board_state(winner_1_fixture)
    assert result == 0
    
@pytest.fixture
def winner_2_fixture():
    return [[0, 2, 1], [0, 2, 0],[1, 2, 0]]

def test_2_should_win(winner_2_fixture):
    result = determine_board_state(winner_2_fixture)
    assert result == 2
    
@pytest.mark.xfail(reason="This test is expected to fail because 2 wins")
def test_2_should_win_1_should_fail(winner_2_fixture):
    result = determine_board_state(winner_2_fixture)
    assert result == 1
    
@pytest.mark.xfail(reason="This test is expected to fail because 2 wins")
def test_2_should_win_0_should_fail(winner_2_fixture):
    result = determine_board_state(winner_2_fixture)
    assert result == 0

@pytest.fixture
def winner_0_fixture():
    return [[0, 1, 2],[0, 1, 0],[2, 2, 0]]

def test_0_should_win(winner_0_fixture):
    result = determine_board_state(winner_0_fixture)
    assert result == 0
    
@pytest.mark.xfail(reason="This test is expected to fail because 0 wins")
def test_0_should_win_1_should_fail(winner_0_fixture):
    result = determine_board_state(winner_0_fixture)
    assert result == 1
    
@pytest.mark.xfail(reason="This test is expected to fail because 0 wins")
def test_0_should_win_2_should_fail(winner_0_fixture):
    result = determine_board_state(winner_0_fixture)
    assert result == 2
    