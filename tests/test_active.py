import numpy as np

from pm.active import active_return, active_weights, tracking_error


def test_active_weights_sum_zero_when_both_fully_invested():
    p=np.array([.6,.4]); b=np.array([.5,.5])
    assert np.isclose(active_weights(p,b).sum(),0)

def test_zero_active_weights_zero_te():
    w=np.array([.5,.5]); cov=np.eye(2)*.04
    assert np.isclose(tracking_error(w,w,cov),0)

def test_active_return_hand_example():
    assert np.isclose(active_return(0.08, 0.05), 0.03)
