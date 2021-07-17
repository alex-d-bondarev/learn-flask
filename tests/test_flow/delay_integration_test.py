from learn_app.test_flow.models.delay import Delay


def test_delay_can_be_created():
    Delay(max_delay=100, random=False)
