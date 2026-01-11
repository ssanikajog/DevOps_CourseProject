from leave_management import check_leave


def test_leave_approved():
    leave_balance = {"E001": 20}
    status, remaining = check_leave("E001", 5, leave_balance)

    assert status == "Leave Approved"
    assert remaining == 15


def test_leave_rejected_insufficient_balance():
    leave_balance = {"E002": 10}
    status, remaining = check_leave("E002", 15, leave_balance)

    assert status == "Leave Rejected (Insufficient balance)"
    assert remaining == 10


def test_invalid_employee():
    leave_balance = {"E001": 20}
    status, remaining = check_leave("E999", 3, leave_balance)

    assert status == "Employee not found"
    assert remaining is None


def test_invalid_leave_days():
    leave_balance = {"E001": 20}
    status, remaining = check_leave("E001", -2, leave_balance)

    assert status == "Invalid number of leave days"
    assert remaining == 20
