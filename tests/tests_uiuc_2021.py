import numpy as np
from PySDM_examples.UIUC_2021.frozen_fraction import FrozenFraction
from PySDM.physics import constants as const

TOTAL_PARTICLE_NUMBER =1
DROPLET_VOLUME = 1
VOLUME = 1
FF = FrozenFraction(volume=VOLUME, total_particle_number=TOTAL_PARTICLE_NUMBER, droplet_volume=DROPLET_VOLUME)


class TestFrozenFraction():
    @staticmethod
    def test_qi2ff():
        all_frozen = FF.qi2ff(TOTAL_PARTICLE_NUMBER * DROPLET_VOLUME * const.rho_w / VOLUME)
        np.testing.assert_almost_equal(all_frozen, 1)

    @staticmethod
    def test_ff2qi():
        assert FF.qi2ff(FF.ff2qi(1)) == 1
