from datetime import date

from planner import completion_rate, days_left, is_urgent, sort_by_due


# This test is already written for you. Read it, then run pytest.
def test_days_left_counts_days_until_due():
    # Arrange
    today = date(2026, 10, 19)
    due = date(2026, 10, 22)
    # Act
    result = days_left(due, today)
    # Assert
    assert result == 4


# Now write the tests below. Use the same three steps: Arrange, Act, Assert.
# TODO 1: days_left is negative when the task is overdue.
def test_days_left_is_negative_when_task_is_overdue():
    # Arrange
    today = date(2026, 10, 19)
    due = date(2026, 10, 18)
    assert days_left(due, today) == -1

# TODO 2: is_urgent is True when the task is due tomorrow.
def test_is_urgent_when_due_tomorrow():
    today = date(2026, 10, 19)
    due = date(2026, 10, 20)
    assert is_urgent(due, today) is True

# TODO 3: is_urgent is True when the task is due in exactly 2 days (the limit).
def test_is_urgent_when_due_in_exactly_two_days():
    today = date(2026, 10, 19)
    due = date(2026, 10, 21)
    assert is_urgent(due, today, limit=2) is True

# TODO 4: is_urgent is False when the task is overdue.
def test_is_urgent_is_false_when_task_is_overdue():
    today = date(2026, 10, 19)
    due = date(2026, 10, 18)
    assert is_urgent(due, today) is False

# TODO 5: sort_by_due puts the soonest task first.
def test_sort_by_due_puts_soonest_task_first():
    task_later = {"name": "Task A", "due": date(2026, 10, 25)}
    task_soonest = {"name": "Task B", "due": date(2026, 10, 20)}
    tasks = [task_later, task_soonest]
    sorted_tasks = sort_by_due(tasks)
    assert sorted_tasks[0] == task_soonest
    
# TODO 6: completion_rate returns 0.0 when there are no tasks.
def test_completion_rate_returns_zero_when_no_tasks():
    completed_count = 0
    total_count = 0
    rate = completion_rate(completed_count, total_count)
    assert rate == 0.0

# TODO 7: completion_rate(1, 3) returns 33.3.
def test_completion_rate_one_of_three_returns_thirty_three_point_three():
    completed_count = 1
    total_count = 3
    rate = completion_rate(completed_count, total_count)
    assert rate == 33.3
